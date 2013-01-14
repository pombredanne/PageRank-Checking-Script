#!/usr/bin/env python
#  Thanks to Corey Goldberg (http://code.google.com/p/corey-projects/) for his work on pagerank.py

import pagerank

file = open ('urlList.txt', 'r')
dump = open ('PRdump.txt', 'w')

for line in file:
  rank = pagerank.get_pagerank(line)
	print >>dump, rank, "\n",
