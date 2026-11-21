import sys;
sys.setrecursionlimit(100000)
from functools import cache
import math
input = lambda:sys.stdin.readline().rstrip()
def solve(hp: int) -> int:
    q = (math.isqrt(24 * hp - 23) - 1) // 6
    rem = hp - 3 * q * (q + 1) // 2
    return 3 * q + (rem + q) // (q + 1)

def main():
    t:int=int(input())
    for i in range(t):
        print(solve(int(input())))
if __name__=="__main__":
    main()