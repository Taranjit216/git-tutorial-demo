# ouestion return swap value 10,20 to 20,10

'''def swap(x,y):
    x,y=y,x
    return
# print(x,y) , this will give error
x=10
y=20
swap(x,y)
print(x,y)'''

# solution

def swap(x,y):
    x,y=y,x
    return x,y
x=10
y=20
x,y=swap(x,y)
print(x,y)
