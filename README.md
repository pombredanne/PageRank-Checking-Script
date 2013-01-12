PageRank Checking Script
========================

** This is a few years old and Google might throttle you immediately. Just keeping this up for reference **

A Python script that checks the PageRank values of a given URL list. Worked with chunks of ~2500 URLs every 20 minutes.
Be advised that you should have a "safety" IP address to do this from. Shouldn't matter with small batches though.

Reads from urlList.txt. One URL per line

Run 'begin-check.py'

Dumps list of PageRanks into PRdump.txt

