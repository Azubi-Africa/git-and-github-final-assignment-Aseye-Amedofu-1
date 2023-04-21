cipher_text = "BYZAXCDEFGHIJKLMNOPQRSTUVW"
    
    
text = input("Enter cipher message: ").upper()
#s defines the shift count
S = int(input("Choose the shift code: "))

decrypted = str()

# transverse the cipher text
for i in text:
    updated_position = (cipher_text.find(i)+S) % 26
    decrypted += cipher_text[updated_position]

print(decrypted)

# Author
# Samuel Aseye Amedofu