'''import csv
data = [
    ["Name" , "Age", "City"],
    ["Rinki" , 14, "Vadodara"],
    ["Rimi",19,"Surat"],
    ["Khush",18,"Kim"]
]

filename = "Student.csv"
with open(filename, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' has been created successfully!")



f = open("C:\\Users\\lab\\Desktop\\Student.csv", "a")
f.write("roll No., Name,CPII,Mathsll,Physics,\n")
Roll_No = input("Enter Your Roll No.[Press enter to Quit]")
while Roll_No:
    nm = input("Enter your name:")
    c, m,p = input("Enter marks of Chemistry,Maths,Physics:").split(" ")
    f.write(Roll_No+","+nm+","+c+","+m+","+p+"\n")
    Roll_No = input("Enter Your roll no. [Press enter to Quit]")
    f.close()

import csv

with open("C:\\Users\\lab\\Desktop\\Student.csv", "a", newline = " ")as f:
    writer = csv.writer(f)
    writer.writerows(["Name", "Roll No.", "CPII"])
    writer.writerows(["Parth","24BEC073", "20"])'''

f = open("C:\\Users\\lab\\Desktop\\Student.csv", "r")
a = f.readline()
while a:
    Roll_No, nm, cp2, maths2, phy

