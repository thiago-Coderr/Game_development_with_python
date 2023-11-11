import random


# functions action_forward & action_backward are used to move the turtle forward and backward respectively: f_pen is
# and instance of Turtle() from turtle module, f_colours is an array of multiple colors and angle is the direction the
# turtle will take to move forward or backward

def action_forward(f_pen, f_colours, angle):
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(angle)
    f_pen.forward(12)


def action_backward(f_pen, f_colours, angle):
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(angle)
    f_pen.backward(12)


# space function gives the space for graphical representation:  f_pen is
# and instance of Turtle() from turtle module

def space(f_pen):
    for _ in range(5):
        f_pen.setheading(0)
        f_pen.forward(12)


# =========== functions for alphabet letters and graphical representation ==========
# They receive and instance of Turtle() from turtle module and array of colours

# =========  A  ==========
# Graphical representation of letter A

def letter_A(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 70)

    for _ in range(6):
        f_pen.setheading(70)
        f_pen.forward(12)

    f_pen.setheading(110)
    f_pen.backward(12)

    for _ in range(5):
        action_backward(f_pen, f_colours, 110)

    for _ in range(3):
        f_pen.setheading(110)
        f_pen.forward(12)

    f_pen.setheading(180)
    f_pen.forward(12)
    f_pen.dot(12, random.choice(f_colours))

    for _ in range(3):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(5):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==========   B  =============
# b_piece represents graphically the number 3 in order to be re-used to for letter B
def b_piece(f_pen, f_colours):
    for _ in range(2):
        action_forward(0)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)

    f_pen.dot(12, random.choice(f_colours))

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.backward(12)

    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(3):
        f_pen.setheading(0)
        action_forward(0)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.backward(12)


# letter_B forms letter B completely
def letter_B(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    # auxiliary function to represent number 3 for B representation
    b_piece(f_pen, f_colours)
    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)

    f_pen.dot(12, random.choice(f_colours))
    for _ in range(3):
        f_pen.setheading(0)
        f_pen.backward(12)

    f_pen.setheading(90)
    f_pen.backward(12)
    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)

    f_pen.dot(12, random.choice(f_colours))
    for _ in range(3):
        f_pen.setheading(0)
        f_pen.backward(12)

    f_pen.setheading(90)
    f_pen.backward(12)
    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)

    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(0)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===========  C  ==============
# graphical representation of letter C

def letter_C(f_pen, f_colours):
    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(4):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(0)
        f_pen.forward(12)


# ============  D  ================
# graphical representation of letter D

def letter_D(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(4):
        action_forward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 180)

    for _ in range(7):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==========  E  ==============
# graphical representation of letter E

