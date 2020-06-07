from pathlib import Path
from time import sleep

# giving no args when you initialize a new path object just takes the current path
curr_path = Path()
print(curr_path.exists())
for file in curr_path.glob("*.py"): # use glob to file all files that follow a certain pattern & iterate over them
  print(file)

print("-"*50)

# giving a string arg of the folder name searches for that path and stores it as a path instance
animezon = Path("Animezon")
print(animezon.exists()) # false bc it can only find paths deeper than it, can't go out
print("-"*50)

# giving a string arg of the folder name searches for that path and stores it as a path instance
test_folder = Path("test_folder")
print(test_folder.exists()) # false bc it does not exist
test_folder.mkdir() # creates a folder at the level that the terminal is at when the function is called
print(test_folder.exists())  # true bc it was created
sleep(3)
test_folder.rmdir()
print(test_folder.exists())  # false bc it was deleted
print("-"*50)