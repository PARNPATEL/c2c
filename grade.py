sub_1 = int(input("enter the mark od subject_1")) 
sub_2 = int(input("enter the mark od subject_2"))
sub_3 = int(input("enter the mark od subject_3"))
sub_4 = int(input("enter the mark od subject_4"))
sub_5 = int(input("enter the mark od subject_5"))

sum= sub_1 + sub_2 + sub_3 + sub_4 + sub_5
total = 500
grade= sum*100/total

if (grade > 90 and grade <=100):
    print ("grade A+") 
elif (grade > 80 and grade <=90):
  print("grade B")
elif (grade > 75 and grade <=80):
     print("grade c")
elif(grade >0 and grade <75):
    print ("grade f")
else:
    print("enter valid marks ")
