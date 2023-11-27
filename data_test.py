import pytest
from data import Applicant
import data


def test_applicant_creation():
    applicant = Applicant(name="Aduś Zaduś", GPA=3.5, first_choice='Physics', second_choice="Biotech",
                          third_choice="Chemistry")

    assert applicant.name == 'Aduś Zaduś'
    assert applicant.GPA == 3.5
    assert applicant.first_choice == 'Physics'
    assert applicant.second_choice == 'Biotech'
    assert applicant.third_choice == 'Chemistry'


def test_new_sort_applicants(sample_sorted_applicants_list):
    applicants_lst = data.applicants_lst(sample_sorted_applicants_list)
    applicants_dict = data.new_sort_applicants(applicants_lst, 3)


    result = {'Biotech': [Applicant(name='Adrian Keefe', GPA=4.14, first_choice='Biotech', second_choice='Physics',
                                    third_choice='Chemistry')],
              'Chemistry': [Applicant(name='Natha Gryn', GPA=3.14, first_choice='Chemistry', second_choice='Biotech',
                                      third_choice='Physics')],
              'Engineering': [Applicant(name='Natha Keefe', GPA=3.14, first_choice='Engineering', second_choice='Biotech',
                                        third_choice='Chemistry')],
              'Mathematics': [Applicant(name='Adam Smith', GPA=2.14, first_choice='Mathematics', second_choice='Biotech',
                                        third_choice='Chemistry')],
              'Physics': [Applicant(name='Joe Doe', GPA=3.14, first_choice='Physics', second_choice='Biotech',
                                    third_choice='Chemistry')]
              }

    assert result == applicants_dict
