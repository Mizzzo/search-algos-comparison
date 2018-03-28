def create_data(n):
    temp = (i for i in range(n))
    return temp
n = 100000
target = n + 1
ma_list = create_data(n)
def linear_search(input_list,target):

    for element in input_list:
        if element == target:
            return True
    return False
print(linear_search(ma_list,target))
