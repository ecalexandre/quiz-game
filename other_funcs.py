# ================== Modules ======================== #
import json
import random
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

# ===================================================================== #
def read_questions_ask_and_check(file_path, amount_of_questions, player_score, correct_answers_count, question_count ) -> int:
   try:
      with file_path.open("r", encoding="utf-8") as file:
         file_questions = json.load(file)

   except FileNotFoundError:
      print(f"Error: the file '{file_path.name}' was not found.")
   except json.JSONDecodeError:
      print(f"Error: the file '{file_path.name}' does not contain valid JSON.")

   available_questions = random.sample(file_questions, k=amount_of_questions)
         
   while available_questions:
      random_question = random.choice(available_questions)

      print("\n====================================")

      display_chars_one_by_one(0.05, f'\n[{random_question["points"]} POINTS] {random_question["question"]} [difficulty: {random_question["level"]}]  {question_count}/10 \n')

      for index, choice in enumerate(random_question["choices"], start=1):
         print(f'[{index}] {choice} \n')
      
      not_answered_proprely = True
      
      while not_answered_proprely:

         user_input = input("~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n|—---—(Enter your number below)\n|\n|---> ")
         print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")

         try:
            user_number_choice = int(user_input)

         except ValueError:
               display_chars_one_by_one(0.05, "Please, put a valid number\n")
               continue

         match user_number_choice:
      
            case value if value == random_question["correct_answer"]:
               display_chars_one_by_one(0.05, "Correct!\n")
               print("====================================\n") 
               question_count += 1
               player_score += random_question["points"]
               correct_answers_count +=1
               not_answered_proprely = False


            case _:
               display_chars_one_by_one(0.05, f"Incorrect. {random_question["explanation"]}")
               not_answered_proprely = False
               question_count += 1


      available_questions.remove(random_question)
   
   return player_score, correct_answers_count, question_count