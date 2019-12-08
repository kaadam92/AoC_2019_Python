import sys

test_vector = [111111, 223450, 123789, 123389, 111122, 112222, 111222]


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

    return possible_count, possible_list


def part_2(possible_list):
    print('-------------PART II-----------')
    part_2_list = possible_list.copy()
    possible_count = 0
    part_2_out = []
    for x in part_2_list:
        if check_number_pt2(x):
            part_2_out.append(x)
            possible_count += 1

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


def check_number_pt2(num):
    input_num_str = (str)(num)
    two_rep_check = 0
    rep_count = 1
    repetitive = 0
    reps = []

    for digit_index in range(0, 5):
        if input_num_str[digit_index] == input_num_str[digit_index + 1]:
            repetitive = 1
            rep_count += 1
        else:
            if repetitive == 0:
                rep_count = 1
            else:
                reps.append(rep_count)
                repetitive = 0
                rep_count = 1
        if digit_index == 4 and repetitive == 1:
            reps.append(rep_count)

    for rep in reps:
        if rep == 2:
            two_rep_check = 1

    if two_rep_check:
        return 1
    else:
        return 0


def only_2_repeat(num1, num2, num3):
    if (num1 == num2 or num2 == num3) and num1 != num3:
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
part_1_possible, part_1_possible_list = part_1(range_num)
print("Solution: {}".format(part_1_possible)) # 579

part_2_possible = part_2(part_1_possible_list)
print("Test: {}".format(part_2(test_vector)))
print("Solution: {}".format(part_2_possible)) # 358