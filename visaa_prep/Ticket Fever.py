n=int(input())
for i in range(n):
    t,m=map(int,input().split())
    r=t-m
    if r>=0:
        print(r)
    else:
        print(0)
