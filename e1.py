s=raw_input("dose protash me polla !!!  ")
list1=list(s)
m=len(list1)
i=m
while i>=0:
	i=i-1
	if (list1[i]==("!")):
		pos=i-1
	else: break	
for i in range(0,pos):
	if (list1[i]==("!")):
		list1[i]=list1[i].replace("!"," ")
s=''.join(list1)
print s
