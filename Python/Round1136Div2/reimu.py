import sys
input = lambda:sys.stdin.readline().rstrip()
print= sys.stdout.write
def solve(t: tuple)->str:
    return str(max(0,max([ci-i-1 for i,ci in enumerate(sorted([-(-ai // t[1]) for ai in map(int,input().split())])[:-1])])))+"\n"
def main():
    t:int=int(input())
    for _ in range(t):
        print(solve(tuple(map(int,input().split()))))
if __name__=="__main__":
    main()