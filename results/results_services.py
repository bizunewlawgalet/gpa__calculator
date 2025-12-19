# results/result_service.py

results = []  # stores tuples: (student_id, course_code, letter_grade, grade_point)
results_file = "results.txt"

def score_to_letter(score):
    if score >= 90:
        return "A+"
    elif score >= 85:
        return "A"
    elif score >= 80:
        return "A-"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "B-"
    elif score >= 60:
        return "C+"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "C-"
    elif score >= 45:
        return "D"
    else:
        return "F"
def grade_point(letter):          # Return grade point for a letter grade
    table = {
        "A+": 4.0, "A": 4.0, "A-": 3.75,
        "B+": 3.5, "B": 3.0, "B-": 2.75,
        "C+": 2.5, "C": 2.0, "C-": 1.75,
        "D": 1.0, "F": 0.0
    }
    return table[letter]

def load_results():                # Load all results from file
    results.clear()
    try:
        with open(results_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue
                sid, code, letter, gp = parts
                results.append((sid, code, letter, float(gp)))
    except FileNotFoundError:
        pass

def save_results():                 # Save all results to file
    with open(results_file, "w") as file:
        for sid, code, letter, gp in results:
            file.write(f"{sid},{code},{letter},{gp}\n")

def add_result(sid, code, score, students_dict, courses_dict):  # Add a result for a student
    load_results()

    if sid not in students_dict:
        return "Student not found."

    if code not in courses_dict:
        return "Course not found."

    for st_id, crs, _, _ in results:
        if st_id == sid and crs == code:
            return "Result already exists for this student and course."

    letter = score_to_letter(score)
    gpoint = grade_point(letter)
    results.append((sid, code, letter, gpoint))
    save_results()
    return f"Result added! Grade = {letter}, Point = {gpoint}"

def list_results(sid, students_dict):          # Return all results for a student
    load_results()
    if sid not in students_dict:
        return None                           # student not found

    student_results = []
    for st_id, code, letter, gp in results:
        if st_id == sid:
            student_results.append({
                "student_id": st_id,
                "course_code": code,
                "grade": letter,
                "gpoint": gp
            })
    return student_results

def get_results():                            #Return all results
    load_results()
    return results
