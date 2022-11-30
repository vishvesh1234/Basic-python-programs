#to print the number of odd numbers, even numbers and zeros

l=[1,2,4,0,-7,-8,0,3,-5,6]
pos_count,neg_count,zero_count=0,0,0

for i in l:
    if i>0:
        pos_count +=1
    elif i==0:
        zero_count +=1
    else :
        neg_count +=1

print(" the count of positive numbers is :",pos_count)
print(" the count of zero's is :",zero_count)
print(" the count of negative numbers is :",neg_count)
