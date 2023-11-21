def mean_score(a: int, b: int, c: int) -> float:
    """Just simple average from 3 numbers"""
    mean = (a + b + c) / 3
    return mean


def bar_level(mean: float) -> str:
    """Check the score and return proper message"""
    if mean >= 60:
        message = 'Congratulations, you are accepted!'
    else:
        message = 'We regret to inform you that we will not be able to offer you admission.'

    return message


def make_a_dict(a: int) -> dict:
    """Make a dictionary"""
    applicants_dict = dict()
    while a != 0:
        applicant = input()
        name = ' '.join(applicant.split()[0:2])
        score = float(applicant.split()[2])
        if name not in applicants_dict:
            applicants_dict.update({name: score})
        a -= 1

    return applicants_dict


def sort_output_func(b: int, applicants_dict: dict) -> list:
    """Sort the dictionary according to score and if score the same alphabetically"""
    # sort by the name
    sorted_name_dict = dict(sorted(applicants_dict.items()))
    # sort by the score
    sorted_applicants_dict = dict(sorted(sorted_name_dict.items(), key=lambda item: -item[1]))
    message_lst = ['Successful applicants:']
    for name in sorted_applicants_dict.keys():
        if b != 0:
            message_lst.append(name)
            b -= 1
        else:
            break
    return message_lst


def read_file() -> list:
    """Read file, for every applicant make dict with needed date, make a list with all dict"""
    applicants_lst = []
    with open('applicant_list.txt', 'r') as file:
        applicants = file.readlines()
        for line in applicants:
            applicants_dict = dict()
            line = line.split()
            name = ' '.join(line[0:2])
            score = float(line[2])
            first_choice = line[3]
            second_choice = line[4]
            third_choice = line[5]
            applicants_dict.update({
                'name': name,
                'GPA': score,
                'first_choice': first_choice,
                'second_choice': second_choice,
                'third_choice': third_choice
            })
            applicants_lst.append(applicants_dict)

    return applicants_lst


def sort_read_file(applicants_lst: list) -> list:
    """Sort by name and next by GPA"""
    applicants_name_lst = sorted(applicants_lst, key=lambda x: x['name'])[::-1]
    applicants_sorted_lst = sorted(applicants_name_lst, key=lambda x: x['GPA'])[::-1]
    return applicants_sorted_lst


# def choice_list(applicants_lst: list):
#     """Make 3 dict with departments according to applicant priority choice"""
#
#     first_choice = {'Biotech': [],
#                    'Chemistry': [],
#                    'Engineering': [],
#                    'Mathematics': [],
#                    'Physics': []
#                    }
#     second_choice = {'Biotech': [],
#                    'Chemistry': [],
#                    'Engineering': [],
#                    'Mathematics': [],
#                    'Physics': []
#                    }
#     third_choice = {'Biotech': [],
#                    'Chemistry': [],
#                    'Engineering': [],
#                    'Mathematics': [],
#                    'Physics': []
#                    }
#
#     for applicant in applicants_lst:
#         name_gpa = f"{applicant['name']} {applicant['GPA']}"
#         if applicant['first_choice'] in first_choice:
#             first_choice[applicant['choice_num']].append(name_gpa)
#         if applicant['second_choice'] in second_choice:
#             second_choice[applicant['choice_num']].append(name_gpa)
#         if applicant['third_choice'] in third_choice:
#             third_choice[applicant['choice_num']].append(name_gpa)
#
#     return first_choice, second_choice, third_choice


# def new_sort_applicants(applicants_sorted_lst: list, c: int) -> dict:
#
#     departments = {'Biotech': [],
#                    'Chemistry': [],
#                    'Engineering': [],
#                    'Mathematics': [],
#                    'Physics': []
#                    }
#     added_applicants = []
#
#     for applicant in applicants_sorted_lst:
#         if applicant not in added_applicants:
#             if len(departments[applicant['first_choice']]) < c:
#                 departments[applicant['first_choice']].append(applicant)
#                 added_applicants.append(applicant)
#
#     for applicant in applicants_sorted_lst:
#         if applicant not in added_applicants:
#             if len(departments[applicant['second_choice']]) < c:
#                 departments[applicant['second_choice']].append(applicant)
#                 added_applicants.append(applicant)
#
#     for applicant in applicants_sorted_lst:
#         if applicant not in added_applicants:
#             if len(departments[applicant['third_choice']]) < c:
#                 departments[applicant['third_choice']].append(applicant)
#                 added_applicants.append(applicant)
#
#     # sort lists inside departments dict according to GPA
#     for applicants_lst in departments.values():
#         applicants_lst.sort(key=lambda x: x['GPA'], reverse=True)
#
#     return departments






