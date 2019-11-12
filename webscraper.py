import redis
from realty import Realty
#from confluent_kafka.avro import AvroProducer
#from confluent_kafka import avro
from confluent_kafka import Producer

conf = {
    "bootstrap.servers": "pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092",
    "sasl.mechanisms": "PLAIN",
    "security.protocol": "SASL_SSL",
    "sasl.username": "CYKVGYPEZSU4T3QO",
    "sasl.password": "RHRkHBLWl4hUMc7FitA1En38oe6fkxLlYvvJno5uoHKzRqrE2rkqdoN/dOmsgEw0"
    # "schema.registry.url": "https://psrc-lgkvv.europe-west3.gcp.confluent.cloud",
    # "schema.registry.basic.auth.credentials.source": "USER_INFO",
    # "schema.registry.basic.auth.user.info": "DPOPNMGULHPXKRZI:TmEljmZi4Dy67pRf035YXi1kHm9D3/P7w/eievRmEk86rBJ1XzhzViUPBkOoKpN4"

}

# record_schema = avro.loads("""
# {
#   "fields": [
#     {
#       "name": "title",
#       "type": "string"
#     },
#     {
#       "name": "id",
#       "type": "int"
#     },
#     {
#       "name": "description",
#       "type": "string"
#     },
#     {
#       "name": "price",
#       "type": "float"
#     },
#     {
#       "name": "post_code",
#       "type": "int"
#     },
#     {
#       "default": "NONE",
#       "name": "street",
#       "type": "string"
#     },
#     {
#       "default": "NONE",
#       "name": "city",
#       "type": "string"
#     },
#     {
#       "default": "NONE",
#       "name": "country",
#       "type": "string"
#     },
#     {
#       "default": "NONE",
#       "name": "house_number",
#       "type": "string"
#     }
#   ],
#   "name": "realty",
#   "type": "record"
# }
# """)

# producer = AvroProducer(conf, default_value_schema=record_schema)

def delivery_callback(err, msg):
        if err:
            print('%% Message failed delivery: %s\n' % err)
        else:
            print('%% Message delivered to %s [%d] @ %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))
test_producer = Producer({
           'bootstrap.servers': 'pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092',
           'sasl.mechanisms': 'PLAIN',
           'security.protocol': 'SASL_SSL',
           'sasl.username': 'CYKVGYPEZSU4T3QO',
           'sasl.password': 'RHRkHBLWl4hUMc7FitA1En38oe6fkxLlYvvJno5uoHKzRqrE2rkqdoN/dOmsgEw0'
    })

test_producer.produce("users", "hiper", "lagos", callback=delivery_callback)

test_producer.poll(0)

# test_realty = {
#             "title": "Nai", 
#             "id": 2332,
#             "description": "superHaus", 
#             "price": 123, 
#             "post_code": 4910, 
#             "street": "Roseggerstraße", 
#             "city": "Ried im Innkreis", 
#             "country": "AT", 
#             "house_number": "12"
#         }

# producer.produce(topic="wh-immo", value=test_realty, callback=lambda err, msg: print("{}{}".format(err, msg)))

 