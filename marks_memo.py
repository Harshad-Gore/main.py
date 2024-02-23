#python program to find percentage of marks in five subjects.
phy=float(input("Enter marks of PHYSICS.\n"))
chem=float(input("Enter marks of CHEMISTRY.\n"))
math=float(input("Enter marks of MATHS.\n"))
bio=float(input("Enter marks of BIOLOGY.\n"))
eng=float(input("Enter marks of ENGLISH.\n"))
cgpa = (phy+chem+math+bio+eng)/5
if (phy<=100 and chem<=100 and math<=100 and bio <=100 and eng<=100):
    while (phy<=100 and chem<=100 and math<=100 and bio <=100 and eng<=100):
        if(cgpa>=75):
            print("Distinction.\n CGPA :",cgpa)
        elif(cgpa>=65 and cgpa<75):
            print("First Class.\n CGPA :",cgpa)
        elif(cgpa>=55 and cgpa<65):
            print("Second Class.\n CGPA :",cgpa)
        elif(cgpa>=45 and cgpa<55):
            print("Third Class.\n CGPA :",cgpa)
        elif(cgpa>=35 and cgpa<45):
            print("Forth Class.\n CGPA :",cgpa)
        else:
            print("Fail")
        break
else:
    print("Enter valid marks.(Between 1 to 100)\n")