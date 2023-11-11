import os

def is_file_empty(file_name):
    return os.path.getsize(file_name) == 0


def moreThan_3lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return len(lines) > 3


def append_content(file_name, player_name, player_score):
    with open(file_name, 'a') as file:
        file.write(f"{player_score},{player_name}\n")


def onlyTop_3(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Keep the first 3 lines
    lines = lines[:3]

    with open(file_name, "w") as file:
        file.writelines(lines)


def sort_scores(file_name):
    # Read the existing scores from the file

    array_name = []
    array_score = []
    array_dict = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        sides = line.split(",")
        array_score.append(float(sides[0]))
        array_name.append(sides[1])
        name = sides[1].replace("\n", "")
        array_dict[float(sides[0])] = name

    array_score.sort(reverse=True)
    with open(file_name, 'w') as file:
        file.write("")

    with open(file_name, 'w') as file:
        for scores in array_score:
            names = array_dict.get(scores)
            file.write(f"{scores},{names}\n")


def ranking_updation(file_name, player_name, player_score):
    # Add the last player details to the file
    append_content(file_name, player_name, player_score)


def print_rank(f_pen, file_name):
    array_name = []
    array_score = []
    aux_name = []

    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        sides = line.split(",")
        array_score.append(float(sides[0]))
        array_name.append(sides[1])

    for name in array_name:
        aux_name.append(name.replace("\n", ""))

    f_pen.penup()
    f_pen.goto(-480, 200)
    f_pen.pendown()

    f_pen.write("============ Score Ranking ===========", align="left", font=("Arial", 24, "bold"))
    f_pen.goto(-480, 110)
    f_pen.pendown()
    f_pen.write("Rank 1", align="left", font=("Arial", 14))
    f_pen.goto(-480, 90)
    f_pen.pendown()
    f_pen.write(f"Name: {aux_name[0]} ", align="left", font=("Arial", 14))
    f_pen.goto(-480, 70)
    f_pen.pendown()
    f_pen.write(f"Score: {array_score[0]}", align="left", font=("Arial", 14))

    f_pen.goto(-480, 30)
    f_pen.pendown()
    f_pen.write("Rank 2.", align="left", font=("Arial", 14))
    f_pen.goto(-480, 10)
    f_pen.pendown()
    f_pen.write(f"Name: {aux_name[1]}", align="left", font=("Arial", 14))
    f_pen.goto(-480, -10)
    f_pen.pendown()
    f_pen.write(f"Score: {array_score[1]}", align="left", font=("Arial", 14))

    f_pen.goto(-480, -50)
    f_pen.pendown()
    f_pen.write("Rank 3.", align="left", font=("Arial", 14))
    f_pen.goto(-480, -70)
    f_pen.pendown()
    f_pen.write(f"Name: {aux_name[2]}", align="left", font=("Arial", 14))
    f_pen.goto(-480, -90)
    f_pen.pendown()
    f_pen.write(f"Score: {array_score[2]}", align="left", font=("Arial", 14))



