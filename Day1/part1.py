import os

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')

def historian_hysteria():
    left_list = []
    right_list = []
    with open(input_file) as input:
        for line in input:
            nums = line.split()
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1]))
    
    left_list.sort()
    right_list.sort()

    sum = 0
    for i in range(len(left_list)):
        sum += abs(left_list[i] - right_list[i])
    return sum

print(historian_hysteria())
