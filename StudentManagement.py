# ----------Student Result Management System---------

students = []

def add_student():
    roll = input("Enter Roll No : ")
    for s in students:
       if s["roll"] == roll:
            print("Roll No already exists!")
            return

    name = input("Enter Name : ")
    n = int(input("How many subjects? : "))
    
    marks_list = []
    for i in range(n):
       m = int(input(f"Enter marks for Subject {i+1} : "))
    marks_list.append(m)

    total = sum(marks_list)
    average = total / n

    
    if average >= 90:
         grade = "A"
    elif average >= 75:
         grade = "B"
    elif average >= 50:
         grade = "C"
    else:
         grade = "D"

    
    status = "Pass" if average >= 35 else "Fail"

    student = {
         "roll": roll,
         "name": name,
         "marks": marks_list,
         "total": total,
         "average": average,
         "grade": grade,
         "status": status
     }
    students.append(student)
    print("Student Added Successfully!\n")
def display_all():
     if not students:
         print("No students found!\n")
         return
     for s in students:
         print("----- Student Report -----")
         print(f"Roll No : {s['roll']}")
         print(f"Name : {s['name']}")
         print(f"Marks : {s['marks']}")
         print(f"Total : {s['total']}")
         print(f"Average : {s['average']:.2f}")
         print(f"Grade : {s['grade']}")
         print(f"Result : {s['status']}")
         print("--------------------------\n")
def search_student():
     roll = input("Enter Roll No to search : ")
     for s in students:
         if s["roll"] == roll:
             print(f"\nFound -> {s['name']} | Total: {s['total']} | Avg: {s['average']:.2f} | Grade: {s['grade']} | {s['status']}\n")
             return
     print("Student not found!\n")

def highest_scorer():
     if not students:
         print("No data\n")
         return
     top = max(students, key=lambda x: x["total"])
     print(f"Highest Scorer : {top['name']} ({top['roll']}) - {top['total']} marks\n")
def lowest_scorer():
     if not students:
         print("No data\n")
         return
     low = min(students, key=lambda x: x["total"])
     print(f"Lowest Scorer : {low['name']} ({low['roll']}) - {low['total']} marks\n")

def class_average():
     if not students:
         print("No data\n")
         return
     class_avg = sum(s["average"] for s in students) / len(students)
     print(f"Class Average : {class_avg:.2f}\n")


while True:
     print("------ MENU ------")
     print("1. Add Student")
     print("2. Display All Reports")
     print("3. Search by Roll No")
     print("4. Highest Scorer")
     print("5. Lowest Scorer")
     print("6. Class Average")
     print("7. Exit")
    
     choice = input("Enter choice : ")

     if choice == "1":
         add_student()
     elif choice == "2":
         display_all()
     elif choice == "3":
         search_student()
     elif choice == "4":
         highest_scorer()
     elif choice == "5":
         lowest_scorer()
     elif choice == "6":
         class_average()
     elif choice == "7":
         break
     else:
         print("Invalid choice!\n")