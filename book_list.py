books = []
while True:
    book = input("Enter a book name (enter q to quit): ")
    if book.lower() == "q":
        break
    books.append(book)
print("Books you entered:")
for b in books:
    print(b)