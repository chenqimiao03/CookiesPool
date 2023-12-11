import requests
from loguru import logger
from storage import RedisClient


class _Tester:
	
	def __init__(self):
		self.cookies = RedisClient('scrape.center-antispider6:cookies')

	def test(self, username, cookies):
		raise NotImplementedError

	def run(self):
		for username, cookies in self.cookies.all().items():
			self.test(username, cookies)

class Tester(_Tester):
	def __init__(self):
		_Tester.__init__(self)

	def test(self, username, cookies):
		logger.info(f'testing credential for {username}')
		try:
			r = requests.get('https://antispider6.scrape.center/login', headers={
				'Cookie': cookies}, timeout=10, allow_redirects=False)
			if r.status_code == 200:
				logger.info('credential is valid')
			else:
				logger.info('credential is not valid, delete it')
				self.cookies.delete(username)
		except ConnectionError:
			logger.info('test failed, check network')

if __name__ == '__main__':
	Tester().run()

