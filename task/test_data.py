import pytest
from data import Applicant
import data
from unittest import mock

# Create test applicants
applicants = [
    Applicant(name='Jermine Brunton', physics_score=78.5, chemistry_score=81.0, biotech_score=82.5,
              mathematics_score=73.0, engineering_score=82.5, special_exam_score=48.0, first_choice='Physics',
              second_choice='Engineering', third_choice='Mathematics'),
    Applicant(name='Justo Mirfin', physics_score=66.0, chemistry_score=77.0, biotech_score=74.0,
              mathematics_score=61.0, engineering_score=60.5, special_exam_score=41.0, first_choice='Engineering',
              second_choice='Biotech', third_choice='Chemistry'),
    Applicant(name='Uzma Naysmythe', physics_score=67.5,
              chemistry_score=94.0, biotech_score=77.0, mathematics_score=75.0, engineering_score=73.0,
              special_exam_score=80.0, first_choice='Chemistry', second_choice='Engineering', third_choice='Mathematics')
    ,
]

def test_applicant_creation():
    """Test the creation of an Applicant instance."""
    applicant = Applicant(
        name="John Doe",
        physics_score=80.0,
        chemistry_score=75.5,
        biotech_score=65.0,
        mathematics_score=90.0,
        engineering_score=85.0,
        special_exam_score=88.0,
        first_choice="Physics",
        second_choice="Chemistry",
        third_choice="Biotech"
    )
    assert applicant.name == "John Doe"
    assert applicant.physics_score == 80.0
    assert applicant.chemistry_score == 75.5
    assert applicant.biotech_score == 65.0
    assert applicant.mathematics_score == 90.0
    assert applicant.engineering_score == 85.0
    assert applicant.special_exam_score == 88.0
    assert applicant.first_choice == "Physics"
    assert applicant.second_choice == "Chemistry"
    assert applicant.third_choice == "Biotech"


def test_read_file():
    applicants = data.read_file()

    assert len(applicants) == 98  # assuming there are 98 applicants in your test file


@pytest.mark.parametrize("capacity", [1, 2, 3])
def test_new_sort_applicants(capacity):
    departments = data.new_sort_applicants(applicants, capacity)

    # Check that no department exceeds capacity
    for department, applicants_list in departments.items():
        assert len(applicants_list) <= capacity

    # # Check that every department has at least one applicant
    # for department, applicants_list in departments.items():
    #     assert len(applicants_list) != 0

    # Check for correct sorting within each department
    for department, applicants_list in departments.items():
        for i in range(len(applicants_list) - 1):
            current_applicant = applicants_list[i]
            next_applicant = applicants_list[i + 1]

            current_score = getattr(current_applicant, department.lower() + '_score')
            next_score = getattr(next_applicant, department.lower() + '_score')

            # Check for correct sorting by score and name
            assert current_score >= next_score or \
                   (current_score == next_score and current_applicant.name <= next_applicant.name)

    # # Check for unique assignment of applicants
    # seen_applicants = set()
    # for department, applicants_list in departments.items():
    #     for applicant in applicants_list:
    #         assert applicant not in seen_applicants
    #         seen_applicants.add(applicant)




# def test_new_sort_applicants(sample_sorted_applicants_list):
#     applicants_lst = data.applicants_lst(sample_sorted_applicants_list)
#     applicants_dict = data.new_sort_applicants(applicants_lst, 3)
#
#
#     result = {'Biotech': [Applicant(name='Adrian Keefe', GPA=4.14, first_choice='Biotech', second_choice='Physics',
#                                     third_choice='Chemistry')],
#               'Chemistry': [Applicant(name='Natha Gryn', GPA=3.14, first_choice='Chemistry', second_choice='Biotech',
#                                       third_choice='Physics')],
#               'Engineering': [Applicant(name='Natha Keefe', GPA=3.14, first_choice='Engineering', second_choice='Biotech',
#                                         third_choice='Chemistry')],
#               'Mathematics': [Applicant(name='Adam Smith', GPA=2.14, first_choice='Mathematics', second_choice='Biotech',
#                                         third_choice='Chemistry')],
#               'Physics': [Applicant(name='Joe Doe', GPA=3.14, first_choice='Physics', second_choice='Biotech',
#                                     third_choice='Chemistry')]
#               }
#
#     assert result == applicants_dict
#
# @mock.patch('university_func.read_file')
# def test_read_file(mock_read_file):
#     """ this test do not check sort feature of function"""
#     mock_read_file.return_value = [{
#         'name': 'Natha Keefe',
#         'physics_GPA': 3.14,
#         'chemistry_GPA': 3.54,
#         'math_GPA': 4.15,
#         'computer_science': 3.12,
#         'first_choice': 'Engineering',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }]
#     application_lst = data.read_file()
#
#     assert application_lst == [{
#         'name': 'Natha Keefe',
#         'physics_GPA': 3.14,
#         'chemistry_GPA': 3.54,
#         'math_GPA': 4.15,
#         'computer_science': 3.12,
#         'first_choice': 'Engineering',
#         'second_choice': 'Biotech',
#         'third_choice': 'Chemistry'
#     }]