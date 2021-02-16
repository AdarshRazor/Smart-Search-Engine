# importing the module 
import wikipedia 
import os
import time
# clearing the screen for better view.
os.system('cls')

Topic = (input("Enter the search: ").capitalize())
# finding result for the search 
# sentences = 2 refers to numbers of line 
result = wikipedia.summary(Topic, sentences=1) 
Word_Tagging = wikipedia.search(Topic)

# # printing the result 
print("\n",Topic,"\n","\n",result,"\n")

# storing word tagged data in file
'''file_thing = open("{}.txt".format(Topic), "w")
for x in Word_Tagging:
    file_thing.write(x + "\n")'''

# file_thing = open("{}.txt".format(Topic), "r")
# Related= input("Want to see realted results ? (Y/N): ")
# if Related == "Y":
#     print("Related Topics:\n",file_thing.read())
#     file_thing.close()

# chunking the tagged word for better result.

# exiting the program
time.sleep(1)
os.system("cls")
print("Thank You for using SSE !\nFor any query: adarshanshu7@gmail.com")
time.sleep(3)