#calculate line slope

x1=int(input("enter a value:"))
x2=int(input("enter a value:"))
y1=int(input("enter a value:"))
y2=int(input("enter a value:"))

slope = (y2-y1)/(x2-x1)

if slope=='positive':
    print("positive slope")
elif slope=='negetive':
    print("negative slope")
elif slope==0:
    print("horizontal line")
else:
    print("vertical line")
