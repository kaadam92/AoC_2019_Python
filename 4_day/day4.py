import sys

test_vector = [111111, 223450, 123789, 123389, 111122, 112222]


def test_num_checker(test_data):
    for i in test_data:
        check_number_pt2(i)
    return 0


def part_1(range_num):
    print('-------------PART I------------')
    possible_count = 0
    possible_list = []
    for x in range(range_num[0], range_num[1]):
        if check_number_pt1(x):
            possible_count += 1
            possible_list.append(x)

    return possible_count


def part_2():
    print('-------------PART II-----------')
    possible_count = 0
    possible_list = []
    for x in range(range_num[0], range_num[1]):
        if check_number_pt2(x):
            possible_count += 1
            possible_list.append(x)

    return possible_count


def check_number_pt1(num):
    input_num_str = (str)(num)
    adjesent_same = 0
    adjesent_not_desc = 1

    for digit_index in range(len(input_num_str)-1):
        if input_num_str[digit_index] == input_num_str[digit_index + 1]:
            adjesent_same = 1
        if input_num_str[digit_index] > input_num_str[digit_index + 1]:
            adjesent_not_desc = 0

    if adjesent_same and adjesent_not_desc:
        return 1
    else:
        return 0


def only_2_repeat(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return 0
    else:
        return 1


def check_number_pt2(num):
    input_num_str = (str)(num)
    adjesent_same = 0
    adjesent_not_desc = 1
    only_2_repeat_check = 0

    for digit_index in range(len(input_num_str)-1):
        if input_num_str[digit_index] == input_num_str[digit_index + 1]:
            adjesent_same = 1
            if (digit_index > 0) and only_2_repeat_check == 0:
                only_2_repeat_check = only_2_repeat((input_num_str[digit_index-1]), (input_num_str[digit_index]), (input_num_str[digit_index+1]))

        if input_num_str[digit_index] > input_num_str[digit_index + 1]:
            adjesent_not_desc = 0

    if adjesent_same and adjesent_not_desc and only_2_repeat_check:
        return 1
    else:
        return 0


def get_data(filename, separator):
    with open(filename) as file:
        input_str_list = list(file.readline().split(separator))
        input_num_list = []
        for x in input_str_list:
            input_num_list.append((int)(x))
        return input_num_list


# Main Starts here

print("AoC 2019 Day 2 - Python")
range_num = get_data("data.txt", "-")
print("Test: {}".format(test_num_checker(test_vector)))
print("Solution: {}".format(part_1(range_num))) # 579
print("Test: {}".format(test_num_checker(test_vector)))
print("Solution: {}".format(part_2()))