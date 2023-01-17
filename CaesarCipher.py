print("""
 #####     #    #######  #####     #    ######      #####  ### ######  #     # ####### ######  
#     #   # #   #       #     #   # #   #     #    #     #  #  #     # #     # #       #     # 
#        #   #  #       #        #   #  #     #    #        #  #     # #     # #       #     # 
#       #     # #####    #####  #     # ######     #        #  ######  ####### #####   ######  
#       ####### #             # ####### #   #      #        #  #       #     # #       #   #   
#     # #     # #       #     # #     # #    #     #     #  #  #       #     # #       #    #  
 #####  #     # #######  #####  #     # #     #     #####  ### #       #     # ####### #     # 
 """)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
should_continue = True


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the number that each character will be shifted by: \n"))
        shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        result = input("Type 'yes' if you want to go again. Otherwise exit with 'no': ")
        if result == "no":
            should_continue = False
            print("Goodbye")
    else:
        direction = input("Invalid entry, only type 'encode' to encrypt, or type 'decode' to decrypt: \n").lower()
