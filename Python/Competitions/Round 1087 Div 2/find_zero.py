
def query(i,j):
    print("?",i,j,flush=True)
    inp=int(input())
    if inp==-1:
        exit(0)
    if inp==1:
        return True
    return False
for t in range(int(input())):
    n=int(input())
    for i in range(1,n-1):
        if query(2*i-1,2*i):
            print("!",2*i-1)
            break
    if query(2*n-3,2*n-1):
        print("!",2*n-1)
    if query(2*n-2,2*n-1):
        print("!",2*n-2)
    else:        
        print("!",2*n)
            