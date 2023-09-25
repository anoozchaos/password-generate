#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import random

# Getting password length from the user
length = int(input("Enter password length: "))

# Define character sets
characterList = ""

# Getting character set for password
print('''Choose character set for password from these:
          1. Digits
          2. Letters
          3. Special characters
          4. Exit''')

while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        # Adding digits to possible characters
        characterList += string.digits
    elif choice == 2:
        # Adding letters (both uppercase and lowercase) to possible characters
        characterList += string.ascii_letters
    elif choice == 3:
        # Adding special characters to possible characters
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Pick a valid option")

# Generating the password
password = []

for i in range(length):
    # Pick a random character from our character list
    randomChar = random.choice(characterList)

    # Appending a random character to the password
    password.append(randomChar)

# Printing the password as a string
print("The random password is " + "".join(password))



# In[2]:





# In[ ]:



            


# In[16]:







# In[ ]:





# In[ ]:





# In[ ]:




