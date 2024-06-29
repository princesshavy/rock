print("Welcome to Rock,Paper,Scissors!")
playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Great!Let's play :)")
score = 0


answer = input( "Which is the strongest? ")
if answer == "Rock":
    print ("GENIUS!")
    score += 1
else:
    print("INCORRECT")

print("Next Question!")
answer = input("Which is more important to the world? ")
if answer == "Paper":
    print ("Good!")
    score += 1
else:
    print("INCORRECT")

print("Next Question!")
answer = input("Which is destructive to the rest? ")
if answer == "Rock":
    print ("You are a GENIUS!")
    score += 1
else:
    print("INCORRECT")


print("Next Question!")
answer = input("Which only destroys 1 of the others? ")
if answer == "Scissors":
    print ("You are a GENIUS!")
    score += 1
else:
    print("INCORRECT")

print("Next Question!")
answer = input("Which is the miners pride? ")
if answer == "Rock":
    print ("You are a GENIUS!")
    score += 1
else:
    print("INCORRECT")

print("You got" + " " + str(score) + " questions correct!")


