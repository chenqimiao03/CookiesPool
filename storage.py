import random
import redis

class RedisClient:

	def __init__(self, name):
		self._db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
		self.name = name

	def set(self, key, value):
		self._db.hset(self.name, key, value)

	def get(self, key):
		return self._db.hget(self.name, key)

	def value(self):
		return random.choice(self._db.hvals(self.name))

	def delete(self, key):
		return self._db.hdel(self.name, key)

	def __len__(self):
		return self._db.hlen(self.name)

	def keys(self):
		return self._db.keys(self.name)

	def all(self):
		return self._db.hgetall(self.name)
