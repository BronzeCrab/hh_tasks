#!/usr/bin/python
# -*- coding: utf-8 -*-
# Медиана 
# python 2.7

print 'Введите элементы массива через пробел'
init_array = list(map(int, raw_input().split()))

init_array1 = []
init_array2 = []

for i in range (N):
	print 'Введите %d элемент первого массива:' % i
	init_array1.append(float(raw_input()))
for i in range (N):
	print 'Введите %d элемент втрого массива:' % i
	init_array2.append(float(raw_input()))

whole_array=[]

for i in range (N):
	
	whole_array.append(init_array1[i])
	whole_array.append(init_array2[i])

whole_array.sort()
median = (whole_array[N-1]+whole_array[N])/2
	
print 'Медиана массива длиной 2N %r' % median

