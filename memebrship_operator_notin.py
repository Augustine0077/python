word = "APPLE"
letter = input("Enter a letter: ")
if letter not in word:
    print(f"{letter} is not present in {word}")
else:
    print(f"{letter} is present in {word}")