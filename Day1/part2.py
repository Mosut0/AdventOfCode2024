import os

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')

def historian_hysteria():
    left_list = {}
    right_list = []
    with open(input_file) as input:
        for line in input:
            nums = line.split()
            left_list.setdefault(int(nums[0]), 0)
            right_list.append(int(nums[1]))
    
    for num in right_list:
        if num in left_list:
            left_list[num] += 1

    sum = 0
    for k, v in left_list.items():
        sum += k * v

    return sum

print(historian_hysteria())
