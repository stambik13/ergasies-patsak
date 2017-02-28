a=eval(raw_input("dose th lista me toulaxiston 5 stoixeia: "))
a.sort()
mo=sum(a)/len(a)
length=len(a)-2
s=0
for i in range(1,length):
	ap=0
	ap=a[i]-mo
	t_r=0
	t_r=ap*ap
	s=s+t_r
if (len(a)>=5):
    diak=s/(len(a)-4)
    import math
    t_a=math.sqrt(diak)
    print t_a
else: 
    print "edoses list me ligotera apo 5 stoixeia"
