#! /usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
    str="function"
    print(str);

def foo1(num):
    print('num' ,num);

def foo2(name ,history):
    print('python' ,name);
    print('history' ,history);

if __name__=="__main__":
    print("main")
    foo2('hello' ,'python')
    foo1(6)
    foo()