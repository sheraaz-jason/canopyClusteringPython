#! /usr/bin/env python

import sys
import DataPoint
import subprocess

# Check for sufficient arguments
if len(sys.argv) < 2:
	print("ERROR: Insufficient arguments")
	sys.exit(-1)

# List to hold canopy centers
canopyCenters = []

# Read canopy center file
cat = subprocess.Popen(["hadoop", "fs", "-cat", sys.argv[1]], stdout=subprocess.PIPE)
for line in cat.stdout:
	if line.find("Warning:") == 0:
	 	continue
	(key,value) = line.split("\t")
	dp = DataPoint.DataPoint(value.strip())
	canopyCenters.append(dp)

# Assign points to canopies
for line in sys.stdin:
	dp = DataPoint.DataPoint(line.strip())
	insert = True
 	for canopyCenter in canopyCenters:	
 		if dp.checkT1(canopyCenter):
 			print(canopyCenter.toString() + "\t" + dp.toString())