#!/usr/bin/env python3

# Define variables
# For the opponent: the key is what is read from the file and the value is the translated name.
opponent = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
# For the player: The key is what is read from the file.
# The value is a tuple with the first value being the translated play.
# the second value is the players value that would result in the player winning.
player = {'X':('Rock','Scissors'), 'Y':('Paper','Rock'), 'Z':('Scissors','Paper')}
# The scores dict has keys for the translated names and values for their scores
scores = {'Rock':1, 'Paper':2, 'Scissors':3}
round_score = 0  # Track the score for the round
game_score = 0  # Track the score for the game

# Read input file
with open("puzzle_input.txt") as f:
    for line in f:
        if line != "\n":  # Line is not a blank line so continue playing game
            line = line.split()  # splits on the space between characters
            opponent_plays = line[0]
            opponent_plays = opponent[opponent_plays]  # Translate opponent play
            player_plays = line[1]
            player_plays = player[player_plays]  # Get winning tuple for players play
            if player_plays[1] == opponent_plays:  # Test if player won
                round_score += 6
            elif player_plays[0] == opponent_plays:  # Test if player tied
                round_score += 3
            round_score += scores[player_plays[0]]  # Add the score from the play to get round score
            game_score += round_score  # Add to total score
            round_score = 0  # Reset the round score
            
# Output data
print(f"The total score for the game is: {game_score}.")
