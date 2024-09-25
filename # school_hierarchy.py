# school_hierarchy.py

class School:
    def __init__(self, name, principal, student_count):
        self.name = name
        self.principal = principal
        self.student_count = student_count

    def display_info(self):
        print(f"School Name: {self.name}, Principal: {self.principal}, Student Count: {self.student_count}")


class MiddleSchool(School):
    def __init__(self, name, principal, student_count, lowest_grade, highest_grade):
        super().__init__(name, principal, student_count)
        self.lowest_grade = lowest_grade
        self.highest_grade = highest_grade

    def display_info(self):
        super().display_info()
        print(f"Grades Offered: {self.lowest_grade} to {self.highest_grade}")


class HighSchool(School):
    def __init__(self, name, principal, student_count, sports_field_name):
        super().__init__(name, principal, student_count)
        self.sports_field_name = sports_field_name

    def display_info(self):
        super().display_info()
        print(f"Sports Field Name: {self.sports_field_name}")


# Main program
if __name__ == "__main__":
    my_school = School("Green Valley School", "Mr. Smith", 500)
    my_school.display_info()

    my_middle_school = MiddleSchool("Riverdale Middle School", "Ms. Johnson", 300, 6, 8)
    my_middle_school.display_info()

    my_high_school = HighSchool("Westside High School", "Mr. Brown", 700, "Westside Stadium")
    my_high_school.display_info()
