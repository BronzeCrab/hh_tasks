#!/usr/bin/python
# -*- coding: utf-8 -*-
# Задача про весы
# Методом полного перебора
# Python 2.7

from __future__ import print_function

init_array,b = [],[]
pan1,pan2 = [],[]

def check():

	q = False
	for i in range (n):
		if b[i] == 0:
			q = True
	return q 

def add_1():

	i = 0
	while (b[i] == 1) and (i < n-1):
		i += 1
	b[i] = 1
	for k in range (i):
		b[k] = 0

def partition():

	for k in range (n):

		if balance:
			pass

		elif b[k] == 1:
			pan1.append(init_array[k])
			
		else:
			pan2.append(init_array[k])

def exit():

	char = ''
	print ('Хотите выйти? Y/n')
	char = raw_input()
	if char in ('y','Y'):
		return True
		
while True:

	print ('Введите исходный массив(все элементы через пробел)')
	init_array = list(map(int, raw_input().split()))
	n = len (init_array)
	 
	for i in range (n):
		b.append(0)
		
	balance = False
	existence_of_100 = False
	
	while check():
	
		add_1()
		
		s1 = 0
		s2 = 0
		
		for i in range (n):
	
			if b[i] == 0:
				s1 += init_array[i]
			else:
				s2 += init_array[i]
	
			if (s1 == 100) or (s2 == 100):
				existence_of_100 = True				
		
		if abs(s1 - s2) == 0 :
			partition()	
			balance = True
	
	if balance == True:
		
		for i in range (len(pan1)):
			print (pan1[i],end=' ')
		print ('- ',end='')
	
		for i in range (len(pan2)):
			print (pan2[i],end=' ')
		print ('\n')
	
		if existence_of_100:
			print ('yes')
		else:
			print ('no')		
	else:
		print ('Уравновесить весы невозможно')
		if existence_of_100:
			print ('yes')
		else:
			
if exit():
		break
	else:
		continue
