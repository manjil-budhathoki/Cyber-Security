# 🚀 Cybersecurity CIA Triad & Caesar Cipher

## 🔒 CIA Triad (Confidentiality, Integrity, Availability)
The **CIA Triad** is the foundation of cybersecurity, ensuring secure, accurate, and accessible data.

### 🔹 **1. Confidentiality**
   - Protects data from unauthorized access.
   - **Tools & Techniques:**
     - **Encryption**: AES, RSA, ECC
     - **Access Control**: RBAC, MAC
     - **VPNs**, **Steganography**

### 🔹 **2. Integrity**
   - Ensures data remains unchanged unless modified by authorized parties.
   - **Tools & Techniques:**
     - **Hashing**: SHA-256, MD5, HMAC
     - **Digital Signatures**: RSA, ECDSA
     - **File Integrity Monitoring**: Tripwire, OSSEC

### 🔹 **3. Availability**
   - Ensures authorized users can access data when needed.
   - **Tools & Techniques:**
     - **Redundancy**: RAID, Load Balancers
     - **Backup Strategies**: Incremental, Differential
     - **DDoS Protection**: Cloudflare, AWS Shield

---

## 🔑 Caesar Cipher: Simple Encryption Technique
The **Caesar Cipher** is a substitution cipher that shifts letters in the alphabet by a fixed number.

### 📌 **How it Works?**
1. Choose a shift value (e.g., `shift = 3`).
2. Replace each letter with the letter found `X` places later in the alphabet.
   - Example with `shift = 3`:
     - A → D, B → E, C → F, ..., X → A, Y → B, Z → C

### 📌 **Example of Encryption & Decryption**
```python
# 📝 Python Code for Caesar Cipher

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
```

## 🔥 Summary
✅ **CIA Triad** ensures **security, accuracy, and availability** of data.<br>
✅ **Caesar Cipher** is a simple, yet foundational encryption technique.<br>
✅ Python code and visualization help understand encryption better.<br>

