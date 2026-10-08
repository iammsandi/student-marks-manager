student_name = "Jane Doe"
English_score = 95
Science_score = 88
marks= {
    "English_score": 95, 
    "Science_score": 88
}
average_score = (English_score + Science_score) / 2
with open("student_marks.txt", "w") as file:
    file.write(f"Student Name: {student_name}\n")
    file.write(f"English Score: {English_score}\n")
    file.write(f"Science Score: {Science_score}\n")
    file.write(f"Average Score: {average_score}\n")
while True:
    if average_score >= 90:
        print("well done")
    elif average_score >= 80:
        print("good job")
    elif average_score >= 70:
        print("you can do better")
    else:
        print("keep trying")
    break 
print(f"{student_name}'s average score is: {average_score}")
#The next student 
student_name = input("Enter the next student's name: ")
while True: 
    try:
        English_score = int(input("Enter the English score: "))
        Science_score = int(input("Enter the Science score: "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for scores.")
    continue
average_score = (English_score + Science_score) / 2
with open("student_marks.txt", "w") as file:
    file.write(f"Student Name: {student_name}\n")
    file.write(f"English Score: {English_score}\n")
    file.write(f"Science Score: {Science_score}\n")
    file.write(f"Average Score: {average_score}\n")
while True:
    if average_score >= 90:
        print("well done")
    elif average_score >= 80:
        print("good job")
    elif average_score >= 70:
        print("you can do better")
    else:
        print("keep trying")
    break 
while True:
    student_name = input("enter student name (or type 'stop' to end ):")
    if student_name.strip().lower() == "Stop":
        break
    #The next student 
student_name = input("Enter the next student's name: ")
English_score = int(input("Enter the English score: "))
Science_score = int(input("Enter the Science score: "))
average_score = (English_score + Science_score) / 2
while True:
    if average_score >= 90:
        print("well done")
    elif average_score >= 80:
        print("good job")
    elif average_score >= 70:
        print("you can do better")
    else:
        print("keep trying")
    break 
with open("student_marks.txt", "w") as file:
    file.write(f"Student Name: {student_name}\n")
    file.write(f"English Score: {English_score}\n")
    file.write(f"Science Score: {Science_score}\n")
    file.write(f"Average Score: {average_score}\n")