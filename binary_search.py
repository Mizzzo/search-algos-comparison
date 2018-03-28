def create_data(n):
    temp = [i for i in range(n)]
    return temp
n = 100
target = n + 11
ma_list = create_data(n)
def binary_search(input_list,target):
    found = False
    low = 0
    high = len(input_list) - 1
    mid = int((high + low) / 2)
    while (low <=high) and (not found):



        curr = input_list[mid]

        if curr == target:
            found = True
            return True
        elif curr < target:
            low = mid +1
        elif curr > target:
            high = mid - 1

        mid = int((high + low) / 2)
        print(mid)
    return False

print(binary_search(ma_list,target))
