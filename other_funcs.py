
# ================== Modules ======================== #
import json
import random

# This function serves to display text like you were typing on a keyobard
from quiz_game_code_testing import display_chars_one_by_one
# ================================================== #

player_score : int = 0
correct_answers_count: int = 0
question_count = 1


# =============== Quiz Game banner variable ================== #
quiz_game_banner : str = r"""
|========================================================|
|    ___        _                                        |
|   / _ \ _   _(_)____   __ _  __ _ _ __ ___   ___       |
|  | | | | | | | |_  /  / _` |/ _` | '_ ` _ \ / _ \      |
|  | |_| | |_| | |/ /  | (_| | (_| | | | | | |  __/      |  
|   \__\_\\__,_|_/___|  \__, |\__,_|_| |_| |_|\___|      |
|                       |___/                            |
|========================================================|
"""

# ================================================================== #

# =========================================================================================================================================== #
def read_questions_ask_and_check(file_path, amount_of_questions, player_score, correct_answers_count, question_count ) -> int:
   '''
   1. This function will read the files(easy, medium and hard) with JSON data (questions)
   
   2. This function will ask questions one by one
   
   3. This function will check the user input if it is equal to the correct answer


   params:
   1. file_path: The questions file's path
   2. amount_of_questions: The amount of random questions taken from the file
   3. player_score: the player's score
   4. correct_answers_count: The amount of correct answers the user accumulated
   5. question_count: the amount of questions that passed

   return: It will return the updated version of 'player_score', 'correct_answers_count' and 'question_count' variables
   '''
   

   # This will open the file and it will convert its content into python objects
   try:
      with file_path.open("r", encoding="utf-8") as file:
         file_questions = json.load(file)


   # If the file doesn't exist, it will print out this error in order to avoid crashing
   except FileNotFoundError:
      print(f"Error: the file '{file_path.name}' was not found.")
   
   # If the JSON file contains errors, it will print out this error in order to avoid crashing
   except json.JSONDecodeError:
      print(f"Error: the file '{file_path.name}' does not contain valid JSON.")

   available_questions = random.sample(file_questions, k=amount_of_questions)
         
   while available_questions:
      random_question = random.choice(available_questions)

      print("\n====================================")

      # Displays the points that the questions gives if the user gets the right answer
      # Displays the questions and its difficulty
      # Displays the amount of questions that passed
      display_chars_one_by_one(0.05, f'\n[{random_question["points"]} POINT] {random_question["question"]} [difficulty: {random_question["level"]}]  {question_count}/10 \n')
      
      # display the choices one by one
      for index, choice in enumerate(random_question["choices"], start=1):
         print(f'[{index}] {choice} \n')
      
      not_answered_proprely = True
      
      while not_answered_proprely:

         user_input = input("~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n|—---—(Enter your number below)\n|\n|---> ")
         print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

         try:
            user_number_choice = int(user_input)

         
         # if the user put a wrong type of data, it will ask the user to put a valid number
         except ValueError:
               display_chars_one_by_one(0.05, "Please, put a valid number\n")
               continue

         match user_number_choice:
            
            # If the user got the correct answer, it will increase the score by the amount of points the question
            # gives, it will increment the amount of times the user got a correct answer by 1
            case value if value == random_question['correct_answer']:
               display_chars_one_by_one(0.05, "Correct!\n")
               print("====================================\n") 
               question_count += 1
               player_score += random_question["points"]
               correct_answers_count +=1
               not_answered_proprely = False

            
            # If the user got the wrong number, it will say it is incorrect and make the user move on to the next question'''
            case _:
               display_chars_one_by_one(0.05, f"Incorrect. {random_question['explanation']}")
               not_answered_proprely = False
               question_count += 1


      available_questions.remove(random_question)
   
   return player_score, correct_answers_count, question_count
# =========================================================================================================================================== #