Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print('test')
test
>>> print(type(10))
<class 'int'>
>>> print(type('hallo'))
<class 'str'>
>>> print(type(type))
<class 'type'>
>>> print(type(false))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> print(type(False))
<class 'bool'>
>>> n = 100
>>> print(n)
100
>>> a = b = c = 300
>>> print(a,b,c)
300 300 300
>>> a = 100
>>> b =100
>>> a+b
200
>>> print(100%2)
0
>>> print(100%3)
1
>>> print(100%8)
4
>>> print(2**2)
4
>>> var = 'A'
>>> var * 3
'AAA'
>>> s = 'foo'
>>> print(s in 'hello world')
False
>>> s = 'foo'
>>> a = ['a','b','c']
>>> len(a)
3
>>> print(a)
['a', 'b', 'c']