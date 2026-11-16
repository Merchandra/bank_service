import random
point = 0
count=0
while count < 3:
  print("-----menu-----")
  print("1.stone")
  print("2.paper")
  print("3.scissor")

  choice=int(input("enter the choice:"))

  if choice not in [1,2,3]:
      print("invalid choice")
  computer = random.choice(["stone","paper","scissor"])

  print("choice:",choice)
  print("computer:",computer)



  if choice ==1 and computer =="scissor" or choice ==2  and  computer =="stone" or choice==3 and computer =="paper":



     print("user win ")
     point+=1

  elif choice ==1 and computer =="paper" or choice ==2 and computer == "scissor" or computer =="stone":

      print("user lose")

  else:

   print("draw")
   print("point:",point)
   count+=1


