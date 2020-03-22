l=list(map(int,input().split()))
l1=[]
for i in l:
    if i in l1:
        print("YES")
    else:
         l1.append(i)
         print("NO")