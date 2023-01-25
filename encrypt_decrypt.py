# import the caesar clipher art logo and OS library
import os
import art

# Defining a clear function for clearing screen 
def clear():
    os.system('cls')

# A list containing alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function for caesar encryption and decryption
def caesar(message, shift, direction):

    secret_msg = ""

    # loop through every letter in input message 
    for charac in message:

        # check if the letter from input message is in alphabet or not
        if charac in alphabet:

            # Getting the index of letter from input message in alphabet 
            position = alphabet.index(charac)

            # check if the user want encryption or decryption 
            # check if the direction is encode or not
            if direction == 'encode':

                # Add the shifting position index with letter in message position 
                new_shift = position + shift

                # Add the encrypted letter from alphabet to secret message 
                secret_msg += alphabet[new_shift]
            
            # check if the direction is decode or not
            elif direction == 'decode':

                # Substract the shifting position index with letter in message position 
                new_shift = position - shift

                # Add the decrypted letter from alphabet to secret message 
                secret_msg += alphabet[new_shift]

        # If letter does not exist in alphabet simply add it without modification 
        else:
            secret_msg += charac
    
    # Output the encrypted or decrypted message 
    print(f"Here's the {direction}d result: {secret_msg}")


end = True

# Run the function untill end become false 
while end:
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # if shift value is greater than 26 
    shift %= 26

    # calling caesar function 
    caesar(message=text, shift=shift, direction=direction)

    # If encrypted or decrypted once, then asked again if user want to use it or not 
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    # if user input 'no' then end becomes false and program end with good bye message 
    if run_again == 'no':
        end = False
        print("Bye!")
    elif run_again == 'yes':
        clear()
