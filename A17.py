a = [1,2,3,4,5]  #create a list
b = [1,2,3,4,5]  #create another list
c = a            #c points to same list as a
print(a is c)    #true
print(a is b)    #false
print(a is not c)#false
print(a is not b)#true