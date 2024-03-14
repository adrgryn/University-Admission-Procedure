import io
from dataclasses import dataclass
import os

department_file_mapping = {
    "Biotech": "biotech.txt",
    "Chemistry": "chemistry.txt",
    "Engineering": "engineering.txt",
    "Mathematics": "mathematics.txt",
    "Physics": "physics.txt",
}


@dataclass(frozen=True, slots=True)
class Applicant:
    """Class for keeping track all applicants datas"""

    name: str
    physics_score: float
    chemistry_score: float
    biotech_score: float
    mathematics_score: float
    engineering_score: float
    special_exam_score: float
    first_choice: str
    second_choice: str
    third_choice: str

    # def __hash__(self):
    #     return hash((self.name, self.physics_score, self.chemistry_score, self.biotech_score, self.mathematics_score,
    #                  self.engineering_score, self.special_exam_score, self.first_choice, self.second_choice,
    #                  self.third_choice))


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
            special_exam_score = float(line[6])
            first_choice = line[7]
            second_choice = line[8]
            third_choice = line[9]
            applicants_lst.append(Applicant(name, physics_score, chemistry_score, biotech_score, mathematics_score,
                                            engineering_score, special_exam_score, first_choice, second_choice,
                                            third_choice))

    return applicants_lst


def new_sort_applicants(applicants_sorted_lst: list, c: int) -> dict:
    departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
    added_applicants = []

    def choice(applicants: list, choice_attr: str) -> None:
        for applicant in applicants:
            if applicant not in added_applicants:
                choice_attribute = getattr(applicant, choice_attr)
                if choice_attribute in departments and len(departments[choice_attribute]) < c:
                    departments[choice_attribute].append(applicant)
                    added_applicants.append(applicant)

    # Call the function for each choice
    choice(applicants_sorted_lst, 'first_choice')
    choice(applicants_sorted_lst, 'second_choice')
    choice(applicants_sorted_lst, 'third_choice')

    # Sort lists inside departments dict
    for department, applicants_lst in departments.items():
        score = f"{department.lower()}_score"
        applicants_lst.sort(key=lambda x: (-max(getattr(x, score), x.special_exam_score), x.name))

    return departments


def save_to_file(departments: dict):
    """Create file with applicants for each department"""

    applicant_lst = []
    # Define filename and path
    for department, applicants in departments.items():
        file_name = department_file_mapping.get(department, 'default.txt')
        directory = 'data'
        path = os.path.join(directory, file_name)

        # Check if 'data' directory exist and if not create it
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            # check if applicant is already saved in file
            with open(path, 'w') as applicants_file:
                content = applicants_file.readlines()
                for line in content:
                    applicant_lst.append(line)
        except io.UnsupportedOperation:
            pass
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass

        with open(path, 'a') as applicants_file:
            for applicant in applicants:
                # Check if the applicant name is not already in the file
                if applicant.name not in applicant_lst:
                    if getattr(applicant, department.lower() + "_score") > applicant.special_exam_score:
                        applicants_file.write(f'{applicant.name} {getattr(applicant, department.lower() + "_score")}\n')
                    else:
                        applicants_file.write(f'{applicant.name} {applicant.special_exam_score}\n')


# print(new_sort_applicants(read_file(), 3))