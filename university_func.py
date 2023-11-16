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





