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


