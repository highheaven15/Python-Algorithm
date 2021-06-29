#03. 부분집합 구하기(DFS)

import sys
sys.stdin = open("input.txt", "rt")

def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1 #사용하고 넘어갈때
        DFS(v+1)
        ch[v]=0 #사용안하고 넘어갈때
        DFS(v+1)


if __name__ == "__main__":
    n=int(input())
    ch=[0]*(n+1) #체크변수, 개수는 1개 더 넉넉하게 뒀다
    DFS(1)
