class Caeser:
  
  def __init__(self, shift):
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

  def encrypt(self, message, key):
    result = ''
    for i in message:
      if i in self.alphabet:
        result += self.alphabet[(self.alphabet.index(i) + key) % 26]
      else:
        result += i
    return result
  
  def decrypt(self,cipher, key):
    result = ''
    for i in cipher:
      if i in self.alphabet:
        result += self.alphabet[(self.alphabet.index(i)- key) % 26] 
      else:
        result += i
    return result  
  
message = input("Enter the your Message to Encrypt: ")
cipher = Caeser(3)

while True:
  print("1. Encrypt")
  print("2. Decrypt")
  print("3.Exit")
  choice = input("Enter your choice: ")
  if choice == '1':
    encrypted_message = cipher.encrypt(message, 3)
    print("Encrypted Message: ", encrypted_message)
  elif choice == '2':
    if encrypted_message is None:
      print("Please encrypt the message first")
    else:
      decrypted_message = cipher.decrypt(encrypted_message,3)
      print("Decrypted Message: ", decrypted_message)
      
  elif choice == '3':
    print("Exiting...")
    break 
    
    
