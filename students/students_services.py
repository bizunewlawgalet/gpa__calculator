# students/student_service.py
students = {}  # Global dictionary: id data
STUDENT_FILE = "students.txt"
def load_students():                           # Load all students from file into memory
    students.clear()
    try:
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                sid, fname, lname, dept = parts
                students[sid] = {"fname": fname, "lname": lname, "dept": dept}
    except FileNotFoundError:
        pass

def register_student(sid, fname, lname, dept):    # Register a new student
    load_students()

    if sid in students:
        return False  

    students[sid] = {"fname": fname, "lname": lname, "dept": dept}
    with open(STUDENT_FILE, "a") as file:
        file.write(f"{sid},{fname},{lname},{dept}\n")
    return True

def list_students():                            #   Return list of student dicts
    load_students()
    if not students:
        return []

    student_list = []                            # Return list of student dicts
    for sid, data in students.items():
        student_list.append({
            "id": sid,
            "fname": data["fname"],
            "lname": data["lname"],
            "dept": data["dept"]
        })
    return student_list

def get_students():                             #   Return raw students dictionary
    load_students()
    return students
