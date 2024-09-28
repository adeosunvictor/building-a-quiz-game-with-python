# WELCOME AND INTRODUCTION

print("welcome to QUIZ MASTER!!")
User = str(input("what is your name? "))
playing = input(f"{User} do you Do you want to play? ")
 
if playing.lower()!= "yes":
    quit()

print("Okay! let's play 😊 ")


# keeping record of the score
score = 0

# QUESTION AND ANSWERS 

answer = input("what does cpu stand for?  ").lower() 
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input("what does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")




answer = input("what does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4 )*100) + "%")