def letter_E(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    for _ in range(2):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===========  F  ==============
# Graphical representation of letter F

def letter_F(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(90)
        f_pen.forward(12)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==========  G  ===============
# Graphical representation of letter G

def letter_G(f_pen, f_colours):
    # re-used letter_C to represent letter C and finally create letter G
    letter_C(f_pen, f_colours)
    for _ in range(2):
        f_pen.setheading(90)
        f_pen.backward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.backward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(3):
        action_backward(f_pen, f_colours, 90)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===========  H  =================
# Graphical representation of letter H

def letter_H(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(3):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    for _ in range(3):
        action_forward(f_pen, f_colours, 90)

    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==========  I   ================
# Graphical representation of letter I

def letter_I(f_pen, f_colours):
    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.backward(12)

    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(1):
        action_backward(f_pen, f_colours, 0)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===========   J   ====================
# Graphical representation of letter J

def letter_J(f_pen, f_colours):
    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(1):
        action_backward(f_pen, f_colours, 45)

    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(0)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))

    for _ in range(2):
        action_forward(f_pen, f_colours, 165)

    f_pen.backward(12)
    f_pen.setheading(0)

    for _ in range(2):
        action_forward(f_pen, f_colours, 90)

    for _ in range(3):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(6):
        f_pen.setheading(0)
        f_pen.forward(12)

    f_pen.setheading(90)
    f_pen.forward(12)
    f_pen.setheading(0)


# =============  K   ================
# Graphical representation of letter K


def letter_K(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(4):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(4):
        action_forward(f_pen, f_colours, 45)

    for _ in range(4):
        f_pen.setheading(45)
        f_pen.backward(12)

    for _ in range(5):
        action_backward(f_pen, f_colours, 140)

    for _ in range(5):
        f_pen.setheading(140)
        f_pen.forward(12)

    for _ in range(3):
        f_pen.setheading(45)
        f_pen.forward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.forward(12)


# =================  L  ==================
# Graphical representation of letter L

def letter_L(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===============  M  ================
# Graphical representation of letter M

def letter_M(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        action_backward(f_pen, f_colours, 145)

    f_pen.setheading(145)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 40)

    f_pen.setheading(40)
    f_pen.backward(12)

    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)


# ================  N  ==================
# Graphical representation of letter N

def letter_N(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(7):
        action_backward(f_pen, f_colours, 120)

    f_pen.setheading(120)
    f_pen.forward(12)

    for _ in range(6):
        action_forward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===============  O   ===================
# Graphical representation of letter O

def letter_O(f_pen, f_colours):
    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(4):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(4):
        action_forward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    for _ in range(6):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===========  P  ===============
# Graphical representation of letter P

def letter_P(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 0)

    for _ in range(3):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(5):
        f_pen.setheading(0)
        f_pen.forward(12)


# ================  Q   ==============
# Graphical representation of letter Q

def letter_Q(f_pen, f_colours):
    # letter_O is being re-used to complete letter Q
    letter_O(f_pen, f_colours)
    for _ in range(2):
        f_pen.setheading(0)
        f_pen.backward(12)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.backward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 145)

    for _ in range(3):
        action_backward(f_pen, f_colours, 145)

    for _ in range(2):
        f_pen.setheading(145)
        f_pen.forward(12)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.forward(12)


# =============  R  ==================
# Graphical representation of letter R

def letter_R(f_pen, f_colours):
    # letter_P is being re-used in order to complete letter R
    letter_P(f_pen, f_colours)
    for _ in range(3):
        f_pen.setheading(90)
        f_pen.backward(12)

    for _ in range(5):
        f_pen.setheading(0)
        f_pen.backward(12)

    for _ in range(4):
        action_backward(f_pen, f_colours, 145)

    for _ in range(4):
        action_forward(f_pen, f_colours, 145)

    for _ in range(3):
        action_forward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==============  S  ==================
# Graphical representation of letter S

def letter_S(f_pen, f_colours):
    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.backward(12)

    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.dot(12, random.choice(f_colours))
    f_pen.setheading(90)
    f_pen.backward(12)
    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(3):
        action_backward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)
    f_pen.dot(12, random.choice(f_colours))

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(7):
        f_pen.setheading(0)
        f_pen.forward(12)


# ===============  T  =================
# Graphical representation of letter T

def letter_T(f_pen, f_colours):
    for _ in range(5):
        action_forward(f_pen, f_colours, 0)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.backward(12)

    for _ in range(6):
        action_backward(f_pen, f_colours, 90)

    for _ in range(6):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==============  U  ================
# Graphical representation of letter U

def letter_U(f_pen, f_colours):
    for _ in range(5):
        action_backward(f_pen, f_colours, 90)

    f_pen.setheading(0)
    f_pen.forward(12)

    for _ in range(2):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(90)
    f_pen.forward(12)

    for _ in range(5):
        action_forward(f_pen, f_colours, 90)

    f_pen.setheading(90)
    f_pen.backward(25)

    for _ in range(3):
        f_pen.setheading(0)
        f_pen.forward(12)


# ==========  V  ==============
# Graphical representation of letter V

def letter_V(f_pen, f_colours):
    for _ in range(5):
        action_backward(f_pen, f_colours, 110)

    for _ in range(6):
        action_forward(f_pen, f_colours, 70)

    f_pen.setheading(70)
    f_pen.backward(12)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)


# ============  W  ===============
# Graphical representation of letter W

def letter_W(f_pen, f_colours):
    # letter_V is being re-used in order to represent letter W
    letter_V(f_pen, f_colours)
    for _ in range(2):
        f_pen.setheading(0)
        f_pen.backward(12)
    letter_V(f_pen, f_colours)


# ===============  X  ==================
# Graphical representation of letter X

def letter_X(f_pen, f_colours):
    for _ in range(6):
        action_backward(f_pen, f_colours, 115)

    for _ in range(3):
        f_pen.setheading(115)
        f_pen.forward(12)

    for _ in range(2):
        action_backward(f_pen, f_colours, 60)

    for _ in range(6):
        action_forward(f_pen, f_colours, 60)

    f_pen.setheading(60)
    f_pen.backward(12)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)


# ================ Y ================
# Graphical representation of letter Y

def letter_Y(f_pen, f_colours):
    for _ in range(3):
        action_backward(f_pen, f_colours, 140)

    f_pen.setheading(40)
    f_pen.forward(12)

    for _ in range(3):
        action_forward(f_pen, f_colours, 40)

    for _ in range(4):
        f_pen.setheading(40)
        f_pen.backward(12)

    for _ in range(4):
        action_backward(f_pen, f_colours, 90)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(4):
        f_pen.setheading(0)
        f_pen.forward(12)


# =============  Z   =================
# Graphical representation of letter Z

def letter_Z(f_pen, f_colours):
    for _ in range(4):
        action_forward(f_pen, f_colours, 0)

    f_pen.setheading(0)
    f_pen.backward(12)

    for _ in range(6):
        action_backward(f_pen, f_colours, 60)

    f_pen.setheading(60)
    f_pen.forward(12)

    for _ in range(4):
        action_forward(f_pen, f_colours, 0)

    for _ in range(5):
        f_pen.setheading(90)
        f_pen.forward(12)

    for _ in range(2):
        f_pen.setheading(0)
        f_pen.forward(12)
