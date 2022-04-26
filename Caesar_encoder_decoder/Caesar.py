from art import logo
print(logo)

def encrypt(text, shift) :
    cipher_text = ''
    if shift > 26 :
        shift = shift % 26
    for i in text :
        if i.isalpha() == True :
            temp = ord(i) + int(shift)
            if temp > 122 :
                temp -= 26 
            cipher_text += chr(temp)
        else :
            cipher_text += i
    print(f"The encoded text is {cipher_text}.")

def decrypt(text, shift) :
    cipher_text = ''
    if shift > 26 :
        shift = shift % 26
    for i in text :
        if i.isalpha() == True :
            temp = ord(i) - int(shift)
            if temp < 97 :
                temp += 26 
            cipher_text += chr(temp)
        else :
            cipher_text += i
    print(f"The decoded text is {cipher_text}.")

go_ahead = True
while go_ahead :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction.lower() == "encode"  :
        encrypt(text, shift)
    elif direction.lower() == "decode" :
        decrypt(text, shift)
    else :
        print("wrong order")

    typing = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.")
    if typing.lower() == 'no' :
        go_ahead = False
        print("Goodbye")