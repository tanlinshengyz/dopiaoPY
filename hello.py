#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, world,中国文');


s1 = 72
s2 = 85

r =  'Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', (s2-s1)/s1)
print(r)
print((s2-s1)/s1)


import math

def quadratic(a, b, c):
	x = b**2-4*a*c
	if x >= 0:
		return  (-b+math.sqrt(x))/2/a, (-b-math.sqrt(x))/2/a
	else:
		return 

print(quadratic(2,3,1))


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print(move(12,21,10,0))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)


# 杨辉三角

def triangles(r):
	a,b = [1],0
	while b<r:
		# print(a)
		yield(a)
		a.append(0)

		a = [a[i-1]+a[i] for i in range(len(a))];
		b = b+1
for n in triangles(6):
	print(n)



def normalize(name):
   name=name[0].upper()+name[1:].lower()
   return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))

print(L2)


from functools import reduce
def prod(L):
	def f(x,y):
		return x*y;
	return reduce(f,L)

print(prod([1,2,3,6,6]))
print(prod([3,5,7,9]))
		
