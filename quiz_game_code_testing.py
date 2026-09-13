import random
import time

score : int = 0
questions : list = [{"question": "What is a variable in computer science?",
                    "choices": [
                    "A value",
                    "Something",
                    "He",
                    "Hi"],
                    "correct_answer": 2,
                    "points": 10,
                    "explanation": "Hi it is the 2nd choice"},
                    
                    {"question": "What is an atom?",
                    "choices": [
                    "Matter",
                    "Matter2",
                    "Matter3",
                    "Matter 4"],
                    "correct_answer": 2,
                    "points": 10,
                    "explanation": "Hi it is # 2"}
]

def display_chars_one_by_one(delay: float|int, sequence_of_chars: str) -> None:
  for char in sequence_of_chars:
    print(char, end='', flush=True)
    time.sleep(delay)
  print()

def rules_and_results(func) -> None:
  global score
  def wrapper():
      display_chars_one_by_one(0.05, "Hi this is the quiz game, here are 2 questions for ya!:")

      func()

      print(f'Your score: {score}')
  return wrapper


@rules_and_results
def read_ask_check(delay=0.05) -> None:
  global questions
  global score
  
  available_questions = questions.copy()
  
  
  while available_questions:
    random_question = random.choice(available_questions)
    
    display_chars_one_by_one(0.05, random_question["question"])

    for index, choice in enumerate(random_question["choices"], start=1):
        print(f'[{index}] {choice}')
    
    user_not_answered_proprely = True
    while user_not_answered_proprely:
          
          user_input = input("Enter your number: ")

          try:
            user_number_choice = int(user_input)

          except ValueError:
            display_chars_one_by_one(0.05, "Please, put a valid number")
            continue
           
            
          match user_number_choice:
              case value if value == random_question["correct_answer"]:
                display_chars_one_by_one(0.05, "Correct!")
                score += 50
                user_not_answered_proprely = False


              case _:
                print(f"Incorrect. {random_question["explanation"]}")
                user_not_answered_proprely = False
    
    available_questions.remove(random_question)


def main() -> None:
  read_ask_check()

if __name__ == "__main__":
  main()