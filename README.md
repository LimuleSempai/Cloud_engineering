# Cloud_engineering

from confluet_kafka import producer
import socket

conf = {'bootstrap.servers','localhost:9094','client_id':socket.gethostname{})

producer = Producer(conf)

producer.product("aimene", key="key", value="value")
producer.flush()
