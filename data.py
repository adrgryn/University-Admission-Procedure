from dataclasses import dataclass
import university_func


@dataclass(slots=True)
class Applicant:
    """Class for keeping track all applicants datas"""

    name: str
    GPA: float
    first_choice: str
    second_choice: str
    third_choice: str


applicants_lst = university_func.read_file()
applicants_sorted_lst = university_func.sort_read_file(applicants_lst)


def applicants_lst(applicants_sorted_lst: list) -> list:
    """Give me access to data from Applicant dataclass after tapping  . """
    applicants = []

    for _ in applicants_sorted_lst:
        applicant = Applicant(_['name'], _['GPA'], _['first_choice'], _['second_choice'], _['third_choice'])
        applicants.append(applicant)

    return applicants


def new_sort_applicants(applicants_sorted_lst: list, c: int) -> dict:
    """assign applicants to the proper department first by the first_choice, next second choice...,
    sort applicants list inside dict, check if there aren't same applicants in different departments"""

    departments = {'Biotech': [],
                   'Chemistry': [],
                   'Engineering': [],
                   'Mathematics': [],
                   'Physics': []
                   }
    added_applicants = []

    for applicant in applicants_sorted_lst:
        if applicant not in added_applicants:
            if len(departments[applicant.first_choice]) < c:
                departments[applicant.first_choice].append(applicant)
                added_applicants.append(applicant)

    for applicant in applicants_sorted_lst:
        if applicant not in added_applicants:
            if len(departments[applicant.second_choice]) < c:
                departments[applicant.second_choice].append(applicant)
                added_applicants.append(applicant)

    for applicant in applicants_sorted_lst:
        if applicant not in added_applicants:
            if len(departments[applicant.third_choice]) < c:
                departments[applicant.third_choice].append(applicant)
                added_applicants.append(applicant)

    # sort lists inside departments dict according to GPA
    for applicants_lst in departments.values():
        applicants_lst.sort(key=lambda x: x.GPA, reverse=True)

    return departments

