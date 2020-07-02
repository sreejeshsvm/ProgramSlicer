read(n)
i=1
x=0
sum=0
average=0
while i<=n:
	sum=sum+1
	i=i+1
if (sum%n ==0):
	x=-1
else:
	x=sum
print(x)
average=sum/n
print(average)