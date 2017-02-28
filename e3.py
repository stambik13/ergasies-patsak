a=eval(raw_input("dose th lista: "))
for i in a:		
 if (a[i]==0):
  a.append(0)
  del a[i]
print a
