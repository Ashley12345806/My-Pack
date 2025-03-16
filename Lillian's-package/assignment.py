def student_details():
    name= input("Enter your name here:")
    age= int(input("Enter your age here"))
    gender= input("Enter your gender")
    program = input("Enter your program")
    year_of_study = int(input("Enter your year of study"))
    date_of_birth = input("Enter your date of birth")
    faculty = input("Enter your faculty")
    student_info = {"name":name, "age":age, "gender":gender, "program":program, "year_of_study":year_of_study, "date_of_birth":date_of_birth, "faculty":faculty}
    return student_info
print(student_details())

def marksheet():
    test1 = int(input("Enter your test1 marks here"))
    test2 = int(input("Enter your test2 marks here"))
    final_exams = int(input("Enter your final exams marks here"))
    print("sum_marks")
    sum_marks = test1 + test2 
    print(sum_marks)
    print("average_marks")
    average_marks = sum_marks/2
    print(average_marks)
    final_test_marks = average_marks *(40/100)
    print(f"marked out of 40:{final_test_marks}")
    final_exam_marks = final_exams *(60/100)
    print(f"marked out of 60:{final_exam_marks}")
    total_marks = final_test_marks + final_exam_marks
    print(f"total marks:{total_marks}")
    total_marks = round(total_marks,1)
    return total_marks
print(marksheet())
