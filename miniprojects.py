students=[]
count=0

while True:

    print("------MENU----")
    print("1.Add student")
    print("2.Display student report")
    print("3.Search student")
    print("4.Highest scores")
    print("5.Lowest scores")
    print("6.Class average")
    print("7.Exit")


    choice=int(input("enter the choice:"))

    if choice==1:
        name=input("enter student name:")
        roll_number=int(input("enter roll number:"))

        marks=[]
        subjects=["Tamil","English","Maths","Science","Social"]

        for i in subjects:
            mark=int(input(f" enter {i} mark :"))
            marks.append(mark)

        total=sum(marks)
        average=total/len(subjects)

        if average>=90:
            grade="A"
        elif average>=80:
            grade="B"
        elif average>=70:
            grade="C"
        elif average>=50:
            grade = "D"
        else:
            grade = "F"

        if all(mark >= 35 for mark in marks):
            result = "PASS"
        else:
            result = "FAIL"

        student = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade,
            "result": result
        }

        students.append(student)
        count += 1

        print("student added successfully")

    elif choice == 2:

        for student in students:
         print("------ STUDENT REPORT ------")
         print("name :", student["name"])
         print("roll number :", student["roll_number"])
        print("marks :", student["marks"])
        print("total :", student["total"])
        print("average :", student["average"])
        print("grade :", student["grade"])
        print("result :", student["result"])

    elif choice == 3:

        roll_number = int(input("enter roll number :"))
        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                print("name :", student["name"])
                print("marks :", student["marks"])
                print("total :", student["total"])
                print("average :", student["average"])
                print("grade :", student["grade"])
                print("result :", student["result"])
                found = True
                break

        if found == False:
            print("student not found")

    elif choice == 4:

        if count > 0:
            highest = max(students, key=lambda s: s["total"])
            print("highest scorer :", highest["name"])
            print("total :", highest["total"])
        else:
            print("no students available")

    elif choice == 5:

        if count > 0:
            lowest = min(students, key=lambda s: s["total"])
            print("lowest scorer :", lowest["name"])
            print("total :", lowest["total"])
        else:
            print("no students available")

    elif choice == 6:

        if count > 0:
            class_total = 0

            for student in students:
                class_total += student["average"]

            class_average = class_total / count
            print("class average :", class_average)
        else:
            print("no students available")

    elif choice == 7:
        print("Thank you")
        break

    else:
        print("invalid choice")
            