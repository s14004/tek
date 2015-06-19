import time

print(time.asctime())

def hello(name):
    print(name + "さん、こんにちは")

import sys

print('お名前は? ')
name = sys.stdin.readline()
hello(name)