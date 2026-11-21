import sys;
input = lambda:sys.stdin.readline().rstrip()
def solve(t):
    x,y,m=t
    s=input()
    stones=[x+y]
    for i in range(m):
        if(x+y>0):
            if(s[i]=="+"):
                if(y>0):
                    y+=1
                else:
                    y+=1
                    x-=1
            elif(s[i]=="-"):
                if(y>1 or x==0):
                    y-=1
                    x+=1
                else:
                    x-=1
            stones.append(x+y)
        else:
            break
    return max(stones)
def main():
    t:int=int(input())
    for i in range(t):
        print(solve(tuple(map(int,input().split()))))
if __name__=="__main__":
    main()
    