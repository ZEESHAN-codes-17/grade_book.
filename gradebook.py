import csv
import os

FILENAME = "grades.csv"

# ---------- Helper Functions ----------

def load_data():
    students = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert marks to integers, average to float
                student = {
                    "id": row["id"],
                    "name": row["name"],
                    "math": int(row["math"]),
                    "english": int(row["english"]),
                    "science": int(row["science"]),
                    "total": int(row["total"]),
                    "average": float(row["average"]),
                    "grade": row["grade"]
                }
                students.append(student)
    return students

def save_data(students):
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["id", "name", "math", "english", "science", "total", "average", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def calculate_grade(total, subjects=3):
    avg = total / subjects
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 55:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"
    return avg, grade

# ---------- Core Features ----------

def add_student(students):
    sid = input("Enter student ID: ")
    for s in students:
        if s["id"] == sid:
            print("❌ ID already exists!")
            return
    
    name = input("Enter name: ")
    try:
        math = int(input("Enter Math marks (0-100): "))
        english = int(input("Enter English marks (0-100): "))
        science = int(input("Enter Science marks (0-100): "))
    except ValueError:
        print("❌ Invalid marks, must be numbers!")
        return
    
    total = math + english + science
    avg, grade = calculate_grade(total)

    student = {
        "id": sid,
        "name": name,
        "math": math,
        "english": english,
        "science": science,
        "total": total,
        "average": avg,
        "grade": grade
    }

    students.append(student)
    save_data(students)
    print(f"✅ Student {name} added successfully!")

def view_students(students):
    if not students:
        print("No student records yet.")
        return
    print("\nID   Name       Math English Science Total Average Grade")
    print("-"*55)
    for s in students:
        print(f"{s['id']:4} {s['name']:10} {s['math']:5} {s['english']:7} {s['science']:7} {s['total']:5} {s['average']:7.2f} {s['grade']:5}")

def search_student(students):
    choice = input("Search by ID or Name? (id/name): ").lower()
    if choice == "id":
        sid = input("Enter ID: ")
        for s in students:
            if s["id"] == sid:
                print(s)
                return
        print("❌ Student not found.")
    elif choice == "name":
        name = input("Enter name: ").lower()
        results = [s for s in students if name in s["name"].lower()]
        if results:
            for s in results:
                print(s)
        else:
            print("❌ No student found with that name.")

def update_student(students):
    sid = input("Enter ID of student to update: ")
    for s in students:
        if s["id"] == sid:
            print(f"Updating {s['name']}...")
            try:
                math = int(input("Enter new Math marks: "))
                english = int(input("Enter new English marks: "))
                science = int(input("Enter new Science marks: "))
            except ValueError:
                print("❌ Invalid input, must be numbers!")
                return
            total = math + english + science
            avg, grade = calculate_grade(total)
            s["math"], s["english"], s["science"] = math, english, science
            s["total"], s["average"], s["grade"] = total, avg, grade
            save_data(students)
            print("✅ Student updated successfully!")
            return
    print("❌ Student not found.")

def delete_student(students):
    sid = input("Enter ID of student to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data(students)
            print("✅ Student deleted successfully!")
            return
    print("❌ Student not found.")

# ---------- Main Menu ----------

def main():
    students = load_data()
    while True:
        print("\n---- Gradebook Manager ----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()

      
         
         
  

          



