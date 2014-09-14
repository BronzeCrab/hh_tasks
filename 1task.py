hh_1_task
=========

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Медиана, python 2.7

print 'Введите длину иcxодных массивов'
N = int(raw_input())

init_array1 = []
init_array2 = []

for i in range (N):
	print 'Введите %d элемент первого массива:' % i
	init_array1.append(float(raw_input()))
for i in range (N):
	print 'Введите %d элемент втрого массива:' % i
	init_array2.append(float(raw_input()))

init_array=[]

for i in range (N):
	init_array.append(init_array1[i])
for i in range (N):
	init_array.append(init_array2[i])

init_array.sort()
median = (init_array[N-1]+init_array[N])/2
	
print 'Медиана массива длиной 2N %r' % median

