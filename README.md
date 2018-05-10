# YuGiOh Dice Probabilities

Card / dice game introduced here: https://www.reddit.com/r/yugioh/comments/8ifec8/cp18_number_67/?ref=share&ref_source=link

## Rules

You and your opponent are each given two rolls. The numbers from each roll will be added together. You win the game if you have fewer points than your opponent.

As an advantage, you get to change the number from one of your opponent's rolls to 7. Ideally you'd choose the lower number since that would make a bigger difference and give you a greater chance of winning.

Example game: you roll a 4 and a 5, which gives you a total of 9. Your opponent rolls a 1 and a 5. Now you can take the lower number 1 and change that into a 7. This gives your opponent a total of 12, which means that you win the game.

## Ways to calculate the odds

The two proposed solutions here calculate the probability for a game to end in a win, draw or loss.

allthrows.py goes through each possible die-throw-combination, milliongames.py simulates millions of games. Each one counts the games won / drawn / lost and calculates each probability.

Interestingly enough, milliongames.py comes closer to the solution [calculated here](https://www.reddit.com/r/yugioh/comments/8ifec8/cp18_number_67/dyrrx26/) than allthrows.py that, as we thought, should be the real answer. The question is, where did we go wrong with allthrows.py?
