# DAY 20 – FILE HANDLING (TEXT FILES)


# # # 1) Reading full file
# with open("sample.txt", "r") as f:
#     print(f.read())



# # 2) Reading line by line
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip().title())



# # 3) Writing (overwrite)
# with open("notes.txt", "w") as f:
#     f.write("Day 20 - File Handling\n")
#     f.write("Learning read and write.\n")



# # # 4) Appending
# with open("notes.txt", "a") as f:
#     f.write("Appending new line.\n")




# # 5) Cleaning data in file
# cleaned = []
# with open("sample.txt", "r") as f:
#     for line in f:
#         cleaned.append(line.strip().title())  
# with open("cleaned_output.txt", "w") as f:
#     for city in cleaned:
#         f.write(city + "\n")



# # 6) Counting lines
# count = 0
# with open("sample.txt", "r") as f:
#     for _ in f:
#         count += 1
# print("Total Lines:", count)
 




#  preactices 
# 1. SOLUTION (Python Program Answer)

security_code = int(input("Enter the security code: "))

if security_code == 5566:
    department = input("Enter your department: ")

    if department.lower() == "finance":
        access_level = int(input("Enter your access level: "))

        if access_level >= 5:
            print("Access Granted: Welcome to the meeting room.")
        else:
            print("Insufficient access level.")
    else:
        print("Access denied: Department not allowed.")
else:
    print("Invalid security code.")


# ASSIGNMENT SET 2 — Online Exam Login

reg = int(input("Enter registration number: "))

if reg == 1221:
    subject = input("Enter exam subject: ")

    if subject.lower() == "python":
        password = int(input("Enter exam password: "))

        if password == 8888:
            print("Login successful! Start your exam.")
        else:
            print("Wrong password.")
    else:
        print("Subject not available.")
else:
    print("Registration failed.")
