words = set()
for _ in range(int(input())):
    words.update(input().split())
print(words)


OR

n=int(input())
s=""
for i in range(n):
	s2=input()
	s=s+" "+s2
l=s.split()
s4=set(l)
print(len(s4))