# courses/course_service.py

courses = {}
course_file = "courses.txt"

def load_courses():             #Load all courses from file into memory
    courses.clear()
    try:
        with open(course_file, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                code, title, credit = parts
                courses[code] = (title, int(credit))
    except FileNotFoundError:
        pass

def save_courses():             #   Save all courses from memory to file
    with open(course_file, "w") as file:
        for code, (title, credit) in courses.items():
            file.write(f"{code},{title},{credit}\n")

def add_course(code, title, credit):
    load_courses()
    if code in courses:
        return False             # Course code already exists

    courses[code] = (title, credit)
    save_courses()
    return True

def list_courses():               # Return list of all courses
    load_courses()
    course_list = []
    for code, (title, credit) in courses.items():
        course_list.append({
            "code": code,
            "title": title,
            "credit": credit
        })
    return course_list

def get_courses():                # Return raw courses dictionary
    load_courses()
    return courses
