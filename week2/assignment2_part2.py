# Create a new python file called assignment1_part2.py. All code for this part should be in this file and eventually pushed to Github.
# Create a class called Book. The class should have the following properties:
#     Two attributes, author and title, both of which should be initialized to the blank string
#     An __init__ function that takes in an author and a title, and sets them to the object variables
#     A function called display(), which when called, simply prints out a string representing the book. The output should be in the form of “title, written by author”. Example: “Of Mice and Men, written by John Steinbeck”.

# Print both of these objects to the screen by calling their display() functions
# Once this is completed, run a ‘git status’ command. This should indicate to you that there is a file called assignment1_part2.py that is not in the repository yet. Run the correct git command to add this file to the repository.
# Once that is done, commit this change (to the default master) using ‘git commit’.
# Push this commit to the ‘origin’ using git push, which is Github in this case.

class Book:
    author = ""
    title = ""

#     An __init__ function that takes in an author and a title, and sets them to the object variables
    def __init__(self, author, title):
        self.author = author
        self.title = title

#     A function called display(), which when called, simply prints out a string representing the book. The output should be in the form of “title, written by author”. Example: “Of Mice and Men, written by John Steinbeck”.

    def display(self):
        print(f"{self.title}, written by {self.author}")

# Instantiate two objects from this class. The first object represents the book Harry Potter and the Goblet of Fire, written by J. K. Rowling; the other is Ivanhoe: A Romance by Walter Scott.
book1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Print both of these objects to the screen by calling their display() functions

book1.display()
book2.display()

# Once this is completed, run a ‘git status’ command. This should indicate to you that there is a file called assignment1_part2.py that is not in the repository yet. Run the correct git command to add this file to the repository.
# Once that is done, commit this change (to the default master) using ‘git commit’.
# Push this commit to the ‘origin’ using git push, which is Github in this case.

