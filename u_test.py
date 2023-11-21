from unittest import mock
import university_func
from university_func import mean_score, bar_level, make_a_dict, sort_output_func, department_best_candidates
import pytest
from io import StringIO


def test_mean_score():
    assert mean_score(1, 1, 1) == 1
    assert mean_score(-1, -2, -3) == -2
    assert mean_score(0, 0, 0) == 0
    assert mean_score(10, -5, 3) == 2.6666666666666665
    assert mean_score(10, 10, 10) == 10


def test_bar_level():
    assert bar_level(60) == 'Congratulations, you are accepted!'
    assert bar_level(59) == 'We regret to inform you that we will not be able to offer you admission.'
    assert bar_level(-4) == 'We regret to inform you that we will not be able to offer you admission.'
    assert bar_level(0) == 'We regret to inform you that we will not be able to offer you admission.'
    assert bar_level(100) == 'Congratulations, you are accepted!'


def test_make_a_dict(monkeypatch):
    input_data = "Alice Adams 85.5\nBob Brown 92.0\nCharlie Clark 77.5\nDavid Davis 92.0\nEva Evans 88.5\n"
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    result = make_a_dict(5)

    assert result == {
        'Alice Adams': 85.5,
        'Bob Brown': 92.0,
        'Charlie Clark': 77.5,
        'David Davis': 92.0,
        'Eva Evans': 88.5
    }


def test_sort_output_func():
    applicants_dict = {'Alice Adams': 85.5, 'Bob Brown': 92.0}
    result = ['Successful applicants:', 'Bob Brown']
    assert sort_output_func(1, applicants_dict) == result


@mock.patch('university_func.read_file')
def test_read_file(mock_read_file):
    """ this test do not check sort feature of function"""
    mock_read_file.return_value = [{
        'name': 'Natha Keefe',
        'GPA': 3.14,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }]
    application_lst = university_func.read_file()

    assert application_lst == [{
        'name': 'Natha Keefe',
        'GPA': 3.14,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }]


def test_read_file_sorted():
    applicants = [{
        'name': 'Natha Keefe',
        'GPA': 3.14,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    },
        {
            'name': 'Aaaa Aaaa',
            'GPA': 3.14,
            'first_choice': 'Engineering',
            'second_choice': 'Biotech',
            'third_choice': 'Chemistry'
        },
        {
            'name': 'Zzz Zzz',
            'GPA': 5.14,
            'first_choice': 'Engineering',
            'second_choice': 'Biotech',
            'third_choice': 'Chemistry'
        }
    ]
    application_lst = university_func.sort_read_file(applicants)

    assert application_lst == [{
        'name': 'Zzz Zzz',
        'GPA': 5.14,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    },
        {
            'name': 'Aaaa Aaaa',
            'GPA': 3.14,
            'first_choice': 'Engineering',
            'second_choice': 'Biotech',
            'third_choice': 'Chemistry'
        },
        {
            'name': 'Natha Keefe',
            'GPA': 3.14,
            'first_choice': 'Engineering',
            'second_choice': 'Biotech',
            'third_choice': 'Chemistry'
        }
    ]


# @pytest.fixture
# def sample_applicants_sorted_lst():
#     return [
#         {'name': 'Applicant1', 'GPA': 3.8, 'first_choice': 'Biotech', 'second_choice': 'Engineering',
#          'third_choice': 'Physics'},
#     ]


def test_department_best_candidates():
    c = 2

    sample_application_lst = [
        {'name': 'Applicant1', 'GPA': 3.8, 'first_choice': 'Biotech', 'second_choice': 'Engineering',
         'third_choice': 'Physics'},
    ]

    result = department_best_candidates(c, sample_application_lst)

    assert len(result['Biotech']) <= c
    assert len(result['Chemistry']) <= c
    assert len(result['Engineering']) <= c
    assert len(result['Mathematics']) <= c
    assert len(result['Physics']) <= c

    assert 'Applicant1 3.8' in result['Biotech']

# def test_department_best_cadidates():
#     applicants_sorted_lst_1 = [{
#         'name': 'Natha Keefe',
#         'GPA': 3.14,
#         'first_choice': 'Engineering',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }, {
#         'name': 'Adrian Keefe',
#         'GPA': 3.14,
#         'first_choice': 'Biotech',
#         'second_choice': 'Physics',
#         'third_choice': 'Chemistry'
#     }, {
#         'name': 'Natha Gryn',
#         'GPA': 3.14,
#         'first_choice': 'Chemistry',
#         'second_choice': 'Biotech',
#         'third_choice': 'Physics'
#     }, {
#         'name': 'Joe Doe',
#         'GPA': 3.14,
#         'first_choice': 'Physics',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }, {
#         'name': 'Adam Smith',
#         'GPA': 3.14,
#         'first_choice': 'Mathematics',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }]
#
#     applicants_sorted_lst_2 = [{
#         'name': 'Natha Keefe',
#         'GPA': 3.14,
#         'first_choice': 'Engineering',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }, {
#         'name': 'Adrian Keefe',
#         'GPA': 3.14,
#         'first_choice': 'Biotech',
#         'second_choice': 'Physics',
#         'third_choice': 'Chemistry'
#     }, {
#         'name': 'Natha Gryn',
#         'GPA': 3.14,
#         'first_choice': 'Chemistry',
#         'second_choice': 'Biotech',
#         'third_choice': 'Physics'
#     }, {
#         'name': 'Joe Doe',
#         'GPA': 3.14,
#         'first_choice': 'Physics',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }]
#     result_1 = university_func.department_best_candidates(1, applicants_sorted_lst_1)
#     expected_result_1 = [['Biotech', 'Adrian Keefe 3.14'],
#                        ['\nChemistry', 'Natha Gryn 3.14'],
#                        ['\nEngineering', 'Natha Keefe 3.14'],
#                        ['\nMathematics', 'Adam Smith 3.14'],
#                        ['\nPhysics', 'Joe Doe 3.14']]
#
#     result_2 = university_func.department_best_candidates(1, applicants_sorted_lst_2)
#     expected_result_2 = [['Biotech', 'Adrian Keefe 3.14'],
#                        ['\nChemistry', 'Natha Gryn 3.14'],
#                        ['\nEngineering', 'Natha Keefe 3.14'],
#                        ['\nMathematics'],
#                        ['\nPhysics', 'Joe Doe 3.14']]
#
#     assert result_1 == expected_result_1
#     assert result_2 == expected_result_2
