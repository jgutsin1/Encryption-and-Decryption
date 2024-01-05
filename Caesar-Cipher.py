def encrypt(pt, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ct = ""
    for c in pt.lower():
        for i in range(0, len(alphabet)):
            if(c == alphabet[i]):
                ct += alphabet[(i + shift) % 26]
                break
            elif i == len(alphabet) - 1:
                pt += c
                break
    return ct.upper()
            

def decrypt(ct, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pt = ""
    for c in ct.lower():
        for i in range(0, len(alphabet)):
            if(c == alphabet[i]):
                pt += alphabet[(i - shift) % 26]
                break
            elif i == len(alphabet) - 1:
                pt += c
                break
    return pt.lower()

type = input("Do you want to encrypt or decrypt? Type e for encrypt, d for decrypt: ")
if type == "e":
    pt = input("Please enter the plain text message: ")
    shift = input("Please enter the shift as a number: ")
    ct = encrypt(pt, int(shift))
    print("Your encrypted text is", ct)
elif type == "d":
    ct = input("Please enter the cipher test message: ")
    shift = input("Please enter the shift as a number: ")
    pt = decrypt(ct, int(shift))
    print("Your decrypted text is", pt)
else:
    print("Incorrect input")
 