class ManageStudents:
    def __init__(self, student_dict):
        self.student_dict = student_dict

    def view_individual_student_details(self, roll_number):
        if roll_number in self.student_dict:
            print(self.student_dict[roll_number])
        else:
            print(f"The student with roll number - {roll_number} doesn't exist\n")
                
    def topper(self):
        max_total_marks = 0
        for _, student in self.student_dict.items():
            sum_of_the_marks = 0
            for m in student.marks:
                sum_of_the_marks = sum_of_the_marks + int(m)
            if sum_of_the_marks > max_total_marks:
                max_total_marks = sum_of_the_marks
                topper_of_class = student
        print(topper_of_class) 
    
    def average_mark_in_each_subject(self):
        sub_1_total_mark, sub_2_total_mark, sub_3_total_mark = [0, 0, 0]
        for _,student in self.student_dict.items():
            sub_1_total_mark = sub_1_total_mark + int(student.marks[0])
            sub_2_total_mark = sub_2_total_mark + int(student.marks[1])
            sub_3_total_mark = sub_3_total_mark + int(student.marks[2])
        avg_sub_1 = sub_1_total_mark/len(self.student_dict)
        avg_sub_2 = sub_2_total_mark/len(self.student_dict)
        avg_sub_3 = sub_3_total_mark/len(self.student_dict)
        print(f'\naverage mark in subject - 1 is : {avg_sub_1}')
        print(f'average marks in subfect - 2 is :  {avg_sub_2}')
        print(f'average marks in subject  - 3 is : {avg_sub_3}\n\n')

    def __str__(self):
        for i, (_, s) in enumerate(self.student_dict.items()):
            print(f"\nStudent - {i+1} Details:{s}")
        return f"\n"
    
    def topper_in_each_subject(self):
        max_marks_sub1, max_marks_sub2, max_marks_sub3 = [0, 0, 0]
        topper_sub1, topper_sub2, topper_sub3 = ["", "", ""]
        for _,student in self.student_dict.items():
            if max_marks_sub1 < int(student.marks[0]):
                max_marks_sub1 = int(student.marks[0])
                topper_sub1 = student
            if max_marks_sub2 < int(student.marks[1]):
                max_marks_sub2 = int(student.marks[1])
                topper_sub2 = student
            if max_marks_sub3 < int(student.marks[2]):
                max_marks_sub3 = int(student.marks[2])
                topper_sub3 = student
        print(f"\nTopper of subject - 1: {topper_sub1}")
        print(f"Topper of subject - 2: {topper_sub2}")
        print(f"Topper of subject - 3: {topper_sub3}\n\n")