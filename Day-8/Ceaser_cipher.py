# encryption algorithm
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


def ceaser(message, k, cipher_direction):
    end_text = ""
    sign = 1
    if cipher_direction == "encode":
        sign = -1

    for i in range(0, len(message)):
        if message[i] in alphabet:
            end_text += alphabet[(alphabet.index(message[i]) - (sign) * k) % 26]
        else:
            end_text += message[i]
    print(f"The {cipher_direction}ed text is {end_text}")


# def encrypt(message, k):
#     cipher_text = ""
#     for i in range(0, len(message)):
#         cipher_text += alphabet[(alphabet.index(message[i]) + k) % 26]
#     return cipher_text
#
#
# def decrypt(cipher_text, k):
#     message = ""
#     for i in range(len(cipher_text)):
#         message += alphabet[(alphabet.index(cipher_text[i]) - k) % 26]
#     return message


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26

    # if direction == "encode":
    #     cipher_text = encrypt(text, shift)
    #     print(f"The encoded text is {cipher_text}")
    # else:
    #     message = decrypt(text, shift)
    #     print(f"The decoded message is {message}")

    ceaser(text, shift, direction)
    result = input("Yes to continue, No to exit:\n")
    if result == "No":
        should_continue = False
