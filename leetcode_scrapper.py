import os
import json
import threading
from urllib.error import HTTPError
from urllib.request import urlopen
import bs4
from bs4 import BeautifulSoup

# soup = BeautifulSoup(urlopen("https://leetcode.com/problemset/algorithms/"))

problems = json.loads(urlopen("https://leetcode.com/api/problems/algorithms/").read().decode())

print("Leetcode Api Result \n\n\n" + str(problems))

print("\n\n\nLeetcode Api Problems\n\n")

for problem in problems['stat_status_pairs']:
	print(str(problem['stat']['question_id']) + " : " + problem['stat']['question__title_slug'])