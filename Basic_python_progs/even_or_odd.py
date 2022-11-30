return odd_number
     retrun even_number # Wont be reached


number_list = [1, 2, 3, 4, 5, 6]

def calculate_odd_even():
    odd_number = 0
    even_number = 0
    for i in number_list:
        if i % 2 == 0:
            even_number = even_number + i
        else:
            odd_number = odd_number + i
    
    return (odd_number, even_number)

my_tuple = calculate_odd_even()
print(my_tuple) # prints (9, 12)
