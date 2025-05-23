# Calculate final note of a student

import submodule.basic as sub

# placing a external module inside the path of sys module
import sys
sys.path.append("C:\\Users\\boss\\Documents\\PROJETOS\\PDM\\python\\utils")
import utils.functions as f

name = input("What is your name?\n")
sub.saudar(name)

school = input("Which school do you atttend?\n")
print("Good one!")

school_grades = input("Enter your of your school grades in math: ").split()
grades = map(float, school_grades)

finalNote = f.avg(list(grades))
print(f"Your final note is: {finalNote}! Congrats!")