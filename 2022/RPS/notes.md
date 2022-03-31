# Exp

# Flag: picoCTF{50M3_3X7R3M3_1UCK_B69E01B8}

Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row. Connect to the program with netcat: $ nc saturn.picoctf.net 53865 The program's source code with the flag redacted can be downloaded here.

The winning condition is `strstr(player_turn, loses[computer_turn])`
it searches for the string `loses[computer_turn]` in `player_turn` so if we put all the values in `player_turn` then it should always win

There is no validation of the player_turn input.

```
Please make your selection (rock/paper/scissors):
rockpaperscissors
rockpaperscissors
You played: rockpaperscissors
The computer played: paper
You win! Play again?
Congrats, here's the flag!
picoCTF{50M3_3X7R3M3_1UCK_B69E01B8}
Type '1' to play a game
Type '2' to exit the program
```