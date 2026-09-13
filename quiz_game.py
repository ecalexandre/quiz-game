'''__
  | _ \\ _   _(_)____   __ _  __ _ _ __ ___   ___
 | | | | | | | |_  /  / _` |/ _` | '_ ` _ \\ / _ \
 | |_| | |_| | |/ /  | (_| | (_| | | | | | |  __/
 \\__\\_\\__,_|_/ | \\__, \\__,_|_| |_| |_\\___|
                     |___/
'''
# ================== Modules ======================== #
from pathlib import Path

# My quiz game core variables/functions
from other_funcs import player_score, correct_answers_count, question_count, quiz_game_banner
from other_funcs import read_questions_ask_and_check
from quiz_game_code_testing import display_chars_one_by_one
# ================================================== #

# ========================= questions files ============================ #
easy_questions_file_path = Path("questions") / "easy-questions.json"
medium_questions_file_path = Path("questions") / "medium-questions.json"
hard_questions_file_path = Path("questions") / "hard-questions.json"
# ====================================================================== #


def intro_and_results(game_running) -> None:
    '''
    This function serves to display the rules at the beginning of the game and the results at the end
    of the game


    param:
    1. game_running: This represents the function that this decorator is going to change its behaviour
    which will be the 'run_quiz' function
    '''
    def wrapper() -> None:
        global player_score
        global correct_answers_count
        global quiz_game_banner
        display_chars_one_by_one(0.05, "Hi, Welcome to the quiz game 🏆 and here, I am here to test your general knowledge 🧠!")
        display_chars_one_by_one(0.05, "There are 10 questions in total that you will have to answer. Each one will potentially get harder so be careful! 😉")
        display_chars_one_by_one(0.05, "Good luck!")
        game_running()
        display_chars_one_by_one(0.05, "     +-+-+-+-+-+-+-+\n 🏆🏆 R|e|s|u|l|t|s| 🏆🏆\n     +-+-+-+-+-+-+-+ \n\n")
        display_chars_one_by_one(0.05, f'Your Points: {player_score} points!')
        display_chars_one_by_one(0.05, f'You got {correct_answers_count} correct answers in total')
        display_chars_one_by_one(0.05, f'Percentage: {player_score}%')
    return wrapper


@intro_and_results
def run_quiz():
    '''
    This function will call the function 3 times for the easy,medium and hard files
    This functions will make sure the `player_score`, the `correct_answers_count` and the `question_count`
    variables store the updated versions of themselves that got returned by the function 3 times
    
    '''
    
    global easy_questions_file_path
    global medium_questions_file_path
    global hard_questions_file_path
    global player_score
    global correct_answers_count
    global question_count
    
    # =========================== updated variables ======================================== #
    player_score, correct_answers_count, question_count = read_questions_ask_and_check(
    easy_questions_file_path, 3, player_score, correct_answers_count, question_count
    )
    player_score, correct_answers_count, question_count = read_questions_ask_and_check(
    medium_questions_file_path, 4, player_score, correct_answers_count, question_count
    )
    player_score, correct_answers_count, question_count = read_questions_ask_and_check(
    hard_questions_file_path, 3, player_score, correct_answers_count, question_count
    )
    # ==================================================================================== #



def play_or_not() -> None:
    display_chars_one_by_one(0.005, quiz_game_banner)
    display_chars_one_by_one(0.04, "Hi! You have succesfully entered the quiz game!")
    
    user_didnt_answer_correctly = True
    while user_didnt_answer_correctly:   
        user_choice = input("Do you wish to continue [Y or N]: ")
        try:
           match user_choice:
             
             # If user decides to play, it will run the quiz game
             case value if value == "Y" or value == "y":
               print("Loading", end='')
               display_chars_one_by_one(1, "...")
               print()
               run_quiz()
               user_didnt_answer_correctly = False
               
        
             # If user decides to stop, the script stops
             case value if value == "N" or value == "n":
               print("succesfully quit")
               user_didnt_answer_correctly = False
             
             # If the user put another letter, the program will tell him to put a valid choice (Yes or no)
             case _:
               display_chars_one_by_one(0.02, "Please, put a valid choice")
        
        # If the user didn't put a letter at all, the program will tell him to put a valid choice (Yes or no)
        except ValueError:
            print("Please, put a valid choice")


# The main function
def main():
    play_or_not()   


# Runs the main function
if __name__ == '__main__':
    main()