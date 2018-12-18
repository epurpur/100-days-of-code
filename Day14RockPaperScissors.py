from RPSclasses import Roll, Player
import time

def main():
    print_header()
    
    
    game_loop()
    #game_loop(player1, player2, rolls)
        
def print_header():
    print('----------------------------------------')
    print('            Rock Paper Scissors         ')
    print('----------------------------------------')

    print('Today we are going to play a game')
    time.sleep(1)
    player1 = Player("Erich")
    player2 = Player("Computer")
    print("Today, Player 1 is %s and Player 2 is %s." % (player1.name, player2.name))
    time.sleep(2)
    print("Starting game now...")
    time.sleep(2)
    

def build_three_rolls(results_from_game):
    """logs results of each players' rolls in game"""
    print("Player score:", results_from_game[0], "Computer score:", results_from_game[1])
    if results_from_game[0] == results_from_game[1]:
        print("Result was a tie, play again!")
        game_loop()
    elif results_from_game[0] > results_from_game[1]:
        print("You win, congratulations!")
    else:
        print("Computer wins, better luck next time")


def game_loop():
    count = 0    
    player_wins = 0
    cpu_wins = 0
    
    while count < 3:
        outcome = Roll.play()
        #outcome[0] = my choice
        #outcome[1] = cpu choice
        if outcome[0] == outcome[1]:
            print("Tie!")
        elif outcome[0] == 'rock':
            if outcome[1] == 'paper':
                print("Computer wins!")
                cpu_wins += 1
            else:
                print("You win!")
                player_wins += 1
        elif outcome[0] == 'paper':
            if outcome[1] == 'scissors':
                print("Computer Wins!")
                cpu_wins += 1
            else:
                print("You win!")
                player_wins += 1
        elif outcome[0] == 'scissors':
            if outcome[1] == 'rock':
                print("Computer wins!")
                cpu_wins += 1
            else:
                print("You win!")
                player_wins += 1
        count += 1
    
    print("After 3 games the results are...")
    time.sleep(3)
  
    results = player_wins, cpu_wins
    
    build_three_rolls(results)

    
if __name__ == '__main__':              #this is in here to determine if this module(.py file) is being run directly or is imported
    main()                              #if this module (.py file) is run directly, initiate the main() function