import numpy as np

print("Hello world")

number = np.random.randint(1, 101) # загадываем число

def new_game(num:int) -> int:
    count = 0 
    while True:
        count += 1
        predict_number = int(input("Угадай число от 1 до 100"))
    
        if predict_number > number:
            print("Must be low")
        elif predict_number < number:
            print("Must be hight")
        else:
            print("good")
            break

new_game(100)
