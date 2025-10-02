word = "APPLE"
letter = input("Enter a letter: ")
if letter in word:
    print(f"{letter} is present in {word}")
else:
    print(f"{letter} is not present in {word}")