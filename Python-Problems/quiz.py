from tkinter import Y

# Quiz 1, result will be (8, 7)
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

# Quiz 2, result will be 77
myList = "7 77 55 2345"
my_sec_list = myList.split()

print(max(my_sec_list))

# Quiz 3, result will be False
x = [1,2,3,4]
y = x.copy()

print(x is y)


# Quiz 4, result will be error
x = int(2.0) + str(2) + float(3)
print(x)