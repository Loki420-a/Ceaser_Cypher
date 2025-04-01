
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']
condition = False

def ceaser(original_text, shift_amount, direction):
    cypher_text = ""  

    if direction == "decode":
        shift_amount = -shift_amount 

    for letter in original_text:
        if letter not in alphabets:
            cypher_text += letter  # Add non-alphabet characters as is
            continue
        value = alphabets.index(letter) + shift_amount
        value %= len(alphabets)  # Ensures circular shift
        cypher_text += alphabets[value]
    
    print(f"Here is the {direction}d result: {cypher_text}.")  # Moved outside the loop

while not condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt the message\n").lower()  
    text = input("Enter the message\n").lower()
    shift = int(input("Type the shift number.\n"))

    ceaser(text, shift, direction)

    cont_condition = input("Press 'yes' if you want to continue again and 'no' to exit.\n").lower()

    if cont_condition != 'yes':
        condition = True




