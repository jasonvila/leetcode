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

# soup = BeautifulSoup(urlopen("https://leetcode.com/problems/count-the-repetitions/#/description"), "html.parser")

# print(str(soup.find("div", {"class" : "question-description"})).encode("utf-8"))

# if not os.path.exists("count-the-repetitions"):
# 	os.makedirs("count-the-repetitions")

# f = open(os.getcwd() + "/count-the-repetitions/README.md", "w")
# f.write(str(soup.find("div", {"class" : "question-description"}).encode("utf-8")))
# f.close()

def fetch_problem(p):
	p_id = str(p['stat']['question_id'])
	p_slug = p['stat']['question__title_slug']
	
	print(str(p_id) + " : " + p_slug)

	soup = BeautifulSoup(urlopen("https://leetcode.com/problems/" + p_slug + "/#/description"), "html.parser")
	
	while len(p_id) < 3:
		p_id = "0" + p_id
	
	if not os.path.exists(p_id + "_" + p_slug):
		os.makedirs(p_id + "_" + p_slug)

	description = soup.find("div", {"class" : "question-description"})

	f = open(os.getcwd() + "/" + p_id + "_" + p_slug + "/README.md", "w")

	if description:
		print("\n\n" + str(description.encode("utf-8")) + "\n\n")
		f.write(str(description.encode("utf-8")))
	else:
		print("\n\nNo Description\n\n")
		f.write("No Description")
	f.close()


for problem in problems['stat_status_pairs']:
	fetch_problem(problem)
	t = threading.Thread(target = fetch_problem, args = (problem,))
	t.start()
