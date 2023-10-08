import turtle
import pandas
import random
import letters_module  # customized module for graphical representation of alphabet letters

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
window = turtle.Screen()
window.setup(width=1000, height=600)
window.title("Guessing States")

new_name = ""

# Gif images declaration
image_1 = "usa.gif"
image_2 = "france.gif"
image_3 = "angola_1.gif"
image_4 = "chad.gif"
image_5 = "india.gif"

# CSV file's names declaration for images coordinates and dots representation coordinates
usa_coordinates_file = "usa_coordinates.csv"
usa_dot_coordinates_file = "usa_dots_coordinates.csv"
france_coordinates_file = "france_coordinates.csv"
france_dot_coordinates_file = "france_dots_coordinates.csv"
angola_coordinates_file = "angola_coordinates.csv"
angola_dot_coordinates_file = "angola_dots_coordinates.csv"
chad_coordinates_file = "chad_coordinates.csv"
chad_dot_coordinates_file = "chad_dots_coordinates.csv"
india_coordinates_file = "india_coordinates.csv"
india_dot_coordinates_file = "india_dots_coordinates.csv"

# Array of multiple colours for dot representation
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# ================================  My all functions =========================


# ===========  Writing graphically payer's name  ================
def print_name_graphically(player_name):
    for letter in player_name:
        if letter == 'A' or letter == 'a':
            letters_module.letter_A(pen, colours)
        elif letter == 'B' or letter == 'a':
            letters_module.letter_B(pen, colours)
        elif letter == 'C' or letter == 'c':
            letters_module.letter_C(pen, colours)
        elif letter == 'D' or letter == 'd':
            letters_module.letter_D(pen, colours)
        elif letter == 'E' or letter == 'e':
            letters_module.letter_E(pen, colours)
        elif letter == 'F' or letter == 'f':
            letters_module.letter_F(pen, colours)
        elif letter == 'G' or letter == 'g':
            letters_module.letter_G(pen, colours)
        elif letter == 'H' or letter == 'h':
            letters_module.letter_H(pen, colours)
        elif letter == 'I' or letter == 'i':
            letters_module.letter_I(pen, colours)
        elif letter == 'J' or letter == 'j':
            letters_module.letter_J(pen, colours)
        elif letter == 'K' or letter == 'k':
            letters_module.letter_K(pen, colours)
        elif letter == 'L' or letter == 'l':
            letters_module.letter_L(pen, colours)
        elif letter == 'M' or letter == 'm':
            letters_module.letter_M(pen, colours)
        elif letter == 'N' or letter == 'n':
            letters_module.letter_N(pen, colours)
        elif letter == 'O' or letter == 'o':
            letters_module.letter_O(pen, colours)
        elif letter == 'P' or letter == 'p':
            letters_module.letter_P(pen, colours)
        elif letter == 'Q' or letter == 'q':
            letters_module.letter_Q(pen, colours)
        elif letter == 'R' or letter == 'r':
            letters_module.letter_R(pen, colours)
        elif letter == 'S' or letter == 's':
            letters_module.letter_S(pen, colours)
        elif letter == 'T' or letter == 't':
            letters_module.letter_T(pen, colours)
        elif letter == 'U' or letter == 'u':
            letters_module.letter_U(pen, colours)
        elif letter == 'V' or letter == 'v':
            letters_module.letter_V(pen, colours)
        elif letter == 'W' or letter == 'w':
            letters_module.letter_W(pen, colours)
        elif letter == 'X' or letter == 'x':
            letters_module.letter_X(pen, colours)
        elif letter == 'Y' or letter == 'y':
            letters_module.letter_Y(pen, colours)
        elif letter == 'Z' or letter == 'z':
            letters_module.letter_Z(pen, colours)
        elif letter == ' ':
            letters_module.space(pen)


