# Q1. An e-commerce store stores information about its products in a nested dictionary.The outer dictionary uses product IDs as keys, and the inner dictionary stores product 
# details like name, category, price, and stock quantity.products = { 101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50}, 102: 
# {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200}, 103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30} }

# • Increase the stock of the "Shirt" product (add 50 more units) using increment/decrement operators
# • Add a new product (e.g., "Smartphone")


products = { 
    101: {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 50}, 
    102: {"name": "Shirt", "category": "Apparel", "price": 25, "stock": 200}, 
    103: {"name": "Coffee Maker", "category": "Home Appliances", "price": 80, "stock": 30}
     }
products[102]["stock"] += 50
print(products)
products[104] = {"name": "Smartphone", "category": "Electronics", "price": 800, "stock": 100}
print(products) 

# Q2. A library management system uses a nested dictionary to store information about books. The outer dictionary uses ISBN numbers as keys, and the inner dictionary stores book
# details like title, author, genre, and availability status. books = { "978-3-16-148410-0": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction",
# "available": True}, "978-0-14-118263-6": {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "available": False},
# "978-0-452-28423-4": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "available": True} }          
# • Change the availability status of "1984" to True using logical operators
# • Add a new book to the library   
books = { 
    "978-3-16-148410-0": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "available": True}, 
    "978-0-14-118263-6": {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "available": False},
    "978-0-452-28423-4": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "available": True} 
    }       
books["978-0-14-118263-6"]["available"] = True
print(books)
books["978-1-56619-909-4"] = {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "available": True}
print(books)

# Q3. A student management system uses a nested dictionary to store information about students. The outer dictionary uses student IDs as keys, and the inner dictionary stores
# student details like name, age, grade, and attendance percentage. students = { 201: {"name": "Alice", "age": 20, "grade": "A", "attendance": 95}, 202: {"name": "Bob", "age": 22, "grade": "B", "attendance": 85},
# 203: {"name": "Charlie", "age": 21, "grade": "C", "attendance": 90} }
# • Increase the attendance percentage of "Bob" by 5% using increment/decrement operators
# • Add a new student to the system
students = {
     201: {"name": "Alice", "age": 20, "grade": "A", "attendance": 95},
     202: {"name": "Bob", "age": 22, "grade": "B", "attendance": 85},
     203: {"name": "Charlie", "age": 21, "grade": "C", "attendance": 90} 
        }
students[202]["attendance"] += 5
print(students) 
students[204] = {"name": "David", "age": 23, "grade": "B", "attendance": 88}
print(students)



# Q2. You are given a list that contains some duplicate items. Remove the duplicates by converting the list to a set. Final output should be in list
# shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
shopping_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
shopping_list1 = set(shopping_list)
print(list(shopping_list1))

# Q3. You have a list of numbers, and you want to find the unique numbers in the list. Use a set to identify and print the unique numbers.
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
numbers1 = set(numbers)
print(numbers1)
print(list(numbers1))

# Q3. You are managing a list of students enrolled in two different courses.You need to perform various set operations to understand the student enrollment.
# Task: Create two sets: one for students in "Course A" and one for students in "Course B". Find the students who are in "Course A" but not in "Course B" (difference).
# find students who are only in one of the two courses (symmetric difference).
# course_a = {"John", "Alice", "Bob", "David"} 
# course_b = {"Alice", "Eve", "Charlie", "David"}
# Using set methods

# • Find students who are in Course A but not in Course B (difference)

# • Find students who are only in one of the two courses (symmetric difference)

course_a = {"John", "Alice", "Bob", "David"}
course_b = {"Alice", "Eve", "Charlie", "David"}
print(course_a.difference(course_b))
print(course_a.symmetric_difference(course_b)) 


# Q4. Write a Python program to store and display the details of a book.
# The program should ask the user to input the following information:
# Title of the book
# Author’s name
# Year of publication
# Price of the booK
# Store the entered details in a tuple.
# Finally, display the book details in a proper format as shown below:
# Expected Output:
# Title: Harry Potter
# Author: JK Rowlings
# Year of Publication: 2000
# Price: $180.0

title = input("Enter the title of the book: ")
author = input("Enter the author's name: ")
year = input("Enter the year of publication: ")
price = float(input("Enter the price of the book: "))
book_details = (title ,author, year, price)
print(book_details)
print(f"Title: {book_details[0]}")
print(f"Author: {book_details[1]}")
print(f"Year of Publication: {book_details[2]}")
print(f"Price: ${book_details[3]}")


# 5. Write a program to check if a user’s chosen subject is available in the list of offered subjects.
# Instructions:
# Given a list of subjects, ask the user to input a subject.
# Display whether the subject is available or not.
# Expected Output:
# Enter the subject you are interested in: art
# art is available.

subjects = ["math", "science", "history", "art", "music"]
user_subject = input("Enter the subject you are interested in: ")
if user_subject in subjects:
    print("subjects is available.")
else:
    print("subjects is not available.")
    

# Q6. Write a Python program that asks the user to enter a number.

