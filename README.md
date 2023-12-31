# Game_development_with_python
1) - Game Concept: The game allows players to select a specific country (e.g., USA, France, Angola, Chad, India) and 
then guess the names of its states. Players are presented with a map of the selected country, and they have to input 
the correct state names based on the location of dots on the map given by the system.

2) - Educational Purpose: The primary goal of the game is for educational purpose. It aims to help elementary students
learn about the geography of various countries, particularly their states or regions. By recognizing states on a map,
players can improve their knowledge of geography.

3) - Player Interaction: The game includes features such as player name input, the option to choose the number of
states to guess, and a scoring system based on correct guesses. The game provides feedback on the player's performance
and displays their name graphically on the screen.

4) - Menu System: The project includes a menu system with options for selecting a country to play, learning about the
game, and exiting the game. This menu system makes it user-friendly and easy to navigate.

5) - Graphics: The game utilizes the Turtle graphics library for drawing and displaying the map, dots representing
states, and textual information. It also includes graphical representations of player names.

6) - Tech Stack: The project uses Python as its programming language and leverages various Python libraries and modules,
including Turtle for graphics, Pandas for data handling (reading CSV files), and custom modules like letters_module for
displaying letters.

Note:
The image files angola_1.gif, chad.gif, france.gif, india.gif and usa.gif are the map pictures of the countries

The files angola_dots_coordinates.csv, chad_dots_coordinates.csv, france_dots_coordinates.csv, india_dots_coordinates 
and usa_dots_coordinates.csv are files which contain the locations of dots on the map given by the system randomly in order
to be attempted by the players.

The files angola_coordinates.csv, chad_coordinates.csv, france_coordinates.csv, india_coordinates and 
usa_coordinates.csv are files which contain the locations of states names on the map, that are going to be displayed
once the player answer is correct, else, on the same point the system displays XXX.

The file letters_module.py contains the 26 alphabet letters, so that at the end of the game, the system displays the 
name and a message according the score the player got in graphical way.

