txt = input("sample text:")
txt = txt.replace(" ","").lower()

if txt[::-1] == txt:
    print("Palindrome")
else:
    print("not Palindrome")

