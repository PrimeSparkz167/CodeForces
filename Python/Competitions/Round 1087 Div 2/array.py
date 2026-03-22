
ls=[]
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sa=sorted(a)
    ass=sa[::-1]
    l=[]
    for i in range(n):
        p=sa.index(a[i])
        lp=ass.index(a[i])
        l.append(max(p,lp))
        sa.pop(p)
        ass.pop(lp)
    ls.append(l)
for l in ls:
    print((" ").join(map(str,l)))