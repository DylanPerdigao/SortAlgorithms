#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
import sys
import os
import time
import random
from ShellSort import *
from RadixSort import *

def rearrangeGlobal(l):
	aux = dict()
	for elem in l:
		if elem[0] not in aux:
			aux.update({elem[0]:1})
		else:
			count = 1 + aux.get(elem[0])
			aux.update({elem[0]:count})
	return list(aux.items())

def rearrangeUser(l):
	dicio = dict()
	aux = list()
	for elem in l:
		dicio.setdefault(elem[0],list())
	for elem in l:
		if elem[1] not in dicio[elem[0]]:
			dicio[elem[0]].append(elem[1])
	for key,val in dicio.items():	
		aux.append((key,len(val)))
	return aux

def search(l):
	string = ""
	i=-1
	aux=l[-1][1]
	#caso varios vai até primeiro elemento com o numero mais alto
	while abs(i)<=len(l) and aux==l[i][1]:
		i-=1
	i+=1
	#percorre normalmente
	for k in range(len(l)-abs(i),len(l)):
		string += str(l[k][0])+" "
		
	string = string[:-1] + "\n"
	return string
	
def searchBy(category,algorithm):
	l = original
	if category == "GLOBAL":
		l = rearrangeGlobal(l)
	elif category == "USER":
		l = rearrangeUser(l)
	if algorithm == SHELL_SORT:
		l = insertionSort(l)
		l = shellSort(l,key)
	elif algorithm == RADIX_SORT:
		l = convertCounterInString(l)
		l = radixSort(l)
	return search(l)

def convertCounterInString(l):
	newList = list()
	maximum = getMax(l)
	for elem in l:
		zeros=""
		for i in range(len(str(maximum))-len(str(elem[1]))):
			zeros += "0"
		index = zeros + str(elem[1])
		newList.append((elem[0],index))
	return newList

def readText(src):
	l = list()
	elem = list()
	allWordList = list()
	wordList = list()
	allUserList = list()
	userList = list()
	peerList = list()
	with open(src,'r',encoding="utf-8") as f:
		lines = f.readlines()
	for line in lines:
		elem = line.upper().split()
		l.append((elem[0],elem[1]))
		allWordList.append(elem[0])
		allUserList.append(elem[1])
		if elem not in peerList:
			peerList.append(elem)
		if elem[0] not in wordList:
			wordList.append(elem[0])
		if elem[1] not in userList:
			userList.append(elem[1])
	return l, len(allWordList),len(wordList),len(allUserList),len(userList),len(peerList)

if __name__=='__main__':
	SHELL_SORT = "SHELL_SORT"
	RADIX_SORT = "RADIX_SORT"
	##########CONFIG#########
	EXECUTIONS_READ = 1
	EXECUTIONS_ALGORITHM = 1
	PATH = "tests/"
	key = "5-3-1"
	#########################
	l = list()
	original=list()
	filesNames = list()
	with os.scandir(PATH) as files:
		for f in files:
			if f.name[0]!=".":
				filesNames.append(f.name)
		filesNames.sort()
	for text in filesNames:
		times = list()
		for i in range(EXECUTIONS_READ):
			t = time.process_time()
			original,totalWords,numWords,totalUsers,numUsers,numPeers = readText(PATH+text)
			times.append(time.process_time()-t)
		sys.stdout.write("=====================\nTEXT {}:\n---------------------\n".format(text[-5]))
		sys.stdout.write("Distincts/Total words:\t\t{}/{}\n".format(numWords,totalWords))
		sys.stdout.write("Distincts/Total users:\t\t{}/{}\n".format(numUsers,totalUsers))
		sys.stdout.write("Distincts peers:\t\t{}\n".format(numPeers))
		sys.stdout.write("Loading Time [ms]:\t\t{}\n\n".format(sum(times)*1000/len(times)))
		for algorithm in [SHELL_SORT,RADIX_SORT]:
			sys.stdout.write("{}\n".format(algorithm))
			for s in ["GLOBAL","USER"]:
				times = list()
				for i in range(EXECUTIONS_ALGORITHM):
					t = time.process_time()
					searchBy(s,algorithm)
					times.append(time.process_time()-t)
				sys.stdout.write("....{} Search Time [ms]:\t{}\n".format(s,sum(times)*1000/len(times)))		

