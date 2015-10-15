l1=[3,1,2,9,7]
print len(l1)

l2=[]
for i in l1:
	l2.append(i**2)

l2.sort()
print l2
print "removing 9 from list"
l2.remove(9)
print l2