# If the number is greater than 0, print "Positive".

# If the number is less than 0, print "Negative".

# If the number is exactly 0, print "Zero".

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")   
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Q7. Write a Python program that asks the user to enter their age.
# If the age is 18 or older, print "You are eligible to vote."
# If the age is less than 18, print "You are not eligible to vote." 
# If the age is exactly 18, print "Congratulations on reaching voting age!"

age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("Congratulations on reaching voting age!")

# Q7. Write a Python program that simulates a simple login system.
# The correct username is 'admin' and the correct password is 'admin@123'
# The program should take username and password as input from the user.
# It should check the input and display messages according to the folowing conditions:
# If both username and password are correct → print "Login Successful"
# If username is wrong but password is correct → print "Invalid Username".
# If username is correct but password is wrong → print "Invalid Password".
# If both username and password are wrong → print "Invalid Username and Password".       

username = input("Enter your username: ")
password = input("Enter your password: ")   
if username == "admin" and password == "admin@123":
    print("Login Successful")   
elif username != "admin" and password == "admin@123":
    print("Invalid Username")
elif username == "admin" and password != "admin@123":
    print("Invalid Password")
else:
    print("Invalid Username and Password")

# Q8. Write a Python program that takes a number as input from the user and checks whether the number is even or odd.
# If the number is even, print "The number is even."
# If the number is odd, print "The number is odd."
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q9. Write a Python program that takes a year as input from the user and checks whether the year is a leap year or not.
# A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# If the year is a leap year, print "The year is a leap year."  
# If the year is not a leap year, print "The year is not a leap year."
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

# Q10. Write a Python program that takes three numbers as input from the user and finds the largest of the three numbers.
# If the first number is the largest, print "The first number is the largest."
# If the second number is the largest, print "The second number is the largest."
# If the third number is the largest, print "The third number is the largest."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The first number is the largest.")

elif num2 >= num1 and num2 >= num3:
    print("The second number is the largest.")

else:
    print("The third number is the largest.")

# Q11
# student_details = { "Ali": {"age": 20, "grade": "A", "city": "Karachi"}, "Sara": {"age": 21, "grade": "B", "city": "Lahore"}, "Omar": {"age": 19, "grade": "A", "city": "Islamabad"}, "Hina": {"age": 22, "grade": "C", "city": "Faisalabad"} }
# Add a new student using method: "Zara": {"age": 20, "grade": "B", "city": "Multan"}
# Remove a student "Omer" using method   

    student_details     = { 
                        "Ali": {"age": 20, "grade": "A", "city": "Karachi"},
    "Sara": {"age": 21, "grade": "B", "city": "Lahore"},
    "Omar": {"age": 19, "grade": "A", "city": "Islamabad"},
    "Hina": {"age": 22, "grade": "C", "city": "Faisalabad"} 
    }

    student_details ["zara"] = {"age" : 28, "grade" : "B", "city" : "Multan"}
    print(student_details)
    student_details.pop("Omar")
    print(student_details)

# Q12. You are given a nested dictionary that contains information about employees in a company. The outer dictionary uses employee IDs as keys, and the inner dictionary stores employee details like name, department, salary, and years of experience.
# employees = { 1: {"name": "John", "department": "HR", "salary": 50000, "experience": 5}, 2: {"name": "Alice", "department": "IT", "salary": 70000, "experience": 7}, 3: {"name": "Bob", "department": "Finance", "salary": 60000, "experience": 6} }
# • Increase the salary of the employee with ID 2 by 10% using arithmetic operators
# • Add a new employee to the dictionary
employees = { 
    1: {"name": "John", "department": "HR", "salary": 50000, "experience": 5}, 
    2: {"name": "Alice", "department": "IT", "salary": 70000, "experience": 7}, 
    3: {"name": "Bob", "department": "Finance", "salary": 60000, "experience": 6} 
    }
employees[2]["salary"] *= 1.10
print(employees)
employees[4] = {"name": "Eve", "department": "Marketing", "salary": 55000, "experience": 4}
print(employees)

# Q9. Write program to check a person’s eligibility for a loan based on age, credit score, 
# and income. This time, the eligibility criteria will be:
# The person must be 18 years or older. The person must have a credit score of 650 or higher. 
# The person must have an annual income of at least 30000 dollars If the person has a credit score of 700
# or higher, they may still be eligible with an income of 25000 dollars or more.

age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your annual income: "))
if age >= 18 and credit_score >= 650 and income >= 30000 or credit_score >= 700 and income >= 25000:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")


# Q10. Write a Python program to check whether the entered letter is a vowel, a consonant, or invalid input.
# The program should take a single character as input. If the character is a vowel (a, e, i, o, u in both upper and lower case), 
# it will print "Vowel". If it is an alphabet but not a vowel, it will print "Consonant".
# Otherwise, it will print "Please enter valid alphabet".
char = input("Enter a character: ")
if len(char) == 1 and char.isalpha():
    if char.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter valid alphabet")
   

                        