######################################
#   This is a simple test file to ensure the 
#   RiddlerClient works properly. 
#
#   Add in your old tests to be confident 
#   each of your RiddlerClient methods work
######################################

from riddle_client import RiddleClient

riddler_client = RiddleClient()

print("--- TEST ALL RIDDLES ---")

riddle_list = riddler_client.all_riddles()

for riddle in riddle_list:
    print(riddle)

print()

#############

print("--- TEST GUESS RIDDLES ---")

id = 17
guess = "to get to the other side"
guess_riddle_message = riddler_client.guess_riddle(id,guess)


print(guess_riddle_message)

print()