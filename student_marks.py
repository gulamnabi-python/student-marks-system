#Student Marks Management System
print("===Student Marks Systemte==")

#Input student details.
name=input("Enter student name:")
roll_no=input("Enter roll number:")

#Input marks
maths=int(input("Enter Maths marks:"))
science=int(input("Enter Science marks:"))
english=int(input("Enter English marks:"))

#calculate total and average
total=maths+science+english
average=total/3

#Display result
print("\n---Student Report---")
print("Name:",name)
print("Roll No:",roll_no)
print("Total Marks:",total)
print("Average:",average)

#Pass/Fail condition.
if average>=35:
    print("Result:PASS")
else:
    print("Result:FAIL")
