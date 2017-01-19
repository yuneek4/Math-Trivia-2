#Math Trivia Part 2
print("This is part two to the math trivia you have just taken if you took the first one")
name=input("Enter your nanme: ")
print("\nWelcome back, here is parttwo to the math trivia you have just taken previously. If you are a new comer that is fine too, Welcome!")
print("Here is a total of 10 questions that you will be answering. This is not MULTIPLE CHOICE")
print("Please enter you answer")

print("-----------------------------------------------------------------------------------------")

# set quiz score to 0

score= 0
score= int(score) # covert 0 into a number so we can add scores

# question 1
print("Question 1: What is the mean when given the dat values: 7, 9, 4, 2, 9, 5?")
print("")
Q1answer = "6" # right answer to question 1
Q1response = input("your answer: ")
if Q1response == "6" or Q1response == "six":
    print("great job! keep up the good work "  + Q1response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your cuurent score is " + str(score) + " out of 10 ")

# question 2
print("Question 2: What is the median when given the data values: 5, 11,58, 233, 10, 15, 12, 4, 169, 2, 7") 
print("")
Q2answer= "15" # right answer to question 2 
Q2response = input("your answer: ") 
if Q2response == "15" or Q2response == "fifteen": 
  print("great job! keep up the good work " + Q2response + " is correct")
  score= score+ 1
  
else:
   print("sorry, that answer is incorrect")
print("Your current score is " + str(score) + " out of 10 ") 
 
# question 3
print("Question 3: What is the probability of rolling a odd number on a six- sided dice? Leave in decimal form")
print("")
Q3answer = "0.5" # right answer to question 3
Q3response = input("your answer: ")
if Q3response == "0.5" or Q3response == "half":
    print("great job! keep up the good work "  + Q3response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 4
print("Question 4: if Mr. I flipped a coin 12 times and it comes up heads only 4 times, what would the cumulative relative frequency be? Leave in decimal form, round to the hundredths.")
print("")
Q4answer = "0.45" # right answer to question 4
Q4response = input("your answer: ")
if Q4response == "0.45" or Q4response == "forty five hundredths":
    print("great job! keep up the good work "  + Q4response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 5
print("Question 5: There are 10 pairs of sneakers being sold. 3 pair are the same sneaker. What is the probability? Leave in decimal forms and round to the tenths.")
print("")
Q5answer = "0.3" # right answer to question 5
Q5response = input("your answer: ")
if Q5response == "0.3" or Q5response == "three tenths":
    print("great job! keep up the good work "  + Q5response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 6
print("Question 6: What is the upper limit formula?")
print("")
Q6answer = "Q3+1.5(IQR)" # right answer to question 6
Q6response = input("your answer: ")
if Q6response == "Q3+1.5(IQR)" or Q6response == "q3+1.5(iqr)":
    print("great job! keep up the good work "  + Q6response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 7
print("Question 7: The mean is 20 for the history test and 64 for the math test and the standard deviation for both is 4. Amy scored a 64 on both of her test. Calculate the z-score. Which one has a better z-score?")
print("")
Q7answer = "History" # right answer to question 7
Q7response = input("your answer: ")
if Q7response == "History":
    print("great job! keep up the good work "  + Q7response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 8
print("Question 8: If you buy two calvin candy bars, what is the probability that they will both weigh between 2.6 ounces and 3 ounces? Leave in decimal form and round the ten-thousandths")
print("")
Q8answer = ".7172" # right answer to question 8
Q8response = input("your answer: ")
if Q8response == ".7172":
    print("great job! keep up the good work "  + Q8response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 9
print("Question 9: If you buy three unique candy bars, what is the probability that they will weigh less than three ounces? Leave in decimal form and round to the ten-thousandths")
print("")
Q9answer = ".7874" # right answer to question 9
Q9response = input("your answer: ")
if Q9response == ".7874":
    print("great job! keep up the good work "  + Q9response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

# question 10
print("Question 1: What is the formal name of the median of the entire data set?")
print("")
Q10answer = "" # right answer to question 10
Q10response = input("your answer: ")
if Q10response == "Second Quartile":
    print("great job! keep up the good work "  + Q10response + " is correct")
    score = score+ 1
else:
    print("sorry, that answer is incorrect")

print("Your current score is " + str(score) + " out of 10 ")

