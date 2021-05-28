#Write a program that prints the sum of the first ten positive integers, 1 + 2 + ... + 10

r= int(input("How many integers:"))
sum= 0

#operation
u= range(1,r+1)
for e in u:
    sum=sum+e

print("The sum:",sum)
#
yp= 1000
p= 0.05
y= 3

#operation
o= p*y
tot= (yp*o)+yp

print("Total:",tot)
