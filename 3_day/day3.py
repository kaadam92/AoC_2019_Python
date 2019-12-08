import sys
import turtle

inputfile = "data.txt"

scaling_factor = 0.035

wire1_drawn = 0
wire2_drawn = 0


def get_wires(filename):
    with open(filename) as file:
        return list(file.readline().rstrip().split(',')), list(file.readline().rstrip().split(','))


def paint_path(area_dict, delay_dict, wire_data, id, with_delay, wire_drawn):
    min_dist = sys.maxsize
    x, y = 0, 0
    step = 0
    for i in range(len(wire_data)):
        next_element = wire_data[i]
        direction, steps = next_element[0:1], int(next_element[1:])
        for j in range(steps):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            else:
                y -= 1

            if id == 1 and wire_drawn == 0:
                if direction == 'R':
                    wire_graph1.goto(wire_graph1.xcor() + scaling_factor, wire_graph1.ycor())
                elif direction == 'L':
                    wire_graph1.goto(wire_graph1.xcor() - scaling_factor, wire_graph1.ycor())
                elif direction == 'U':
                    wire_graph1.goto(wire_graph1.xcor(), wire_graph1.ycor() + scaling_factor)
                else:
                    wire_graph1.goto(wire_graph1.xcor(), wire_graph1.ycor() - scaling_factor)

            if id == 2 and wire_drawn == 0:
                if direction == 'R':
                    wire_graph2.goto(wire_graph2.xcor() + scaling_factor, wire_graph2.ycor())
                elif direction == 'L':
                    wire_graph2.goto(wire_graph2.xcor() - scaling_factor, wire_graph2.ycor())
                elif direction == 'U':
                    wire_graph2.goto(wire_graph2.xcor(), wire_graph2.ycor() + scaling_factor)
                else:
                    wire_graph2.goto(wire_graph2.xcor(), wire_graph2.ycor() - scaling_factor)
            step += 1
            key = "{} {}".format(x, y)
            if area_dict.get(key) is None or area_dict.get(key) == id:
                area_dict[key] = id
                delay_dict[key] = step
            else:
                min_dist = min(min_dist, delay_dict.get(key) + step if with_delay else abs(x) + abs(y))
    return min_dist


def part_one():
    print('-------------PART I------------')
    wire1, wire2 = get_wires(inputfile)
    area_dict = {}
    delay_dict = {}
    paint_path(area_dict, delay_dict, wire1, 1, False, wire1_drawn)
    return paint_path(area_dict, delay_dict, wire2, 2, False, wire2_drawn)


def part_two():
    print('-------------PART II-----------')
    wire1, wire2 = get_wires(inputfile)
    area_dict = {}
    delay_dict = {}
    paint_path(area_dict, delay_dict, wire1, 1, True, wire1_drawn)
    return paint_path(area_dict, delay_dict, wire2, 2, True, wire2_drawn)

# Main program
print("AoC 2019 Day 2 - Python")

wn = turtle.Screen()
wn.title("Day 3 Visualisation")
wn.bgcolor("black")
wn.setup(width = 1000, height =1000)
wn.tracer(0)

# Wire1
wire_graph1 = turtle.Turtle()
wire_graph1.speed(0)
wire_graph1.color("white")
#wire_graph1.penup()

# Wire1
wire_graph2 = turtle.Turtle()
wire_graph2.speed(0)
wire_graph2.color("blue")
#wire_graph1.penup()


print("Solution: {}".format(part_one()))
wire1_drawn = 1
wire2_drawn = 1
print("Solution: {}".format(part_two()))

while True:
    wn.update()