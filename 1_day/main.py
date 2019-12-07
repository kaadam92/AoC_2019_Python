print("AoC 2019 Day 1 - Python")
print('-------------PART I------------')

with open("data.txt","r") as f:
    line = f.readline()
    cnt = 1
    weights = [1]
    while line:
        if cnt == 1:
            weights = [(int)(line)]
        else:
            weights.append((int)(line))
        cnt += 1
        line = f.readline()


res_cnt = 1
weight_length = len(weights)
fuel_req = [0 for x in range(weight_length)]

for w in range(weight_length):
    temp_res = weights[w] // 3 - 2
    fuel_req[w] = temp_res

fuel_for_weights_result = 0

for w in range(weight_length):
    fuel_for_weights_result += fuel_req[w]


print('Result: {}'.format(fuel_for_weights_result))
print('-------------PART II-----------')

ready = 1
fuel_req_for_fuel = [0 for x in range(weight_length)]
commulative_res = fuel_for_weights_result
ready_check = 0

rounds = 0

while ready:

    for w in range(weight_length):
        temp_res = fuel_req[w] // 3 - 2
        if temp_res < 0:
            temp_res = 0
        fuel_req_for_fuel[w] = temp_res

    for x in range(weight_length):
        commulative_res += fuel_req_for_fuel[x]
        ready_check += fuel_req_for_fuel[x]
    if ready_check == 0:
        ready = 0
    ready_check = 0
    fuel_req = fuel_req_for_fuel
    rounds += 1

    print('Round: {}'.format(rounds))

print('Result: {}'.format(commulative_res))




