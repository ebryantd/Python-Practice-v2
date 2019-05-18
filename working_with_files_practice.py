"""
st = open("D:\FilePractice\FileSubPractice\PythonPracticeFile.txt", "w+")
for i in range(1, 100):
    st.write(str(i)+","+str(i*10)+"\n")
st.close()    
"""
"""
with open("D:\FilePractice\FileSubPractice\PythonPracticeFile.txt", "w+") as st:
    for i in range(1, 100):
        st.write(str(i)+","+str(i*-10)+"\n")
"""
"""
my_list = list()

with open("D:\FilePractice\FileSubPractice\PythonPracticeFile.txt", "r") as st:
    my_list.append(st.read())

for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i])
    i += 1
"""

import csv
"""
with open("D:\FilePractice\FileSubPractice\PythonPracticeFile.csv", "w+", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in range(1, 100):
        w.writerow([i,i**2,i**3])
"""    

with open("D:\FilePractice\FileSubPractice\PythonPracticeFile2.csv", "a", newline='') as f:
    w = csv.writer(f, delimiter=",")
    firstname = input("What is your first name?:")
    lastname = input("What is your last name?:")
    age = input("What is your name?:")
    w.writerow([firstname,lastname,age])
