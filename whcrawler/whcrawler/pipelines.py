# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from kafka import KafkaProducer
from scrapy.exceptions import DropItem
import redis
import json


class KafkaSendPipeline(object):

    def open_spider(self, spider):
        self.kafka_producer = KafkaProducer(
            **{
                'bootstrap_servers': 'pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092',
                'sasl_mechanism': 'PLAIN',
                'security_protocol': 'SASL_SSL',
                'sasl_plain_username': 'BJQ62HTRFKMKDCIM',
                'sasl_plain_password': 'C4PzwqbfC7YYXIFqvCtQxJ+BgcQDrQ+/5o8QE1JsVVk31456wdDbO7anO831q6Pp'
            },
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=str.encode)


    def process_item(self, item, spider):

        self.kafka_producer.send("wh-immo", item, item.get("id", ""))

        return item


class RedisPreSelectPipeline(object):

    def open_spider(self, spider):
        self.redis_db = redis.Redis(host='localhost', port=6379, db=1)
        


    def process_item(self, item ,spider):

        if self.redis_db.get(item.get("id", "")):
            raise DropItem("Realty already exists (id: {})".format(item.get("id", "")))

        return item