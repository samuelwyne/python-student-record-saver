with open("student.txt","w")as file:
    for i in range(5):
     name=input("Enter student name: ")
     while True:
        try:
           marks=int(input("Enter student's marks: "))
           if marks>0:
              break
           else:
              print("Enter correct marks: ")
        except ValueError:
           print("Enter correct marks: ")      
     file.write(f"{name}-{marks}\n")
with open("student.txt","r")as file:
   print(f"{"="*5}student records{"="*5}")
   

   for line in file:
       print(line.strip())