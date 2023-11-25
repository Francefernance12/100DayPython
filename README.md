# 100DayPython
<h3>Every day until the 100th day, I will be uploading 1 different project.</h3>
 
<h3>Day 1</h3>
 
 This is a straightforward generator designed to generate a unique band name. You'll respond to a series of questions, and your answers will amalgamate into a distinctive band name for you.
 
  Brief summary of my codes:
1. Welcome the User using print().
2. I create 2 inputs inside a variable named city and pets_name to get answers of the questions from the User
3. I print the name of the band by combining city and pets_name using concatenation.
 - Optional: I could've used an F string if I wanted to instead of concatenation.

 <h3>Day 2</h3>
 
 I've developed a tip calculator that not only computes the total bill amount with the tip included but also facilitates the calculation of individual shares for a bill split among multiple people. It's a convenient tool for simplifying the process when dining out with friends.
 
 Brief summary of my codes:
1. Welcome the User using print
2. Defined the bill, tip% and the number of people splitting the bill
3. calculate the tip percentage by dividing the tip to 100
4. I would then calculate the bill with the tip percentage to calculate how much tip must be payed
5. I would define the total amount by adding the bill + the tip amount then I rounded the number by 2 by 2 decimal points
6. after that I defined the split amount to calculate how much each person must pay for the total bill
7. Finally, I added the print statement to display the total amount of the bill plus tip.
8. I updated the code, I added an if statement to display only the total amount if 1 person payed but if more than one person payed, it will display the amount of perople paying and the amount they each have to pay.
 
 
 <h3>Day 3</h3>
 
 This game is an adventure where players advance through the storyline by typing in their actions.
 
  Brief summary of my codes:
   1. I incorporated an element of fun by integrating ASCII art.
   2. The initial player choice was defined through an input prompt.
   3. Subsequently, I established an if statement to guide Python in responding to the player's initial choice. Depending on the player's selection, the code directs the player through various story progressions or leads them to a game over screen.
   4. Within these initial if statements, I introduced another layer of choice for the player.
   5. To further diversify the narrative, nested if statements were implemented to handle the third and final choice, creating a branching storyline based on the player's decisions.
   6. Finally, if the player choose the right door at their last choice, they would win!

 
 
 <h3>Day 4</h3> 
 
This is a simple game of rock, paper and scissors against the computer. 
 Brief summary of my codes:
1. To introduce randomness into Python's selection process, I imported the 'random' module.
2. I established a list encompassing the choices: Rock, Paper, and Scissors.
3. Utilizing the 'len()' function, I determined the number of choices in the list, starting the count at 0 by subtracting 1.
4. The computer was granted the ability to make selections by generating three random numbers within the count.
5. I implemented an input mechanism for players to choose between rock, paper, or scissors.
6. Sets of if conditions were crafted for both the player and computer choices, incorporating engaging ASCII art for visual appeal.
7. Win conditions were incorporated to ascertain the victor.
8. The program concludes by revealing the winner of the game.
 
 challenges
 
 I experienced some difficulties during this project. let me share:
- At a certain juncture, when I selected scissors and the computer also chose scissors, Python consistently indicated that the computer had won. Upon investigation, I discovered that in the code block defining the computer's win condition, I had inadvertently utilized the player_choice variable instead of the correct computer_choice variable within the elif statement.
- While examining the player's win condition code block, I sought to understand why my intentional choice of rock was consistently registering as scissors. It became evident that the issue stemmed from the data type of the player_choice variable, which was initially a string. The problem arose when I attempted to equate this string variable to an integer within my if conditions. Recognizing the incompatibility, I resolved the issue by converting the integer to a string, resulting in the desired functionality.
 
 <h3>Day 5</h3>

  This project is a random password generator. It will take your inputs which are number of characters you want to put in your password. There are 3 different characters; letters, numbers, and symbols. After taking all the inputs. python will create the password for you.
 
 Brief summary of my codes:
  - I create 3 lists of different types of characters
  - I take in the User's input. I convert the input into an integer
  - defined the password. convert the password as a string
  - created 3 for loops for each list to randomize and choose the characters
  - I turn the password into a list then shuffle the password
  - I reveal the User's new password.

 Challenges
 - I had a problem with shuffling the password. 

<h3>Day 6</h3>

<h3>Day 7</h3>

This project is a Hangman Game. This Hangman game is a guessing game where the player guesses a letter to slowly figure out the whole word.
If the Player guesses the word wrong, the player loses a life.
If the Player guesses the letter correctly, the letter will fill in the blanks until all the blanks have been filled and the word is fully revealed.

Brief summary of my codes:
 - 


<h3>Day 8</h3>
The project is a Caesar Cipher generator. The Caesar cipher is a basic encryption technique in cryptography where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
The User need to type in the words they want to encrypt or decrypt.
Then the User needs to type in the number of shifts to encrypt or decrypt.
After receiving the inputs, python should start displaying the User's encrypted or decrypted words.

Brief summary of my codes:
 - I created an alphabet list
 - I created a while loop that would stop until the User does not want to try again.
 - Inside the while loop, I Created inputs for the user to type in their words, choice and numbers.
 - I calculate the number of shifts divisible to the number of alphabets in the list to handle larger shifts values.
 - Created the Caesar function which allows the inputted words to be encoded or decoded.
 - Printed the ASCII art logo for the project. The ASCII art logo is from another python file I created that contains the ASCII art.

<h3>Day 9</h3>