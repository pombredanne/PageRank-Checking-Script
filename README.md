PageRank Checking Script
========================

** This is a few years old and Google might throttle you immediately. Just keeping this up for reference **

A Python script that checks the PageRank values of a given URL list. Worked with chunks of ~2500 URLs every 20 minutes.
Be advised that you should have a "safety" IP address to do this from. Shouldn't matter with small batches though. You'll 
need a working version of Python installed. http://www.python.org/download/

Reads from source list 'urlList.txt'. One URL per line

Run 'begin-check.py'

Dumps list of PageRanks into PRdump.txt

Why would I use this?
========================

If you want to monitor the PageRank changes among a spread of your websites over time, this could record useful information.
Know how Google is keeping tabs on your property.

What needs improvement?
========================

Um, everything. 

Wish list: output to CSV, add curl response time for each URL, etc, etc. This was a quick and dirty solution to a small problem, and could be fleshed out.

