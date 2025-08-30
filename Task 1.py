students={"akash":54,"shubham":99,"paul":77,"pooja":86,"akshita":84,"sarthak":33}
x=input("Enter the student's name:")
if x in students:
     print(f"{x}'s Marks: {students[x]}")
else:
     print("student not found")


