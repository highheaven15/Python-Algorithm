
5. 반복문을 이용한 문제 풀이

1. 1부터 N까지 홀수출력하기
2. 1부터 N까지의 합을 구하기
3. N의 약수출력하기

for문
while문 : 조건식이 참인동안 문장을 반복 실행


1. 1부터 N까지 홀수출력하기

n=int(input())
for i in range(1, n+1):
    if i%2==1: 
        print(i)


2. 1부터 N까지의 합을 구하기

n=int(input())
sum=0
for i in range(1,n+1):
    sum =sum+ i
print(sum)



3. N의 약수출력하기

n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end=" ") #end는 줄 바꾸지않는다
