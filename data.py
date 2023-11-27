from dataclasses import dataclass


@dataclass(slots=True)
class Applicant:
    """Class for keeping track all applicants datas"""

    name: str
    physic_score: float
    chemistry_score: float
    math_score: float
    computer_science: float
    first_choice: str
    second_choice: str
    third_choice: str


def read_file() -> list:
    """Read file, place data of applicant in dataclass, make a list of applicants objects"""
    applicants_lst = []
    with open('applicant_list.txt', 'r') as file:
        applicants = file.readlines()
        for line in applicants:
            line = line.split()
            name = ' '.join(line[0:2])
            physic_score = (float(line[2]) + float(line[4])) / 2  # mean of physic and math score
            chemistry_score = float(line[3])
            math_score = float(line[4])
            computer_science = float(line[5])
            first_choice = line[6]
            second_choice = line[7]
            third_choice = line[8]
            applicants_lst.append(Applicant(name, physic_score, chemistry_score, math_score, computer_science,
                                            first_choice, second_choice, third_choice))

    return applicants_lst



def new_sort_applicants(applicants_sorted_lst: list, c: int) -> dict:
    """Assign applicants to the proper department first by the first_choice, next second_choice...,
    sort applicants list inside dict, check if there aren't same applicants in different departments"""

    departments = {'Biotech': [],
                   'Chemistry': [],
                   'Engineering': [],
                   'Mathematics': [],
                   'Physics': []
                   }
    added_applicants = []
    department_lst = ['Physics', ['Chemistry', 'Biotech'], 'Mathematics', 'Engineering']

    def first_choice(index: int) -> None:
        """Take first N applicants by their first choice form sorted list of each department
        (chosen by index from list above) and place in departments dict, also check if there aren't
         same applicants in different departments"""

        for applicant in applicants_sorted_lst[index]:
            if applicant not in added_applicants:
                if applicant.first_choice in department_lst[index] and len(departments[applicant.first_choice]) < c:
                    departments[applicant.first_choice].append(applicant)
                    added_applicants.append(applicant)

    def second_choice(index: int) -> None:
        """Take first N applicants by their second choice form sorted list of each department
                (chosen by index from list above) and place in departments dict, also check if there aren't
                 same applicants in different departments"""

        for applicant in applicants_sorted_lst[index]:
            if applicant not in added_applicants:
                if applicant.second_choice in department_lst[index] and len(departments[applicant.second_choice]) < c:
                    departments[applicant.second_choice].append(applicant)
                    added_applicants.append(applicant)

    def third_choice(index: int) -> None:
        """Take first N applicants by their third choice form sorted list of each department
                (chosen by index from list above) and place in departments dict, also check if there aren't
                 same applicants in different departments"""

        for applicant in applicants_sorted_lst[index]:
            if applicant not in added_applicants:
                if applicant.third_choice in department_lst[index] and len(departments[applicant.third_choice]) < c:
                    departments[applicant.third_choice].append(applicant)
                    added_applicants.append(applicant)

    # call the function above with indexes proper for department_lst
    for i in range(0, 4):
        first_choice(i)
    for i in range(0, 4):
        second_choice(i)
    for i in range(0, 4):
        third_choice(i)


    # sort lists inside departments dict according to GPA and if score is same by name
    for department, applicants_lst in departments.items():

        if department == "Biotech":
            applicants_lst.sort(key=lambda x: x.name)
            applicants_lst.sort(key=lambda x: x.chemistry_score, reverse=True)
        if department == "Chemistry":
            applicants_lst.sort(key=lambda x: x.name)
            applicants_lst.sort(key=lambda x: x.chemistry_score, reverse=True)
        if department == "Engineering":
            applicants_lst.sort(key=lambda x: x.name)
            applicants_lst.sort(key=lambda x: x.computer_science, reverse=True)
        if department == "Mathematics":
            applicants_lst.sort(key=lambda x: x.name)
            applicants_lst.sort(key=lambda x: x.math_score, reverse=True)
        if department == "Physics":
            applicants_lst.sort(key=lambda x: x.name)
            applicants_lst.sort(key=lambda x: x.physic_score, reverse=True)

    return departments




