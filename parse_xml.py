#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from zipfile import ZipFile
import os
import csv
from lxml import etree

pathZip = "/tmp/zipFiles"
arrFirst = []
arrSecond = []

pathCsv = "/tmp/csvFiles"
try:
	os.mkdir(pathCsv)
except:
	print("directory " + pathCsv + " already exists")

for fileZip in os.listdir(pathZip):
	inputZip = ZipFile(pathZip + '/' + fileZip)
	for fileXml in inputZip.namelist():
		tree = etree.XML(inputZip.read(fileXml))
		getIdValue = tree.xpath('//*[@name="id"]')[0].get('value')
		getLevelValue = tree.xpath('//*[@name="level"]')[0].get('value')
		arrFirst.append([getIdValue, getLevelValue])
		for node in tree.xpath('/root/objects/object'):
			arrSecond.append([getIdValue, node.get('name')])

with open(pathCsv + '/file1.csv', "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(arrFirst)

with open(pathCsv + '/file2.csv', "w", newline="") as file:
	writer = csv.writer(file)
	writer.writerows(arrSecond)

