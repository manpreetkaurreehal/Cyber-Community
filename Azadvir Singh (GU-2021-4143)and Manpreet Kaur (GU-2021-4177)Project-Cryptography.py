import pyfiglet as p
print(p.figlet_format("CEASER CIPHER", ))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"THE {cipher_direction}d VERSION OF ENTERED MESSAGE : \n{end_text}\n\n")
end= False
while not end:
  direction = input("ENTER [encode] TO ENCRYP \nENTER [decode] TO DECRYPT\n")
  if direction == "decode":
    print(p.figlet_format("DECODER"))
  else:
    print(p.figlet_format("ENCODER"))
  text = input("\nTYPE YOUR MESSAGE: ").lower()
  shift = int(input("\nENTER SHIFT NUMBER: "))

  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("\n\nDO YOU WANT TO TRY AGAIN [yes/no]\n")
  if restart == "no":
    end = True
    print(p.figlet_format("GOOD BYE"))