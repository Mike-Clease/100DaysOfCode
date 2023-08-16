from CipherArt import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(start_text, text_shift, cipher_direction):
    """
    Takes an input string (text) and encrypts it by
    shifting the letters in the alphabet by (shift).
    """
    output_text = ''

    if cipher_direction == 'decode':
        text_shift *= -1

    for letter in start_text:
        if letter in alphabet:
            i = alphabet.index(letter)
            shifted = i + text_shift         
            output_text += alphabet[shifted]
        else:
            output_text += letter

    return output_text


keep_going = True
print(logo)

while keep_going:
 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    text = encrypt(start_text=text, text_shift=shift, cipher_direction=direction)
    
    print(f"The {direction}d text if {text}.")

    rerun = input("Would you like to try again? ")
    
    if rerun == 'No':
        keep_going = False
        print("Goodbye")


 