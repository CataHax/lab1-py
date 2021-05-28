be= 956 #begining ending
wd= 5 #number of work days

o= wd*(2 * hw)
u= be - o


# print Work, print Personal use
print("Work:",o,"mi")
print("Personal use:",u,"mi")
#
#inputs
t= 0.15
n= int(input("Number of friends, including you:"))
ba= float(input("Bill:"))

#operation
tb= (ba*t)+ba
bp= tb/n
t= ba*t
bp= round(bp,2)



#print: Bill, Tip, Both for each person that has to pay
print("Total bill:",tb)
print("Bill alone:",ba)
print("Tip:",t)
print("Bill for each person:",bp)
