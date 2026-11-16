users = []

def addusers():
      reg_no = int(input("Enter reg no :"))
      for user in users:
           if user["reg_no"] == reg_no:
             print("reg no already exist")
             return
           
      user = {}
      user["reg_no"] = reg_no      
      user["name"] = (input("Enter name :"))
      user["subjects"] = {}
      subjects = ["python","sql","excel","react"]

      for subject in subjects:
          marks = int(input(f"Enter {subject} marks :"))
          user["subjects"][subject] = marks
      users.append(user)
      print("User added successfully")
      

def diplayusers():
    for user in users:
          print("-----user details-----")
          print("reg_no :", user["reg_no"])
          print("name :", user["name"])   

          total = 0
          for subject,mark in user["subjects"].items():
            print(subject,":", mark)   
            total += mark

          avg = total / len(user["subjects"])

          if avg >= 90:
              grade = "A"
          elif avg >= 75:
              grade = "B" 
          elif avg >= 50:
              grade = "C"
          else:
              grade = "Fail"

          print("Total :",total) 
          print("Average :",avg)
          print("Grade :",grade)
          print("----------------------")

while True:
    print("------menu-----")
    print("1.add users")
    print("2.displayers")

    choice = int(input("Enter the choice :"))

    if choice == 1:
        addusers()
    elif choice == 2:
        diplayusers()   
    elif choice == 3:
        break