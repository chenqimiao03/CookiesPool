import time
import multiprocessing
from loguru import logger
from storage import RedisClient
from generator import Generator
from tester import Tester


class Scheduler:

	def run_tester(self, cycle=600):
		loop = 0
		tester = Tester()
		while True:
			logger.debug(f'tester loop {loop} start...')
			tester.run()
			loop += 1
			time.sleep(cycle)

	def run_generator(self, cycle=600):
		loop = 0
		generator = Generator()
		while True:
			logger.debug(f'generator loop {loop} start...')
			loop += 1
			generator.run()
			time.sleep(cycle)

	def run(self):
		try:
			logger.info(f'starting cookies pool for website scrape.center-antispider6')
			tester_process = multiprocessing.Process(target=self.run_tester)
			logger.info(f'starting tester, pid {tester_process.pid}...')
			tester_process.start()
			generator_process = multiprocessing.Process(target=self.run_generator)
			logger.info(f'starting generator, pid {generator_process.pid}...')
			generator_process.start()
			tester_process.join()
			generator_process.join()
		except KeyboardInterrupt:
			logger.info('received keyboard interrupt signal')
			tester_process.terminate()
			generator_process.terminate()


if __name__ == '__main__':
	Scheduler().run()
