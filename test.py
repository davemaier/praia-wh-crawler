from kafka import KafkaProducer


p = KafkaProducer(**{
    'bootstrap_servers': 'pkc-ewzgj.europe-west4.gcp.confluent.cloud:9092',
    'sasl_mechanism': 'PLAIN',
    'security_protocol': 'SASL_SSL',
    'sasl_plain_username': 'BJQ62HTRFKMKDCIM',
    'sasl_plain_password': 'C4PzwqbfC7YYXIFqvCtQxJ+BgcQDrQ+/5o8QE1JsVVk31456wdDbO7anO831q6Pp'
})


future = p.send('python-test', value=b'pipsifipsi')

result = future.get(timeout=60)

print(result)

p.flush()
