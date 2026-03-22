t=int(input())
cl=[]
for i in range(t):
    n,c,k=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    for j in range(n):
            if c>a[j]:
                if k>=c-a[j]:
                    k-=(c-a[j])
                    c+=c
                elif k>0:
                    c+=a[j]+k
                    k=0
                else:
                    c+=a[j]
            elif c==a[j]:
                c+=c 
    cl.append(c)
for c in cl:
    print(c)