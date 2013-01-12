#!/usr/bin/env python
#  Thanks to Corey Goldberg (http://code.google.com/p/corey-projects/) for his work on pagerank.py

import pagerank

f = open ('urlList.txt', 'r')
d = open ('PRdump.txt', 'w')

for line in f:
  rank = pagerank.get_pagerank(line)
	print >>d, rank, "\n",
