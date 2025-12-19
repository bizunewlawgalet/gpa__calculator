# app.py
from students.students_services import register_student, list_students, get_students
from courses.courses_services import add_course, list_courses, get_courses
from results.results_services import add_result, list_results, get_results
from gradereports.grade_reports import calculate_gpa

def main_menu():
    while True:
        print("\n= GPA CALCULATOR MAIN MENU =")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            students_menu()
        elif choice == "2":
            courses_menu()
        elif choice == "3":
            results_menu()
        elif choice == "4":
            report_menu()
        elif choice == "5":
            print("Exiting program…")
            break
        else:
            print("Invalid choice! Try again.")
# ------- Students Menu -----------
def students_menu():
    while True:
        print("\n---- Students Menu ----")
        print("1. Register Student")
        print("2. View Students")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            fname = input("Enter First Name: ").strip()
            lname = input("Enter Last Name: ").strip()
            dept = input("Enter Department: ").strip()

            if register_student(sid, fname, lname, dept):
                print("Student registered successfully.")
            else:
                print("Student ID already exists!")

        elif choice == "2":
            students = list_students()
            if not students:
                print("No students registered.")
            else:
                line = "+------------+----------------+----------------+------------+"
                print("\n" + line)
                print(f"| {'ID':<10} | {'First Name':<14} | {'Last Name':<14} | {'Dept':<10} |")
                print(line)
                for s in students:
                    print(f"| {s['id']:<10} | {s['fname']:<14} | {s['lname']:<14} | {s['dept']:<10} |")
                print(line)

        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")
# ----- Courses Menu ----------
def courses_menu():
    while True:
        print("\n---- Courses Menu ----")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            code = input("Enter Course Code: ").strip()
            title = input("Enter Course Title: ").strip()
            while True:
                try:
                    credit = int(input("Enter Credit Hours: ").strip())
                    break
                except ValueError:
                    print("Credit must be a number.")

            if add_course(code, title, credit):
                print("Course added successfully!")
            else:
                print("Course code already exists!")

        elif choice == "2":
            courses = list_courses()
            if not courses:
                print("No courses added.")
            else:
                col_widths = [12, 30, 8]

                def hline():
                    print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

                hline()
                print(f"| {'Code':<12} | {'Title':<30} | {'Credit':^8} |")
                hline()
                for c in courses:
                    print(f"| {c['code']:<12} | {c['title']:<30} | {c['credit']:^8} |")
                    hline()

        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")

# ------- Results Menu -----------
def results_menu():
    while True:
        print("\n---- Results Menu ----")
        print("1. Record Result")
        print("2. View Results")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID: ").strip()
            code = input("Enter Course Code: ").strip()
            while True:
                try:
                    score = float(input("Enter Score (0-100): ").strip())
                    if 0 <= score <= 100:
                        break
                    print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid number.")

            message = add_result(sid, code, score, get_students(), get_courses())
            print(message)

        elif choice == "2":
            sid = input("Enter Student ID to view results: ").strip()
            student_results = list_results(sid, get_students())
            if student_results is None:
                print("Student ID not registered.")
            elif not student_results:
                print("No results found for this student.")
            else:
                print("+--------------+--------------+----------+--------+")
                print("| Student ID   | Course Code  |  Grade   |   GP   |")
                print("+--------------+--------------+----------+--------+")
                for r in student_results:
                    print(f"| {r['student_id']:<12} | {r['course_code']:<12} | {r['grade']:^8} | {r['gpoint']:^6.1f} |")
                print("+--------------+--------------+----------+--------+")

        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")
# ----- Grade Report Menu -------------
def report_menu():
    while True:
        print("\n---- Grade Report Menu ----")
        print("1. Generate GPA Report")
        print("2. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            sid = input("Enter Student ID for GPA: ").strip()
            message, report_lines = calculate_gpa(sid, get_students(), get_courses(), get_results())
            print(message)
            if report_lines:
                print("\n".join(report_lines))

        elif choice == "2":
            break
        else:
            print("Invalid choice! Try again.")

# ---- Main ----------
if __name__ == "__main__": 
    main_menu()
