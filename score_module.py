import os


def is_file_empty(file_name):
    return os.path.getsize(file_name) == 0


def moreThan_3lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return len(lines) > 3


def sort_scores(file_name):
    # Read the existing scores from the file

    array_name = []
    array_score = []
    array_dict = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            sides = line.split(",")
            array_score.append(int(sides[0]))
            array_name.append(sides[1])
            name = sides[1].replace("\n", "")
            array_dict[int(sides[0])] = name

    array_score.sort(reverse=True)
    with open(file_name, 'w') as file:
        file.write("")
        for scores in array_score:
            names = array_dict.get(scores)
            file.write(f"{scores},{names}\n")








