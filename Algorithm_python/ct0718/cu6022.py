import sys

date = sys.stdin.readline().strip()

print(date[0:2],'',end='')
print(date[2:4],'',end='')
print(date[4:6],'',end='')

# 좋은답
print(date[0:2],date[2:4],date[4:6],sep=' ')