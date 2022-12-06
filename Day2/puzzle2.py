#!/usr/bin/env python3

# Define variables
# For the opponent: the key is what is read from the file and the value is the translated name.
opponent = {'A':'Rock', 'B':'Paper', 'C':'Scissors'}
# For the player: the key is what is read from the file
# the value is a new dictionary where the keys are the opponents moves and 
# the values are the moves the player should do.
player = {'X':{'Rock':'Scissors', 'Paper':'Rock', 'Scissors':'Paper'}, # Lose 
          'Y':{'Rock':'Rock', 'Paper':'Paper', 'Scissors':'Scissors'}, # Draw
          'Z':{'Rock':'Paper', 'Paper':'Scissors', 'Scissors':'Rock'}} # Win
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
            player_outcome = line[1]
            player_possibilities = player[player_outcome]  # Find the possibilities for the player
            player_plays = player_possibilities[opponent_plays]  # What should the player play
            if player_outcome == 'Z':  # The player is to win
                round_score += 6
            elif player_outcome == 'Y':  # The player is to tie
                round_score += 3
            round_score += scores[player_plays]  # Add the score from the play to get round score
            game_score += round_score  # Add to total score
            round_score = 0  # Reset the round score
            
# Output data
print(f"The total score for the game is: {game_score}.")
