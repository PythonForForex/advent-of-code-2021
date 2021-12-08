import sqlite3
from pathlib import Path

import requests


db = f'{Path.home()}/.mozilla/firefox/v69ttedg.default-release/cookies.sqlite'
con = sqlite3.connect(db, timeout=10)
cursor = con.cursor()
query_cookies = cursor.execute('SELECT * from moz_cookies')
get_cookies = query_cookies.fetchall()

cookie_jar = {}
for line in get_cookies:
	if '.adventofcode.com' in line:
		cookie_jar[line[2]]=line[3]


def get_input(day=1):
	if cookie_jar:
		r = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookie_jar)
		r.raise_for_status()

		with open(f'day{day}.txt', 'w') as e:
			e.write(r.text)

		return r.text
	print('problem getting input (cookies)')

