from data import Applicant

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


def sort_read_file(applicants_lst: list) -> list:
    """Sort by name and next by GPA"""
    applicants_name_lst = sorted(applicants_lst, key=lambda x: x.name, reverse=True)
    physics_sorted_lst = sorted(applicants_name_lst, key=lambda x: x.physic_score)[::-1]
    chemistry_sorted_lst = sorted(applicants_name_lst, key=lambda x: x.chemistry_score)[::-1]
    math_sorted_lst = sorted(applicants_name_lst, key=lambda x: x.math_score)[::-1]
    computer_science = sorted(applicants_name_lst, key=lambda x: x.computer_science)[::-1]
    applicants_sorted_lst = [physics_sorted_lst, chemistry_sorted_lst, math_sorted_lst, computer_science]
    return applicants_sorted_lst








