import sqlite3
from pathlib import Path
from sqlite3.dbapi2 import OperationalError

import requests


cookie_jar = {}

def get_cookie():
	if cookie_jar:
		return cookie_jar

	try:
		db = f'{Path.home()}/.mozilla/firefox/v69ttedg.default-release/cookies.sqlite'
		con = sqlite3.connect(db, timeout=3)	
		cursor = con.cursor()
		query_cookies = cursor.execute('SELECT * from moz_cookies')
		get_cookies = query_cookies.fetchall()

		for line in get_cookies:
			if '.adventofcode.com' in line:
				cookie_jar[line[2]]=line[3]
		return cookie_jar
	except OperationalError:
		return False


def get_input(day=1):
	cookie_jar = get_cookie()
	if not cookie_jar:
		try:
			with open(f'inputs/day{day}.txt', 'r') as e:
				raw_input = e.read()
			return raw_input
		except:
			raise OperationalError('Input file unavailable')
	
	r = requests.get(f'https://adventofcode.com/2021/day/{day}/input', cookies=cookie_jar)
	r.raise_for_status()

	with open(f'inputs/day{day}.txt', 'w') as e:
		e.write(r.text)

	return r.text
