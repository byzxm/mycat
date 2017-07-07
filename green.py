# Copyright (c) 2015 Angus H. (4148)
# Distributed under the GNU General Public License v3.0 (GPLv3).

from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import os

# returns a date string for the date that is N days before STARTDATE
def get_date_string(n, startdate):
	d = startdate + timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	rtn2 = d.strftime("%Y-%m-%d 03:14:15")
	return rtn, rtn2

# main app
def main(argv):
	if len(argv) < 1 or len(argv) > 2:
		print "Error: Bad input."
		sys.exit(1)
	n = int(argv[0])
	if len(argv) == 1:
		startdate = date.today()
	if len(argv) == 2:
		startdate = date(int(argv[1][0:4]), int(argv[1][5:7]), int(argv[1][8:10]))
	i = 0
	while i <= n:
		curdate, c2 = get_date_string(i, startdate)
		os.environ["FAKETIME"] = c2
		print(curdate, c2)
		subprocess.call("date")
		num_commits = randint(1, 5)
		for commit in range(0, num_commits):
			#subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > worklog.txt; git add worklog.txt; git commit -m 'update " + curdate[:10] + " 2018'; git push;", shell=True)
			subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > worklog.txt; git add worklog.txt; git commit -m 'update " + curdate[:10] + "'; ", shell=True)
		i += 1
	#subprocess.call("git rm worklog.txt; git commit -m 'delete'; git push;", shell=True)

if __name__ == "__main__":
	main(sys.argv[1:])
