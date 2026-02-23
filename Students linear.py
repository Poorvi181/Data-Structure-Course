students = ["Nameerah", "Poorvi", "Ava", "Swara"]
target = input("Enter the student name you want to search: ")

found = False

for name in students:
    if name == target:
        print("Student Found")
        found=True
        break

if not found:
    ("Element not found!")