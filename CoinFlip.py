import random
#Ask user how many flips and store it in variable 
num_flips = int(input("How many times would you like to flip the coin "))

#Run num_flip tests and if the result is Heads, add one to the tally
total_heads = 0
total_tails = 0
for i in range (num_flips):
    result = random.choice(["Heads", "Tails"])
    if result == "Heads":
        total_heads +=1
    else:
        total_tails +=1
#Print the expected and the experimental values
experimental_heads = total_heads / num_flips
experimental_tails = total_tails / num_flips

print ("Expected Heads = .5000")
print (f"Experimental Heads = {experimental_heads:.4f}")
print("Expected Tails = .5000")
print (f"Experimental Tails = {experimental_tails:.4f}")

