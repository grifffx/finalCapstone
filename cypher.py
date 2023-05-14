
# This cypher uses for example the 15th letter after each letter in a sentence.
# For example, ‘a’ will be ‘p’. Letters are treated as cyclical meaning ‘p’ will be coded to ‘e’ (the 10th letter after ‘p’ is ‘z’,
# so 5 letters after that will be ‘e’ because the cycle starts again).


# Please note I am using IDLE 3.11.2 on Mac OS

import sys
from pathlib import Path

# Function to encrypt a sentence

def cypher (text,shift):
    
    new_text = ""
    
    for character in text:

        # Convert character to ascii
        
        ascii = ord(character)
        new_ascii = ascii

        # If character is upper case apply shift value. Shift value can be positive or negative

        if ascii >= 65 and ascii <= 90:

            new_ascii = ascii + shift

            if new_ascii > 90:

                new_ascii =  new_ascii - 26

            elif new_ascii < 65:

                new_ascii = new_ascii + 26

        # If character is lower case apply shift value. Shift value can be positive or negative

        elif ascii >= 97 and ascii <= 122:

            new_ascii = ascii + shift

            if new_ascii > 122:

                new_ascii = new_ascii - 26

            elif new_ascii < 97:

                new_ascii = new_ascii + 26        

        new_text = new_text + chr(new_ascii) # Convert ascii value back to a character and append to the new text string

    return new_text    

####################################################################

# Function to read sentences from a text file

# Get file name

def read_from_file ():

    file_name = input("Enter file name: ")
    path = Path(file_name)
    file_name_doesnt_exist = True
    
    while file_name_doesnt_exist:
        
        if path.is_file():
            
            print ("Reading sentences from file")
            print (" ")
            print ("Encrypted sentences")
            print (" ")
            
            with open(file_name, 'r') as f:

                # Read each sentence from file and call cypher function to encrypt it
                
                for line in f:
                    
                    print (cypher(line,cypher_shift), end='')
                    print (" ")
                    
                file_name_doesnt_exist = False
        else:

            print ("ERROR file does not exist")
            file_name = input("Enter file name: ")
            path = Path(file_name)

####################################################################
            
# Function to get cypher shift value

# Get positive or negative cypher shift value. For example 15. User can either provide a file containing sentences or enter a sentence

def get_cypher_shift_value():

    cypher_shift_value = 20

    while cypher_shift_value <= -20 or cypher_shift_value >= 20:

        while True:

            try:
                cypher_shift_value = int(input ("Enter cypher shift value between -20 and 20: "))
                break
            except ValueError:
                print ("Invaid input")
                       
        if cypher_shift_value <= -20 or cypher_shift_value >= 20:
            print ("Value out of range")
    return cypher_shift_value           


#####################################################################

# Get cypher shift value

cypher_shift = get_cypher_shift_value()
             
# User can either provide a text file containing sentences to encrypt or enter a sentence manually

input_type = input ("Do you want to read sentences from a file? Y/N: ")

if input_type == "Y" or input_type == "y":
    
    read_from_file()
    print (" ")
    print ("****** DONE *******")
   
else:
    print (" ")

    text_input = input ("Enter sentence: ")

    print ("Encripting Sentence")

    line = cypher(text_input,cypher_shift)

    # A bit of fun on the screen
    
    for i in range(len(line)):

      for j in range(5):

        print(line[:i], (4-j)*" ",

          line[i],j*" ", line[i+1:])

    print (line)
    
    print (" ")
