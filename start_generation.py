#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from lxml.builder import E
from lxml import etree
from random import randint
from zipfile import ZipFile
import uuid
import os

pathXml = "/tmp/xmlFiles"
try:
	os.mkdir(pathXml)
except:
	print("directory " + pathXml + " already exists")

pathZip = "/tmp/zipFiles"
try:
	os.mkdir(pathZip)
except:
	print("directory " + pathZip + " already exists")

for z in range(50):
	for x in range(100):
		genDoc = etree.Element('root')
		objectsTag = etree.Element('objects')

		for ob in range(randint(1, 10)):
			objectsTag.append(E.object(name=str(uuid.uuid4().hex)))

		genDoc.append(E.var(name="id", value=str(uuid.uuid4())))
		genDoc.append(E.var(name="level", value=str(randint(1, 100))))
		genDoc.append(objectsTag)

		resStr = etree.tostring(genDoc, xml_declaration=True, encoding='utf-8', pretty_print=True)
		
		genNameFile = uuid.uuid4().hex + '.xml'
		xmlFile = open(pathXml + '/' + genNameFile, 'wb')
		xmlFile.write(resStr)
		xmlFile.close()
	genNameZip = uuid.uuid4().hex + '.zip'
	zf = ZipFile(pathZip + '/' + genNameZip, 'w')
	for filename in os.listdir(pathXml):
		zf.write(pathXml + '/' + filename, os.path.basename(pathXml + '/' + filename))
		os.remove(pathXml + '/' + filename)
	zf.close()
