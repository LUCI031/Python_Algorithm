#백준 2941 크로아티아 알파벳
import sys
input=sys.stdin.readline

word = input().rstrip()

croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croa:
    word = word.replace(i, '*')
print(len(word))