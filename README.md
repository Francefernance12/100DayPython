# 100DayPython
Every day until the 100th day, I will be uploading 1 different project.

Day 1


Day 2


Day 3


Day 4
This is a simple game of rock, paper and scissors against the computer. 
Brief summary of my codes:
1. first thing first, I imported random to allow the computer to make randomly choose 3 choices.
2. I created a list of choices. [Rock, Paper, and Scissors]
3. I counted the number of choices in the list using len(). Used -1 for the count to start at 0.
4. Allowed the computer to choose 3 random number from the counted number.
5. I created an input for the player to choose rock, paper or scissor 
6. I made sets of if conditions for the player and computer to let python know what have they chose. I Added some cool ASCII art in the mean time
7. Finally, I added the win conditions to figure out who won
8. Program ends with who won the game.

challenges
I experienced some difficulties during this project.
- At one point, when I chose scissors and the computer also picked scissors, python kept on saying that the computer had won. I went back to find out the problem. I found out that in the computer win condition code block, within the `elif` statement, I mistakenly used player_choice variable instead of computer_choice variable.
- Within the player's win condition code block, I was trying to figure out why I kept choosing scissors when I intentionally chose rock. I found out that my player_choice variable input is a string data type so when I added in my if conditions, I was setting my player_choice is equal to a integer. A string data cannot be equal to a integer so I converted the integer into a string then it went well.

