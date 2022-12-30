# Don't do this
a = 20
b = 10

if (a > b): 
    print ("Greatest is ", a)
else:
    print ("Greatest is ", b)
# Greatest is 20

# Instead of this
a = 20
b = 10
res = a if (a > b) else b
print("Greatest is ", res)
# Greatest value is 20