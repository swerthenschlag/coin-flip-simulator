import random
#Ask user how many flips and store it in variable 
num_flips = int(input("How many times would you like to flip the coin "))

#Define the total tallys and define the terms to calculate the longest streaks
total_heads = 0
total_tails = 0
longest_streak = 0
current_streak = 0
previous_result = None
#Set up flipping loop
for i in range (num_flips):
    result = random.choice(["Heads", "Tails"])
    if result == "Heads":
        total_heads +=1
    else:
        total_tails +=1
#Set up longest streak tracker
    if previous_result == result:
        current_streak += 1
    else:
        current_streak = 1
    if current_streak > longest_streak:
        longest_streak = current_streak

    previous_result = result

#Print longest streak
print(f"longest_streak = {longest_streak}")



#Print the expected and the experimental values
experimental_heads = total_heads / num_flips
experimental_tails = total_tails / num_flips

print ("Expected Heads = .5000")
print (f"Experimental Heads = {experimental_heads:.4f}")
print("Expected Tails = .5000")
print (f"Experimental Tails = {experimental_tails:.4f}")

