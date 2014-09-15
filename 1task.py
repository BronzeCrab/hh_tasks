#!/usr/bin/python
# -*- coding: utf-8 -*-
# Медиана 
# python 2.7

print 'Введите элементы массивов через пробел'

init_array = list(map(float, raw_input().split()))
N = len (init_array) / 2

init_array.sort()
median = (init_array[N-1] + init_array[N]) / 2
	
print 'Медиана массива длиной 2N: %r' % median

