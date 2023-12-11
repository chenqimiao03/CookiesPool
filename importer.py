import csv
from storage import RedisClient


def main():
	reader = csv.reader(open('accounts.csv'))
	_db = RedisClient('scrape.center-antispider6:accounts')
	for index, row in enumerate(reader):
		if not index:
			continue
		_db.set(row[0], row[1])

if __name__ == '__main__':
	main()
