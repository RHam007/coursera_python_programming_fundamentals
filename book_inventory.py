books = ["The Hitchhiker's Guide to the Galaxy", "Pride and Prejudice", "To Kill a Mockingbird"]
status = ["available", "available", "checked out"]

#for book in range(min(len(books), len(status))):
#    print(books[book], status[book])

for book in range(min(len(books), len(status))):
    if books[book] == "Pride and Prejudice": #if the selected book's status is available, set the status to "checked out"
        print(books[book], status[book]) #print statement to verify current status
        if status[book] == "available":
            status[book] = "checked out"
        print(books[book], status[book]) #print statement to verify status change
