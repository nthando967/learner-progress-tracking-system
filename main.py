# Programmer Name: Thando Nkosi
# Date: 11 June 2026
# Program: Learner Progress Tracking System (LPTS)

from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.withdraw()

# =========================
# BASE CLASS
# =========================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# =========================
# LEARNER CLASS
# =========================

class Learner(Person):

    def __init__(self, learner_id, name, age, course):

        super().__init__(name, age)

        self.learner_id = learner_id
        self.course = course
        self.marks = []

        # Encapsulation
        self.__average = 0

    # =========================
    # ADD MARK
    # =========================

    def add_mark(self, mark):

        if mark < 0 or mark > 100:

            messagebox.showerror(
                "Invalid Mark",
                "Marks must be between 0 and 100."
            )

            return

        self.marks.append(mark)

        self.calculate_average()

    # =========================
    # CALCULATE AVERAGE
    # =========================

    def calculate_average(self):

        try:

            total = recursive_sum(self.marks)

            self.__average = total / len(self.marks)

        except ZeroDivisionError:

            self.__average = 0

    # =========================
    # GET AVERAGE
    # =========================

    def get_average(self):

        return self.__average

    # =========================
    # STATUS
    # =========================

    def get_status(self):

        average = self.get_average()

        if average < 50:

            return "Fail"

        elif average >= 50 and average <= 74:

            return "Pass"

        else:

            return "Pass with Distinction"

    # =========================
    # CERTIFICATE CHECK
    # =========================

    def qualifies_for_certificate(self):

        return self.get_average() >= 50

    # =========================
    # DISPLAY DETAILS
    # =========================

    def display_details(self):

        print("\n================================")
        print("LEARNER DETAILS")
        print("================================")

        print(f"Learner ID: {self.learner_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Performance: {self.get_status()}")

        if self.qualifies_for_certificate():

            print("Certificate: YES")

        else:

            print("Certificate: NO")

        print("================================")


# =========================
# RECURSIVE FUNCTION
# =========================

def recursive_sum(mark_list):

    if len(mark_list) == 0:

        return 0

    return mark_list[0] + recursive_sum(mark_list[1:])


# =========================
# LEARNER STORAGE LIST
# =========================

learners = []


# =========================
# SEARCH LEARNER
# =========================

def search_learner(learner_id):

    for learner in learners:

        if learner.learner_id == learner_id:

            return learner

    return None


# =========================
# ADD LEARNER
# =========================

def add_learner():

    try:

        learner_id = input("Enter learner ID: ")

        if search_learner(learner_id):

            print("Learner already exists.")
            return

        name = input("Enter learner name: ")

        age = int(input("Enter learner age: "))

        if age < 10:

            print("Invalid age.")
            return

        course = input("Enter learner course: ")

        learner = Learner(
            learner_id,
            name,
            age,
            course
        )

        learners.append(learner)

        messagebox.showinfo(
            "Success",
            "Learner added successfully."
        )

    except ValueError:

        print("Invalid input.")


# =========================
# VIEW LEARNERS
# =========================

def view_learners():

    if len(learners) == 0:

        print("No learners found.")
        return

    for learner in learners:

        learner.display_details()


# =========================
# SEARCH AND DISPLAY
# =========================

def search_and_display():

    learner_id = input("Enter learner ID to search: ")

    learner = search_learner(learner_id)

    if learner:

        learner.display_details()

    else:

        print("Learner not found.")


# =========================
# UPDATE LEARNER
# =========================

def update_learner():

    learner_id = input("Enter learner ID: ")

    learner = search_learner(learner_id)

    if learner:

        new_name = input("Enter new name: ")

        if new_name != "":

            learner.name = new_name

        new_course = input("Enter new course: ")

        if new_course != "":

            learner.course = new_course

        print("Learner updated.")

    else:

        print("Learner not found.")


# =========================
# REMOVE LEARNER
# =========================

def remove_learner():

    learner_id = input("Enter learner ID: ")

    learner = search_learner(learner_id)

    if learner:

        learners.remove(learner)

        print("Learner removed.")

    else:

        print("Learner not found.")


# =========================
# ENTER MARKS
# =========================

def enter_marks():

    learner_id = input("Enter learner ID: ")

    learner = search_learner(learner_id)

    if learner is None:

        print("Learner not found.")
        return

    try:

        number_of_marks = int(
            input("Enter number of marks (2 - 5): ")
        )

        # Validation
        if number_of_marks < 2 or number_of_marks > 5:

            print("You must enter between 2 and 5 marks.")
            return

        # Loop
        for i in range(number_of_marks):

            mark = float(
                input(f"Enter mark {i + 1}: ")
            )

            # Continue
            if mark < 0 or mark > 100:

                print("Invalid mark skipped.")
                continue

            learner.add_mark(mark)

        # Average automatically calculated
        print("\nAverage Calculated Successfully")
        print(f"Average: {learner.get_average():.2f}")
        print(f"Performance: {learner.get_status()}")

        # Message box
        messagebox.showinfo(
            "Results",
            f"Average: {learner.get_average():.2f}\n"
            f"Status: {learner.get_status()}"
        )

    except ValueError:

        print("Invalid input.")


# =========================
# COUNT LEARNERS
# =========================

def count_learners_recursive(learner_list):

    if len(learner_list) == 0:

        return 0

    return 1 + count_learners_recursive(
        learner_list[1:]
    )


# =========================
# MAIN MENU
# =========================

while True:

    print("\n================================")
    print(" LEARNER PROGRESS TRACKING ")
    print("================================")

    print("1. Add Learner")
    print("2. View Learners")
    print("3. Search Learner")
    print("4. Update Learner")
    print("5. Remove Learner")
    print("6. Enter Marks")
    print("7. Count Learners")
    print("8. Exit")

    choice = input("Enter choice: ")

    # =========================
    # MENU OPTIONS
    # =========================

    if choice == "1":

        add_learner()

    elif choice == "2":

        view_learners()

    elif choice == "3":

        search_and_display()

    elif choice == "4":

        update_learner()

    elif choice == "5":

        remove_learner()

    elif choice == "6":

        enter_marks()

    elif choice == "7":

        total = count_learners_recursive(
            learners
        )

        print(f"Total learners: {total}")

    elif choice == "8":

        confirm = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if confirm:

            print("Program closed.")
            break

    else:

        print("Invalid menu option.")