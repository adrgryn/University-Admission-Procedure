from university_func import mean_score, bar_level, make_a_dict, sort_output_func
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
