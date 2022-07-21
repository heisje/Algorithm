'''
counter = int(input())

li = dict()
for a in range(counter):
    name, value= input().split()
    if li.get(name) != False: 
        li[name] = value
    else:
        li += {name: value}

ans = []
for key, value in li.items():
    if value == 'enter':
        ans.append(key)
print('\n'.join(sorted(ans, reverse=True)))
'''
import sys
input = sys.stdin.readline

counter = int(input().rstrip())

li = dict()
for a in range(counter):
    name, value= input().rstrip().split()
    li[name] = value

ans = []
for key, value in li.items():
    if value == 'enter':
        ans.append(key)
print('\n'.join(sorted(ans, reverse=True)))