import random

print('Rock Paper Scissors!')

# Initialize scores
player_score = 0
opponent_score = 0

while True:
    
    # Get Player input
    layer_input = input('Choose "rock", "paper", or "scissors" (Enter "quit" to exit): ').lower()
    print(f'You chose {player_input}')

    # Analyze Input
    if player_input == 'rock':
        player_input = 1
    elif player_input == 'paper':
        player_input = 2
    elif player_input == 'scissors':
        player_input = 3
    elif player_input == 'quit':
        print(f"Your Wins: {player_score}")
        print(f"Opponent Wins: {opponent_score}")
        break
    else:
        print('Enter a valid input!')
        continue

    # Determine opponent input
    opponent_input = random.randint(1, 3)

    # Calculate win, loss, or tie
    diff = player_input - opponent_input

    tie = False

    if diff == -2 or diff == 1:
        player_score += 1
        win_status = True
    elif diff == 0:
        tie = True
    else:
        opponent_score += 1
        win_status = False

    # Convert opponent input into a string
    if opponent_input == 1:
        opponent_input = 'rock'
    elif opponent_input == 2:
        opponent_input = 'paper'
    else:
        opponent_input = 'scissors'


    # Print results
    print(f'Opponent choses {opponent_input}')

    if tie:
        print('Its a tie!')
        continue

    if win_status:
        print('You win!')
    else:
        print('You lose!')


    # Original Implementation (Was able to reduce the repetition by using the difference between the scores)

    # if player_input == 1 and opponent_input == 3: # -2 win
    #     print('Opponent chose scissors! You win!')
    #     player_score += 1
    
    # if player_input == 2 and opponent_input == 3: # -1 lose
    #     print('Opponent chose scissors! You lose!')
    #     opponent_score += 1

    # if player_input == 1 and opponent_input == 2: # -1 lose
    #     print('Opponent chose paper! You lose!')
    #     opponent_score += 1

    # if player_input == 3 and opponent_input == 2: # 1 win
    #     print('Opponent chose paper! You win!')

    # if player_input == 2 == opponent_input == 1: # 1 win
    #     print('Opponent chose rock! You win!')
    #     opponent_score += 1

    # if player_input == 3 and opponent_input == 1: # 2 lose
    #     print('Opponent chose rock! You lose!')
    #     opponent_score += 1