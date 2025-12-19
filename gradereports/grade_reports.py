# gradereports/grade_report.py
REPORT_FILE = "grade_reports.txt"
def save_report(sid, report_lines):    # Append a student's report to the file
    with open(REPORT_FILE, "a") as file:
        file.write(f"Student ID: {sid}\n")
        for line in report_lines:
            file.write(line + "\n")
        file.write("\n\n")

def load_reports():                   # Load all saved grade reports from file
    reports = {}
    try:
        with open(REPORT_FILE, "r") as file:
            current_sid = None
            current_lines = []
            for line in file:
                line = line.strip()
                if line.startswith("Student ID:"):
                    if current_sid and current_lines:
                        reports[current_sid] = current_lines
                    current_sid = line.split(":")[1].strip()
                    current_lines = []
                elif line:
                    current_lines.append(line)
            if current_sid and current_lines:
                reports[current_sid] = current_lines
    except FileNotFoundError:
        pass
    return reports
def calculate_gpa(sid, students_dict, courses_dict, results_list, save_to_file=True):
                                                       # Calculate GPA and generate report for a student
    if sid not in students_dict:
        return f"Student ID {sid} not found.", None

    info = students_dict[sid]
    header = f"Grade Report for {info['fname']} {info['lname']} ({info['dept']})"

    total_points = 0
    total_credits = 0
    found_any = False

    col_widths = [12, 20, 8, 6, 5]

    def hline():
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    report_lines = [header, hline()]
    title_line = f"| {'Course Code':<12} | {'Title':<20} | {'Credit':^8} | {'Grade':^6} | {'GP':^5} |"
    report_lines.append(title_line)
    report_lines.append(hline())

    for st_id, course_code, letter, gp in results_list:
        if st_id == sid:
            found_any = True
            if course_code not in courses_dict:
                line = f"| {course_code:<12} | {'ERROR: Course missing':<20} | {'-':^8} | {'-':^6} | {'-':^5} |"
                report_lines.append(line)
                report_lines.append(hline())
                continue

            title, credit = courses_dict[course_code]
            line = f"| {course_code:<12} | {title:<20} | {credit:^8} | {letter:^6} | {gp:^5.2f} |"
            report_lines.append(line)
            report_lines.append(hline())
            total_points += gp * credit
            total_credits += credit

    if not found_any:
        return "No course results found for this student.", report_lines

    if total_credits == 0:
        return "Credits are zero. Can't calculate GPA.", report_lines

    gpa = total_points / total_credits
    summary_lines = [
        f"Total Credits: {total_credits}",
        f"Total Grade Points: {total_points:.2f}",
        f"GPA: {gpa:.2f}",
    ]
    report_lines.extend(summary_lines)

    if save_to_file:
        save_report(sid, report_lines)

    return "Report generated successfully.", report_lines
