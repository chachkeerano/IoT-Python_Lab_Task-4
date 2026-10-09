students = ["Ali", "Ahmed","Chach", "Sara", "Ayesha", "Bilal"]

name = input("Enter a student name: ").strip().capitalize()

if name in students:
    print("Student Found")

else:
    print("Student Not Found")