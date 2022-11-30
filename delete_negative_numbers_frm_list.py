#delete all negative numbers forom a list of numbers

my_list=[1,2,-3,4,-5]
print("my original list is : ")
res=list(filter(lambda x:x>0,my_list))
print(" The filtered list is : ",res)
