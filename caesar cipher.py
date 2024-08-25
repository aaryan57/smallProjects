alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("encode or decode\n").lower()
text=input("text\n").lower()
shift=int(input("Shift number\n"))
def encrypt(text,shift):
    cipher = ""
    for i in text:

        shifted=alphabet.index(i) + shift
        shifted%=26
        cipher+=alphabet[shifted]
    print(cipher)
def decrypt(cipher,shift):
    plane=""
    for i in cipher:
        shifted=alphabet.index-shift
        plane+=alphabet[shifted]
    print(plane)
if direction=='encode':
    encrypt(text,shift)
