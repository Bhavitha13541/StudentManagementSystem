from student import Student
from manage import ManageStudents

def view_student_details(student_dict):
    print('\t\t\t\t\t\t\033[33m1 -> view individual student details')
    print('\t\t\t\t\t\t2 -> topper of the class')
    print('\t\t\t\t\t\t3 -> average marks in each subject')
    print('\t\t\t\t\t\t4 -> all student details')
    print('\t\t\t\t\t\t5 -> topper in each subject\033[0m')

    choice = int(input("which operation do you want to peform: "))
    obj = ManageStudents(student_dict)

    if choice == 1:
        rnum = input("enter the roll number: ")
        obj.view_individual_student_details(rnum)
    elif choice == 2:
        obj.topper()
    elif choice == 3:
        obj.average_mark_in_each_subject()
    elif choice == 4:
        print(obj)
    elif choice == 5:
        obj.topper_in_each_subject()    

def main():
    student_dict = {}
    while True:
        print("\t\t\t\t\033[32m############################ WELCOME TO STUDENT MANAGEMENT SYSTEM ############################\033[0m\n")
        print("\t\t\t\t\t\t\033[35m1 -> Save the student details\033[0m")
        print("\t\t\t\t\t\t\033[35m2 -> View the student details\033[0m")
        print("\t\t\t\t\t\t\033[35m3 -> exit\033[0m")
        choice = int(input("enter the operation do you want to perform: "))
        if choice == 1:
            r_no = input("enter the roll number of the student: ") 
            name = input("Enter Name of the student: ")
            gender = input("Enter Gender of the student: ")
            age = input("Enter Age of the student: ")
            marks = []
            for i in range(3):
                marks.append(input(f'Enter the marks of the subject - {i+1}: '))
            print("\n")
            student = Student(r_no, name, gender, age, marks)
            student_dict[r_no] = student
        elif choice == 2:
            if len(student_dict) == 0:
                print("There are no student details please add them first")
            else:
                view_student_details(student_dict)
        elif choice == 3:
            exit()
        else:
            print('Incorrect choice')

if __name__ == '__main__':
    main()