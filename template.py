def part_1():
	print('-------------PART I------------')
	pass

def part_2():
	print('-------------PART II-----------')
	pass

def get_data(filename,separator):
	with open(filename) as file:
		return file.readline().rstirp().split(separator)


# Main Starts here

print("AoC 2019 Day 2 - Python")
print("Solution: {}".format(part_1()))
print("Solution: {}".format(part_2()))