from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
  caesar_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in plain_text:
    if letter not in alphabet:
      caesar_text += letter
    else:
      new_position = (alphabet.index(letter) + shift_amount) % 26
      caesar_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {caesar_text}")

print(logo)

should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  choice = input("Type 'yes' if you want to go again. Otherwise type 'no.'\n").lower()
  if choice != "yes":
    print("Goodbye!")
    should_end = True
  else:
    os.system("clear")
