#!/usr/bin/python
# -*- coding: utf-8 -*-
# Медиана 
# Версия python 2.7

def exit():

	print ('Хотите выйти? Y/n')
	char = raw_input()
	if char in ('y','Y'):
		return True
		
while True:

	print 'Введите элементы массивов через пробел:'
	
	init_array = list(map(float, raw_input().split()))
	
	if len(init_array) % 2 != 0:
		print 'Массивы не равны по количеству элементов.'
		if exit():
			break
		else:
			continue
	
	N = len(init_array) / 2
	
	init_array.sort()
	median = (init_array[N-1] + init_array[N]) / 2
		
	print 'Медиана массива длиной 2N: %r' % median
	
	if exit():
		break
	else:
		continue
