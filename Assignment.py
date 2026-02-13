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
