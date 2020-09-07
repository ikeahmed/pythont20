spam = ['cat','bat','rat','elephant']
spam[0]
spam[1]

#list within a list
spam=[['cat','bat'],[10,20,30,40,50]]
print(spam[0][0])
print(spam[1][2])
print (spam[0][0][0])

spam = ['cat','bat','rat','elephant']
print(spam[3])
print(spam[-1])

#slice
print(spam[1:3])
print(spam[1:2])
print(spam[1])

def func1(x):
  x[1]='MyValue'
def func2(x):
  x='MyValue'  

print(type(spam[1:2]))
print(type(spam[1]))
print (spam)
func1(spam)
print (spam)
spam2='AValue'
func2(spam2)
print(spam2)
