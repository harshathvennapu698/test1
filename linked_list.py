n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
s1=''
s2=''
for i in l1:
    s1=str(i)+s1
for j in l2:
    s2=str(j)+s2
l=[]
for k in str(int(s1)+int(s2)):
    l.append(int(k))
for i in l[::-1]:
    print(i,end=' ')