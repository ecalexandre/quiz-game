quiz_running = True; question_1 = True
question_2 = question_3 = question_4 = question_5 = question_6 = question_7 = question_8 = question_9 = question_10 = question_11 = False
question_12 = question_13 = question_14 = question_15 = BONUS_question = False
score = good_answers_gotten_by_user = 0

print("+-+-+-+-+ +-+-+-+-+\n|Q|u|i|z| |g|a|m|e|🏆\n+-+-+-+-+ +-+-+-+-+\nHi, wanna test your knowledge 🧠?\nThere are 15 questions in total")
print("Each question is worth 5 points\nEach question will get harder\nLet's see how many points you can get!\n")
while quiz_running:
    #easy part of the game
    if question_1:
      print("Which country is considered the largest in the world 🌎?    1/15")
      print("1. Canada\n \n2. United states\n \n3. Russia\n \n4. Japan")
      while question_1:
         user_answer_question_1 = input('Enter a number (1-4): ')
         try:
            val_1 = int(user_answer_question_1)
            match val_1:
                
                case 1|2|4: #if answer is either 1 or 2 or 4 = Incorrect
                    print("Wrong, the answer was Russia! Fun fact: Africa could fit russia only 1.77 times")
                    question_1 = False; question_2 = True
                
                case 3: #if answer is 3 = Correct
                    print("Nice, it is actually Russia! :)"); score += 5; good_answers_gotten_by_user += 1
                    question_1 = False; question_2 = True
                
                case _: #if answer is another number = Incorrect
                    print("Invalid number, the answer was Russia!")
                    question_1 = False; question_2 = True 
         
         except ValueError: #if the value type is wrong
                print("Please, enter a valid number next time. Mercury is the closest planet to the sun while being 36 million miles away from the sun")
                question_1 = False; question_2 = True 

    if question_2:
        print(""); print("Which planet 🪐 is closest to the sun?    2/15")
        print("1. Earth\n \n2. Mercury\n \n3. Mars\n \n4. Pluto")
        while question_2:
            user_answer_question_2 = input('Enter a number (1-4): ')
            try:    
               val_2 = int(user_answer_question_2)
               match val_2:
                case 1|3|4:
                    print("Wrong, Mercury is the closest planet to the sun while being 36 million miles away from the sun")
                    question_2 = False; question_3 = True
                
                case 2: #if answer is 2 = Correct
                    print("Bravo! It is, indeed, Mercury. Despite his distance away from the sun (36 million miles)")
                    question_2 = False; score += 5; question_3 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                    print("Invalid number, Mercury is the closest planet to the sun while being 36 million miles away from the sun")    
                    question_2 = False; question_3 = True
            
            except ValueError: #if the value type is wrong
                print("Please, enter a valid number next time. However Mercury is the closest planet to the sun while being 36 million miles away from the sun ")
                question_2 = False; question_3 = True

    if question_3:
       print(""); print('How many sides does a hexagon polygon have?    3/15')
       print('1. 5 sides\n \n2. 6 sides\n \n3. 4 sides\n \n4. 7 sides')
       while question_3:
             user_answer_question_3 = input('Enter a number (1-4): ')
             try:
               val_3 = int(user_answer_question_3)
               match val_3:
                    
                    case 1|3|4: #if answer is either 1 or 3 or 4 = Incorrect
                        print('Wrong, it has 6 sides. "hex" like "six" ')
                        question_3 = False; question_4 = True
                    
                    case 2: #if answer is 2 = Correct
                        print('Correct! it does have 6 sides!')
                        question_3 = False; score += 5; question_4 = True; good_answers_gotten_by_user +=1 
                   
                    case _: #if answer is another number = Incorrect
                        print('Invalid number, it has 6 sides. "hex" like "six" ')
                        question_3 = False; question_4 = True
             
             except ValueError: #if the value type is wrong
                print('Please, enter a valid number next time. But it does have 6 sides')
                question_3 = False; question_4 = True

    if question_4:
       print(''); print('Which city 🏢 in the world is known for his name: "the city that never sleeps"❌💤?   4/15')
       print('1. New York\n \n2. Paris\n \n3. Tokyo\n \n4. Montreal')
       while question_4:
            user_answer_question_4 = input('Enter a number (1-4): ')
            try:
              val_4 = int(user_answer_question_4)
              match val_4:
                
                case 1: #if answer is 1 = Correct
                    print('You got it! It is New York!')
                    question_4 = False; score += 5; question_5 = True; good_answers_gotten_by_user += 1
                
                case 2|3|4: #if answer is either 2 or 3 or 4 = Incorrect
                    print('Wrong, New York is the city known for his permanent noises')
                    question_4 = False; question_5 = True
                
                case _: #if answer is another number = Incorrect
                    print('Invalid number. New York is the city known for his permanent noises ')
                    question_4 = False; question_5 = True
            
            except ValueError: #if the value type is wrong
                print('Please, enter a valid number next time. But the answer was New York!')
                question_4 = False; question_5 = True

    if question_5:
       print(''); print('Still here?'); print(''); print('It will get harder now :D'); print('')
       print('10 * x = 15000    5/15'); print('x = ?'); print('')
       print('1. 3000\n \n2. 1500\n \n3. 6002\n \n4. 150')
       while question_5:
        user_answer_question_5 = input('Enter a number (1-4): ')
        try:
            val_5 = int(user_answer_question_5)
            match val_5:
                
                case 1|3|4: #if answer is either 1 or 3 or 4 = Incorrect
                    print('Incorrect, The value of x is 1500 because 10 times 1500 equals to 15000')
                    question_5 = False; question_6 = True
                
                case 2: #if answer is 2 = Correct
                    print('Nice one! it is 1500 because 10 times 1500 equals to 15000')
                    question_5 = False; score += 5; question_6 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                   print('Invalid number, The value of x is 1500 because 10 times 1500 equals to 15000')
                   question_5 = False; question_6 = True
        
        except ValueError: #if the value type is wrong
            print('Please, enter a valid number next time. The answer was 1500 because 10 times 1500 equals to 15000')
            question_5 = False; question_6 = True

    if question_6:
       print(''); print('Which country has the largest population 🧑‍🤝‍🧑in the world🌎 in 2026?    6/15')
       print('1. Japan\n \n2. China\n \n3. United states\n \n4. India')
       while question_6:
        user_answer_question_6 = input('Enter a number (1-4): ')
        try:
            val_6 = int(user_answer_question_6)
            match val_6:
                
                case 1|2|3: #if answer is either 1 or 2 or 3 = Incorrect
                    print('Wrong, India has over 1.48 billion people while China takes the 2nd place by having 1.41 billion people')
                    question_6 = False; question_7 = True
                
                case 4: #if answer is 4 = Correct
                    print('Yes, it is India due to having 1.48 billion people which makes him in 1st place')
                    question_6 = False; score += 5; question_7 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                   print('Invalid number, India has over 1.48 billion people while China takes the 2nd place by having 1.41 billion people')
                   question_6 = False; question_7 = True
        
        except ValueError:  #if the value type is wrong
               print('Please enter a valid number next time. But India has over 1.48 billion people while China takes the 2nd place by having 1.41 billion people')
               question_6 = False; question_7 = True

    if question_7:
       print(''); print('In the periodic table ⚛️, what is the chemical element with the symbol Fe?    7/15')
       print('1. Fire\n \n2. Iron\n \n3. Fluorine\n \n4. Hydrogen')
       while question_7:
           user_answer_question_7 = input('Enter a number (1-4): ')
           try:
            val_7 = int(user_answer_question_7)
            match val_7:
                
                case 1|3|4: #if answer is either 1 or 3 or 4 = Incorrect
                    print('Nice try but wrong answer. The answer is Iron because its symbol in the periodic table is Fe')
                    question_7 = False; question_8 = True
                
                case 2: #if answer is 2 = Correct
                    print('Nice, you got it! It is Iron!')
                    question_7 = False; score += 5; question_8 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                    print('Invalid number. The answer is Iron because its symbol in the periodic table is Fe')
                    question_7 = False; question_8 = True
           
           except ValueError:  #if the value type is wrong
                 print('Please put a valid number next time. ce try but wrong answer. The answer is Iron because its symbol in the periodic table is Fe')
                 question_7 = False; question_8 = True

    if question_8:
       print(''); print('In what year did the us declared its independence?    8/15')
       print('1. 1774\n \n2. 1870\n \n3. 1776\n \n4. 2010')
       while question_8:
            user_answer_question_8 = input('Enter a number (1-4): ')
            try:
              val_8 = int(user_answer_question_8)
              match val_8:
                    
                    case 1|2|4: #if answer is either 1 or 2 or 4 = Incorrect
                        print('This is a nice guess but it is Incorrect. The us declared its independence on July 4, 1776')
                        question_8 = False; question_9 = True
                    
                    case 3: #if answer is 3 = Correct
                        print('It is indeed in 1776! The us declared its independence on July 4, 1776')
                        question_8 = False; score+=5; question_9 = True; good_answers_gotten_by_user += 1
                    
                    case _: #if answer is another number = Incorrect
                       print('Invalid number. The us declared its independence on July 4, 1776')
                       question_8 = False; question_9 = True
            
            except ValueError: #if the value type is wrong
                print('Please enter a valid number next time. The us declared its independence on July 4, 1776')
                question_8 = False; question_9 = True

    if question_9:
       print(''); print('What is the currency 💰 used in Japan?    9/15')
       print('1. Dollar\n \n2. Yen\n \n3. Peso\n \n4. Yuan')
       while question_9:
        user_answer_question_9 = input('Enter a number (1-4): ')
        try:
           val_9 = int(user_answer_question_9)
           match val_9:
            
            case 1|3|4: #if answer is either 1 or 3 or 4 = Incorrect
                print("Incorrect answer. Japan's current currency name is 'Yen'")
                question_9 = False; question_10 = True    
            
            case 2: #if answer is 2 = Correct
               print('Nice! It is indeed named "Yen"')
               question_9 = False; score += 5; question_10 = True; good_answers_gotten_by_user += 1
            
            case _: #if answer is another number = Incorrect
               print("Invalid number, Japan's current currency name is 'Yen'")
               question_9 = False; question_10 = True    
        
        except ValueError: #if the value type is wrong
            print("Please put a valid number next time. Japan's current currency name is 'Yen'")
            question_9 = False; question_10 = True

    if question_10:
       print(''); print('How to calculate the area of a rectangle?    10/15')
       print('1. Base multiplied by height (b x h)\n \n2. (Base multiplied by height) divided by 2 ((b x h) : 2)\n \n3. 4 times a side of a rectangle (4s)\n \n4. Base multiplied by itself (b*2)')
       while question_10:
        user_answer_question_10 = input('Enter a number (1-4): ')
        try:
            val_10 = int(user_answer_question_10)
            match val_10:
               
                case 2|3|4: #if answer is either 2 or 3 or 4 = Incorrect
                    print('Incorrect. The area of a rectangle is equivalent to the base multiplied by the height')
                    question_10 = False; question_11 = True
                
                case 1: #if answer is 1 = Correct
                   print('Nice! you got it! It is indeed the base multiplied by the height')
                   question_10 = False; score += 5; question_11 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                  print('Invalid number. The area of a rectangle is equivalent to the base multiplied by the height')
                  question_10 = False; question_11 = True   
        
        except ValueError: #if the value type is wrong
           print('Please put a valid number next time. The area of a rectangle is equivalent to the base multiplied by the height')                 
           question_10 = False; question_11 = True
    
     #Hard part of the game 🔥🔥
    if question_11:
       print(''); print("Good luck now...."); print(''); print('🔥🔥 You reached the HARDEST part of the game 🔥🔥 :)'); print('\n \nEach question now is worth 10 points until the last question')
       print('What is the main gas 💨 that humans exhale 😮‍💨?    🔥11/15🔥'); print('1. Oxygen\n \n2. Air\n \n3. carbon dioxide\n \n4. NaCl\n \n5. O2\n \n6. Co2')
       while question_11:
        user_answer_question_11 = input('Enter a number (1-6): ')
        try:
            val_11 = int(user_answer_question_11)
            match val_11:
                
                case 1|2|4|5|6: #if answer is either 1 or 2 or 4 or 5 or 6 = Incorrect
                    print('Nice! but INCORRECT! The human exhales carbon dioxide which is a waste made by the body')
                    question_11 = False; question_12 = True
                
                case 3: #if answer is 3 = Correct
                   print('hmmm... it is CORRECT! the human does exhale carbon dioxide!')
                   question_11 = False; score += 10; question_12 = True; good_answers_gotten_by_user += 1
                
                case _: #if answer is another number = Incorrect
                   print('Invalid number. The human exhales carbon dioxide which is a waste made by the body')
                   question_11 = False; question_12 = True
        
        except ValueError: #if the value type is wrong
            print('Please, put a valid number next time. The human exhales carbon dioxide which is a waste made by the body')
            question_11 = False; question_12 = True

    if question_12:
       print(''); print('What is always in front of you but can’t be seen 👀?    🔥12/15🔥')
       print('1. Your shadow\n \n2. Air\n \n3. The future\n \n4. Everything that is in front of me\n \n5. The past\n \n6. Your body')
       while question_12:
        user_answer_question_12 = input('Enter a number (1-6): ')
        try:
          val_12 = int(user_answer_question_12)
          match val_12:
            
            case 1|2|4|5|6: #if answer is either 1 or 2 or 4 or 5 or 6 = Incorrect
                print('It was a nice guess..... but Incorrect. The future is always in front of you. You cannot see it or get past it')
                question_12 = False; question_13 = True
            
            case 3: #if answer is 3 = Correct
                print('It was correct! It is indeed the future! The future is always in front of you. You cannot see it or get past it')
                question_12 = False; score += 10; question_13 = True; good_answers_gotten_by_user += 1
            
            case _: #if answer is another number = Incorrect
               print('Invalid number, The future is always in front of you. You cannot see it or get past it')
               question_12 = False; question_13 = True
        
        except ValueError: #if the value type is wrong
            print('Please put a valid number next time. However, the future is always in front of you. You cannot see it or get past it')
            question_12 = False; question_13 = True

    if question_13:
       print(''); print('A + B = 32    🔥13/15🔥'); print('A - B = 18'); print('A * B = ?'); print('')
       print('1. 200\n \n2. 10\n \n3. 187\n \n4. 50\n \n5. 175\n \n6. 70')
       while question_13:
        user_answer_question_13 = input('Enter a number (1-6): ')
        try:
          val_13 = int(user_answer_question_13)
          match val_13:
            
            case 1|2|3|4|6: #if answer is either 1 or 2 or 3 or 4 or 6 = Incorrect
                print('Nice guess! but Incorrect. Because A = 25, B = 7 so when you multiply these values, it gives 175! ')
                question_13 = False; question_14 = True
            
            case 5: #if answer is 5 = Correct
                print('Nice! you got the right answer! It is indeed 175! Because A = 25, B = 7 so when you multiply these values, it gives 175!')
                question_13 = False; score += 10; good_answers_gotten_by_user += 1; question_14 = True
            
            case _: #if answer is another number = Incorrect
               print('Invalid number. Because A = 25, B = 7 so when you multiply these values, it gives 175!')
               question_13 = False; question_14 = True
        
        except ValueError: #if the value type is wrong
            print('Please put a valid number next time. However, A = 25, B = 7 so when you multiply these values, it gives 175!')
            question_13 = False; question_14 = True

    if question_14:
       print(''); print('What is the approximate speed 🏃‍♂️of light ✨ in kilometers (per second)?    🔥14/15🔥')
       print('1. 299,792,458 m/s\n \n2. 300,000,000 km/s\n \n3. 299,792 km/s\n \n4. 272,999 km/s\n \n5. 186,282 mi/s\n \n6. 100,000,000,000 km/s')
       while question_14:
        user_answer_question_14 = input('Enter a number (1-6): ')
        try:
          val_14 = int(user_answer_question_14)
          match val_14:
            
            case 1|5: #if answer is 1 or 5 = Incorrect
              print("Incorrect answer. The answer had to be in KILOMETERS. However, light's speed is approximatively 299,792 kilometers per second, according to scientists.")
              question_14 = False; BONUS_question = True
            
            case 2|4|6: #if answer is 2 or 4 or 6 = Incorrect
               print("Incorrect answer. Light's speed is approximatively 299,792 kilometers per second, according to scientists.")
               question_14 = False; BONUS_question = True
            
            case 3: #if answer is 3 = Correct
                print('Nice attempt! You got it! it is approximatively 299,792 kilometers per second, according to scientists')
                question_14 = False; score += 10; good_answers_gotten_by_user += 1; BONUS_question = True
            
            case _: #if answer is another number = Incorrect
                print("Invalid number, light's speed is approximatively 299,792 kilometers per second, according to scientists.")
                question_14 = False; BONUS_question = True
        
        except ValueError: #if the value type is wrong
            print("Please, put a valid number next time. light's speed is approximatively 299,792 kilometers per second, according to scientists.")
            question_14 = False; BONUS_question = True

    if BONUS_question:
       print(''); print("Before we get to the last question, here is a bonus question for you!"); print("If you get the right answer, you'll win 5 exclusise points!"); print('')
       print('Question: If you earn 80$ in 4 hours, how many hours will it take for you to earn 2000$    🔥 👀BONUS/15👀 🔥')
       print('1. 40 hours \n \n2. 100 hours\n \n3. 50 hours\n \n4. 250 hours\n \n5. 450 hours\n \n6. 400 hours')
       while BONUS_question:
        user_answer_BONUS = input('Enter a number (1-6): ')
        try:
            val_Bonus = int(user_answer_BONUS)
            match val_Bonus:
                
                case 1|3|4|5|6: #if answer is 1 or 3 or 4 or 5 or 6 = Incorrect
                    print('Nice attempt! The answer is incorrect though. Because you get 100$ in 5 hours, 100 * 10 = 1000$ which is 50 hours. Multiply it by 2 (1000 * 2 = 2000$) which is 100 hours of work')
                    BONUS_question = False; question_15 = True
                
                case 2: #if answer is 2 = Correct
                    print('You got the right answer! it is 100 hours of work. Because you get 100$ in 5 hours, 100 * 10 = 1000$ which is 50 hours. Multiply it by 2 (1000 * 2 = 2000$) which is 100 hours of work')
                    BONUS_question = False; score += 5; good_answers_gotten_by_user += 1; question_15 = True
                
                case _: #if answer is another number = Incorrect
                    print('Invalid number. you get 100$ in 5 hours, 100 * 10 = 1000$ which is 50 hours. Multiply it by 2 (1000 * 2 = 2000$) which is 100 hours of work')
                    BONUS_question = False; question_15 = True
        
        except ValueError: #if the value type is wrong
            print('Please, put a valid number next time! However, the answer = you get 100$ in 5 hours, 100 * 10 = 1000$ which is 50 hours. Multiply it by 2 (1000 * 2 = 2000$) which is 100 hours of work')
            BONUS_question = False; question_15 = True
    
    if question_15:
        print("\n \nWhat type of mathematical function represents this function rule? ---> f(x) = 3(x-4)    🔥15/15🔥")
        print('1. Identity function\n \n2. Constant function\n \n3. Partial function\n \n4. Linear function\n \n5. Rational function\n \n6. Quadratic function')
        while question_15:
             user_answer_question_15 = input('Enter a number (1-6): ')
             try:
                val_15 = int(user_answer_question_15)
                match val_15:
                  
                  case 1|2|3|5|6:
                    print("This is incorrect. When you look at the function rule it is f(x) = 3x - 4, which is a linear function\n \nbecause it is the only type of first-degree function that has both the rate of change (a) and the initial value (b) that is not worth 0\n \n")
                    question_15 = False; quiz_running = False; print(f'+-+-+-+-+-+-+-+\n R|e|s|u|l|t|s|\n+-+-+-+-+-+-+-+\n \nYou got {good_answers_gotten_by_user} good answers in total\n \nYour score is {score}%')
                  
                  case 4:
                    print("Correct you got it!\n \nit is the only type of first-degree function that has both the rate of change (a) and the initial value (b) that is not worth 0\n \n")
                    question_15 = False; quiz_running = False; score += 10; good_answers_gotten_by_user += 1; print(f'+-+-+-+-+-+-+-+\n R|e|s|u|l|t|s|\n+-+-+-+-+-+-+-+\n \nYou got {good_answers_gotten_by_user} good answers in total\n \nYour score is {score}%')
                  
                  case _:
                    print("Invalid number, It is the linear function\n \nbecause it is the only type of first-degree function that has both the rate of change (a) and the initial value (b) that is not worth 0\n \n")
                    question_15 = False; quiz_running = False; print(f'+-+-+-+-+-+-+-+\n R|e|s|u|l|t|s|\n+-+-+-+-+-+-+-+\n \nYou got {good_answers_gotten_by_user} good answers in total\n \nYour score is {score}%') 

             except ValueError:
                print("You should have put a valid number. It is however, the linear function\n \nBecause it is the only first-degree function that both the rate of change and the initial value that is not worth 0\n \n")
                question_15 = False; quiz_running = False; print(f'+-+-+-+-+-+-+-+\n R|e|s|u|l|t|s|\n+-+-+-+-+-+-+-+\n \nYou got {good_answers_gotten_by_user} good answers in total\n \nYour score is {score}%')