# player_score gives the score out of 100% after the player attempted every guess: state_guessed is the number of
# correct guessed states and out_of is the chosen number of guessing attempts.
def player_scores(state_guessed, out_of):
    score = (len(state_guessed) / out_of) * 100
    last_score = float("{:.2f}".format(score))
    window.clear()
    pen.penup()
    pen.goto(-110.0, 249.0)

    if 0 <= last_score < 40:
        print("Very bad")
        pen.pendown()
        pen.write(f"{last_score} %...Very bad result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)

        # calling the function print_name_graphically to print the player name graphically
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_W(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.space(pen)
        letters_module.letter_A(pen, colours)
        letters_module.letter_R(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.space(pen)
        letters_module.letter_S(pen, colours)
        letters_module.letter_O(pen, colours)
        letters_module.letter_R(pen, colours)
        letters_module.letter_R(pen, colours)
        letters_module.letter_Y(pen, colours)
    elif 40 <= last_score < 50:
        pen.pendown()
        pen.write(f"{last_score} %...Bad result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_U(pen, colours)
        letters_module.letter_H(pen, colours)
        letters_module.letter_H(pen, colours)
        letters_module.space(pen)
        letters_module.letter_G(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_T(pen, colours)
        letters_module.space(pen)
        letters_module.letter_B(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_T(pen, colours)
        letters_module.letter_T(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_R(pen, colours)

    elif 50 <= last_score < 60:
        print("Good result")
        pen.pendown()
        pen.write(f"{last_score} %...Good result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_W(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_L(pen, colours)
        letters_module.letter_L(pen, colours)
        letters_module.space(pen)
        letters_module.letter_D(pen, colours)
        letters_module.letter_O(pen, colours)
        letters_module.letter_N(pen, colours)
        letters_module.letter_E(pen, colours)
    elif 60 <= last_score < 80:
        print("Very good result")
        pen.pendown()
        pen.write(f"{last_score} %...Very good result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_C(pen, colours)
        letters_module.letter_O(pen, colours)
        letters_module.letter_N(pen, colours)
        letters_module.letter_G(pen, colours)
        letters_module.letter_R(pen, colours)
        letters_module.letter_A(pen, colours)
        letters_module.letter_T(pen, colours)
        letters_module.letter_U(pen, colours)
        letters_module.letter_L(pen, colours)
        letters_module.letter_A(pen, colours)
        letters_module.letter_T(pen, colours)
        letters_module.letter_I(pen, colours)
        letters_module.letter_O(pen, colours)
        letters_module.letter_N(pen, colours)
        letters_module.letter_S(pen, colours)
    elif 80 <= last_score < 90:
        print("Excellent result")
        pen.pendown()
        pen.write(f"{last_score} %...Excellent result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_M(pen, colours)
        letters_module.letter_A(pen, colours)
        letters_module.letter_G(pen, colours)
        letters_module.letter_N(pen, colours)
        letters_module.letter_I(pen, colours)
        letters_module.letter_F(pen, colours)
        letters_module.letter_I(pen, colours)
        letters_module.letter_C(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_N(pen, colours)
        letters_module.letter_T(pen, colours)
    elif 90 <= last_score < 101:
        print("Outstanding result")
        pen.pendown()
        pen.write(f"{last_score} %...Outstanding result", align="left", font=("Arial", 24, "bold"))
        pen.penup()
        pen.goto(-430.0, 214.0)
        print_name_graphically(new_name)
        pen.goto(-411.0, 98.0)
        letters_module.letter_T(pen, colours)
        letters_module.letter_O(pen, colours)
        letters_module.letter_P(pen, colours)
        letters_module.letter_P(pen, colours)
        letters_module.letter_E(pen, colours)
        letters_module.letter_R(pen, colours)
        letters_module.space(pen)
        letters_module.letter_G(pen, colours)
        letters_module.letter_U(pen, colours)
        letters_module.letter_Y(pen, colours)

    pen.goto(-400, -30)
    pen.pendown()
    pen.write("Play again", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, -80)
    pen.pendown()
    pen.write("<= Back to menu", font=("Arial", 16, "normal"))
    pen.penup()

    def after_game_coordinates(x, y):
        if -400 <= x <= -200 and -30 <= y <= 20:
            window.clear()
            select_country_menu()
        elif -400 <= x <= -200 and -80 <= y <= -30:
            window.clear()
            main_menu()

    window.onscreenclick(after_game_coordinates)


def is_empty_string(variable):
    if len(variable) == 0:
        return True
    else:
        return False


def is_convertible_to_int(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def play_selected_country(guessing_times, country_coordinates, dots_coordinates, colours_dot):
    def put_dot():
        pen.dot(12, random.choice(colours_dot))

    data_1 = pandas.read_csv(country_coordinates)
    data_2 = pandas.read_csv(dots_coordinates)

    doted_states = data_2.state.to_list()

    all_doted = []
    guessed_states = []

    random_doted_state = random.choice(doted_states)

    play_round = 1
    while play_round < guessing_times + 1:

        guess_this_state = data_2[data_2.state == random_doted_state]
        pen.goto(int(guess_this_state.x), int(guess_this_state.y))
        all_doted.append(random_doted_state)
        put_dot()
        pen.penup()

        answer_state = (
            window.textinput(title=f"{play_round - 1}/{guessing_times}", prompt="Guess the dotted state")).title()
        if answer_state != "":
            play_round = play_round + 1
            if answer_state == random_doted_state:
                guessed_states.append(random_doted_state)
                data_state = data_1[data_1.state == answer_state]
                print(random_doted_state)
                pen.goto(int(data_state.x), int(data_state.y))
                pen.write(random_doted_state)

                while random_doted_state in all_doted:
                    random_doted_state = random.choice(doted_states)

            else:
                data_state = data_1[data_1.state == random_doted_state]
                pen.goto(int(data_state.x), int(data_state.y))
                pen.write("xxxx")
                pen.penup()

                while random_doted_state in all_doted:
                    random_doted_state = random.choice(doted_states)

        else:
            print("Invalid input")

    def coordinates_country(x, y):
        print(x, y)

    window.onscreenclick(coordinates_country)

    player_scores(guessed_states, guessing_times)


# Define a function to draw the menu options
def main_menu():
    # Move the Turtle pen to the top left corner of the screen
    pen.penup()
    pen.goto(-400, 200)
    pen.pendown()

    # Draw the menu options
    pen.write("GUESSING COUNTRIES STATES", align="left", font=("Arial", 24, "bold"))
    pen.penup()
    pen.goto(-400, 100)
    pen.pendown()
    pen.write("Select Country", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    pen.write("About the Game", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, -100)
    pen.pendown()
    pen.write("Exit", font=("Arial", 16, "normal"))

    def main_menu_coordinates(x, y):
        # Check if the user clicked on Option 1
        if -400 <= x <= -100 and 80 <= y <= 120:
            window.clear()
            select_country_menu()
            print("Select country")
        # Check if the user clicked on Option 2
        elif -400 <= x <= -100 and -20 <= y <= 20:
            window.clear()
            about_game_menu()
            print("about the game")
        # Check if the user clicked on Option 3
        elif -400 <= x <= -100 and -120 <= y <= -80:
            turtle.bye()
            print("Option 3 selected")

    window.onscreenclick(main_menu_coordinates)


def select_country_menu():
    # Move the Turtle pen to the top left corner of the screen
    pen.penup()
    pen.goto(-400, 220)
    pen.pendown()

    # Draw the menu options
    pen.write("============ SELECT THE COUNTRY ============", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, 170)
    pen.pendown()
    pen.write("United State Of America", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, 120)
    pen.pendown()
    pen.write("France", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, 70)
    pen.pendown()
    pen.write("Angola", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, 20)
    pen.pendown()
    pen.write("Chad", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, -30)
    pen.pendown()
    pen.write("India", font=("Arial", 16, "normal"))
    pen.penup()
    pen.goto(-400, -80)
    pen.pendown()
    pen.write("<= Back to main menu", font=("Arial", 16, "normal"))

    def select_country_coordinates(x, y):
        global new_name
        global usa_coordinates_file
        global colours

        # option 1 USA
        if -400 <= x <= -200 and 170 <= y <= 220:
            new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()
            while is_empty_string(new_name):
                new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()

            print(new_name)
            window.clear()
            window.addshape(image_1)
            turtle.shape(image_1)
            guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                            "out of 50")
            while not is_convertible_to_int(guess_number):
                guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                                "out of 50")
            play_selected_country(int(guess_number), usa_coordinates_file, usa_dot_coordinates_file, colours)

        # Option 2 France
        elif -400 <= x <= -200 and 120 <= y <= 170:

            new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()
            while is_empty_string(new_name):
                new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()

            print(new_name)
            window.clear()
            window.addshape(image_2)
            turtle.shape(image_2)
            guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                            "out of 13")
            while not is_convertible_to_int(guess_number):
                guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                                "out of 13")

            play_selected_country(int(guess_number), france_coordinates_file, france_dot_coordinates_file, colours)

        # Option 3 Angola
        elif -400 <= x <= -200 and 70 <= y <= 120:

            new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()
            while is_empty_string(new_name):
                new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()

            print(new_name)
            window.clear()
            window.addshape(image_3)
            turtle.shape(image_3)
            guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                            "out of 18")
            while not is_convertible_to_int(guess_number):
                guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                                "out of 18")

            play_selected_country(int(guess_number), angola_coordinates_file, angola_dot_coordinates_file, colours)

            # Option 4 Chad

        elif -200 >= x >= -400 and 20 <= y <= 70:

            new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()
            while is_empty_string(new_name):
                new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()

            print(new_name)
            window.clear()
            window.addshape(image_4)
            turtle.shape(image_4)
            guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                            "out of 17")
            while not is_convertible_to_int(guess_number):
                guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                                "out of 17")

            play_selected_country(int(guess_number), chad_coordinates_file, chad_dot_coordinates_file, colours)

            # Option 5 India
        elif -400 <= x <= -200 and -30 <= y <= 20:

            new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()
            while is_empty_string(new_name):
                new_name = (window.textinput(title="Player Name", prompt="Enter your name")).title()

            print(new_name)
            window.clear()
            window.addshape(image_5)
            turtle.shape(image_5)
            guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                            "out of 26")
            while not is_convertible_to_int(guess_number):
                guess_number = window.textinput(title="Guessing number", prompt="How many state you want to guess "
                                                                                "out of 26")

            play_selected_country(int(guess_number), india_coordinates_file, india_dot_coordinates_file, colours)

        # Option 6 Go back
        elif -400 <= x <= -200 and -80 <= y <= -30:
            window.clear()
            main_menu()
            print("Go back")

    window.onscreenclick(select_country_coordinates)


def about_game_menu():
    pen.penup()
    pen.goto(-480, 200)
    pen.pendown()
    pen.write("Guessing Countries States - An Open World Game Version 1.0", align="left", font=("Arial", 24, "bold"))

    # Write the game description
    pen.goto(-480, 150)
    pen.pendown()
    pen.write(
        "Guessing Countries States is a game developed and published by Tiago Ntalani. In the game,",
        align="left", font=("Arial", 14))
    pen.goto(-480, 130)
    pen.pendown()
    pen.write("players select either USA or France to guess the states given by the system, inputting the correct name "
              "of the state.",
              align="left", font=("Arial", 14))
    pen.goto(-480, 110)
    pen.pendown()
    pen.write(
        "If the inputted state name is correct, then it will display the name of the state on state spot and the "
        "system will assign ",
        align="left", font=("Arial", 14))
    pen.goto(-480, 90)
    pen.pendown()
    pen.write("the player 3 points for every correct answer, if the answer is uncorrect the system will "
              "display xxxx on incorrect state ",
              align="left", font=("Arial", 14))
    pen.goto(-480, 70)
    pen.pendown()
    pen.write(
        "spot, and no point will be assigned to the player. The player also defines out of how many "
        "states he/she is willing to",
        align="left", font=("Arial", 14))
    pen.goto(-480, 50)
    pen.pendown()
    pen.write(
        "guess instead of all country states.",
        align="left", font=("Arial", 14))
    pen.goto(-480, 30)
    pen.pendown()
    pen.write(
        "The game was developed in order to help elementary students in Geography subject by guessing countries states ",
        align="left", font=("Arial", 14))
    pen.goto(-480, 10)
    pen.pendown()
    pen.write("and recognize states map. Will make them recognize the states by its map shape and the country "
              "in question...", align="left", font=("Arial", 14))

    pen.goto(-400, -100)
    pen.pendown()
    pen.write("<= Go back", font=("Arial", 16, "normal"))

    def about_game_menu_coordinates(x, y):
        if -400 <= x <= -100 and -120 <= y <= -80:
            window.clear()
            main_menu()
            print("Option 3 selected")

    window.onscreenclick(about_game_menu_coordinates)


main_menu()

window.mainloop()
