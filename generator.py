import requests
from loguru import logger
from storage import RedisClient

class _Generator:

	def __init__(self):
		self.accounts = RedisClient('scrape.center-antispider6:accounts')
		self.cookies = RedisClient('scrape.center-antispider6:cookies')

	def generate(self, username, password):
		raise NotImplementedError

	def run(self):
		logger.debug('start to run generator')
		for username, password in self.accounts.all().items():
			if self.cookies.get(username):
				continue
			logger.debug(f'start to generate cookie of {username}')
			self.generate(username, password)

class Generator(_Generator):

	def __init__(self):
		_Generator.__init__(self)
	
	def generate(self, username, password):
		if self.cookies.get(username):
			logger.debug(f'credential of {username} exists, skip')
			return
		session = requests.Session()
		session.post('https://antispider6.scrape.center/login', data={
			'username': username,
			'password': password
		})
		cookies = []
		for cookie in session.cookies:
			print(cookie.name, cookie.value)
			cookies.append(f'{cookie.name}={cookie.value}')
		cookies = ';'.join(cookies)
		logger.debug(f'get credential {cookies}')
		self.cookies.set(username, cookies)

if __name__ == '__main__':
	Generator().generate('user1000', 'user1000@123')
