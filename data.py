import io
from dataclasses import dataclass


department_file_mapping = {
        "Biotech": "biotech.txt",
        "Chemistry": "chemistry.txt",
        "Engineering": "engineering.txt",
        "Mathematics": "mathematics.txt",
        "Physics": "physics.txt",
    }

@dataclass(slots=True)
class Applicant:
    """Class for keeping track all applicants datas"""

    name: str
    physics_score: float
    chemistry_score: float
    biotech_score: float
    mathematics_score: float
    engineering_score: float
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
            physics_score = (float(line[2]) + float(line[4])) / 2  # mean of physic and math score
            chemistry_score = float(line[3])
            biotech_score = (float(line[3]) + float(line[2])) / 2  # mean of physic and chemistry score
            mathematics_score = float(line[4])
            engineering_score = (float(line[5]) + float(line[4])) / 2  # mean of computer and math score
            first_choice = line[6]
            second_choice = line[7]
            third_choice = line[8]
            applicants_lst.append(Applicant(name, physics_score, chemistry_score, biotech_score, mathematics_score,
                                            engineering_score, first_choice, second_choice, third_choice))

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
    department_lst = ['Physics', 'Chemistry', 'Biotech', 'Mathematics', 'Engineering']

    def choice(index: int, choice: str) -> None:
        """Take first N applicants by their first choice form sorted list of each department
        (chosen by index from list above) and place in departments dict, also check if there aren't
         same applicants in different departments"""

        for applicant in applicants_sorted_lst[index]:
            if applicant not in added_applicants:
                choice_attribute = getattr(applicant, choice)
                if choice_attribute in department_lst[index] and len(departments[choice_attribute]) < c:
                    departments[choice_attribute].append(applicant)
                    added_applicants.append(applicant)

    # call the function above with indexes proper for department_lst
    for i in range(0, 5):
        choice(i, 'first_choice')
    for i in range(0, 5):
        choice(i, 'second_choice')
    for i in range(0, 5):
        choice(i, 'third_choice')

    # sort lists inside departments dict according to GPA and if score is same by name
    for department, applicants_lst in departments.items():
        score = f"{department.lower()}_score"
        applicants_lst.sort(key=lambda x: x.name)
        applicants_lst.sort(key=lambda x: getattr(x, score), reverse=True)

    return departments


def save_to_file(departments: dict):
    """Create file with applicants for each department"""

    applicant_lst = []
    for department, applicants in departments.items():
        file_name = department_file_mapping.get(department, 'default.txt')
        try:
            # check if applicant is already saved in file
            with open(file_name, 'w') as applicants_file:
                content = applicants_file.readlines()
                for line in content:
                    applicant_lst.append(line)
        except io.UnsupportedOperation:
            pass
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass

        with open(file_name, 'a') as applicants_file:
            for applicant in applicants:
                # Check if the applicant name is not already in the file
                if applicant.name not in applicant_lst:
                    applicants_file.write(f'{applicant.name} {getattr(applicant, department.lower() + "_score")}\n')

