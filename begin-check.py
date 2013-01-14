#!/usr/bin/env python
#  Thanks to Corey Goldberg (http://code.google.com/p/corey-projects/) for his work on pagerank.py

import pagerank

sourceFile = open ('urlList.txt', 'r')
listDump = open ('PRdump.txt', 'w')

for line in sourceFile:
  rank = pagerank.get_pagerank(line)
	print >>listDump, rank, "\n",
