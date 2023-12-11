import csv
import requests

def save(accounts):
	fp = open('accounts.csv', 'a', encoding='utf-8')
	writer = csv.writer(fp)
	writer.writerow(['username', 'password', 'email'])
	for account in accounts:
		writer.writerow([account.get('username'), 
				account.get('password1'), 
				account.get('email')])
	fp.close()

def main():
	accounts = []
	url = 'https://antispider6.scrape.center/register'
	for i in range(1, 1001):
		data = {
			'username': f'user{i}',
			'email': f'user{i}@sdtbu.edu.cn',
			'password1': f'user{i}@123',
			'password2': f'user{i}@123'
		}
		r = requests.post(url=url, data=data)
		if r.status_code == 200:
			print(f'user: user{i} registered successfully')
			accounts.append(data)
	if len(accounts):
		save(accounts)

if __name__ == '__main__':
	main()
