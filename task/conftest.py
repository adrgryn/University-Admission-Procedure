import pytest

@pytest.fixture
def sample_applicants_list():
    return [{
        'name': 'Natha Keefe',
        'physics_GPA': 3.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adrian Keefe',
        'physics_GPA': 4.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 3.12,
        'computer_science': 5.54,
        'first_choice': 'Biotech',
        'second_choice': 'Physics',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Natha Gryn',
        'physics_GPA': 2.14,
        'chemistry_GPA': 3.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Chemistry',
        'second_choice': 'Biotech',
        'third_choice': 'Physics'
    }, {
        'name': 'Joe Doe',
        'physics_GPA': 5.14,
        'chemistry_GPA': 5.12,
        'math_GPA': 4.12,
        'computer_science': 3.54,
        'first_choice': 'Physics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adam Smith',
        'physics_GPA': 4.14,
        'chemistry_GPA': 2.12,
        'math_GPA': 3.12,
        'computer_science': 4.54,
        'first_choice': 'Mathematics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }]


@pytest.fixture()
def sample_sorted_applicants_list():
    return [[{
        'name': 'Joe Doe',
        'physics_GPA': 5.14,
        'chemistry_GPA': 5.12,
        'math_GPA': 4.12,
        'computer_science': 3.54,
        'first_choice': 'Physics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adam Smith',
        'physics_GPA': 4.14,
        'chemistry_GPA': 2.12,
        'math_GPA': 3.12,
        'computer_science': 4.54,
        'first_choice': 'Mathematics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adrian Keefe',
        'physics_GPA': 4.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 3.12,
        'computer_science': 5.54,
        'first_choice': 'Biotech',
        'second_choice': 'Physics',
        'third_choice': 'Chemistry'
    },{
        'name': 'Natha Keefe',
        'physics_GPA': 3.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Natha Gryn',
        'physics_GPA': 2.14,
        'chemistry_GPA': 3.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Chemistry',
        'second_choice': 'Biotech',
        'third_choice': 'Physics'
    }], [{
        'name': 'Joe Doe',
        'physics_GPA': 5.14,
        'chemistry_GPA': 5.12,
        'math_GPA': 4.12,
        'computer_science': 3.54,
        'first_choice': 'Physics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adrian Keefe',
        'physics_GPA': 4.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 3.12,
        'computer_science': 5.54,
        'first_choice': 'Biotech',
        'second_choice': 'Physics',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Natha Keefe',
        'physics_GPA': 3.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Natha Gryn',
        'physics_GPA': 2.14,
        'chemistry_GPA': 3.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Chemistry',
        'second_choice': 'Biotech',
        'third_choice': 'Physics'
    }, {
        'name': 'Adam Smith',
        'physics_GPA': 4.14,
        'chemistry_GPA': 2.12,
        'math_GPA': 3.12,
        'computer_science': 4.54,
        'first_choice': 'Mathematics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }], [{
        'name': 'Natha Gryn',
        'physics_GPA': 2.14,
        'chemistry_GPA': 3.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Chemistry',
        'second_choice': 'Biotech',
        'third_choice': 'Physics'
    }, {
        'name': 'Natha Keefe',
        'physics_GPA': 3.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Joe Doe',
        'physics_GPA': 5.14,
        'chemistry_GPA': 5.12,
        'math_GPA': 4.12,
        'computer_science': 3.54,
        'first_choice': 'Physics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adam Smith',
        'physics_GPA': 4.14,
        'chemistry_GPA': 2.12,
        'math_GPA': 3.12,
        'computer_science': 4.54,
        'first_choice': 'Mathematics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adrian Keefe',
        'physics_GPA': 4.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 3.12,
        'computer_science': 5.54,
        'first_choice': 'Biotech',
        'second_choice': 'Physics',
        'third_choice': 'Chemistry'
    }], [{
        'name': 'Adrian Keefe',
        'physics_GPA': 4.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 3.12,
        'computer_science': 5.54,
        'first_choice': 'Biotech',
        'second_choice': 'Physics',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Adam Smith',
        'physics_GPA': 4.14,
        'chemistry_GPA': 2.12,
        'math_GPA': 3.12,
        'computer_science': 4.54,
        'first_choice': 'Mathematics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Natha Gryn',
        'physics_GPA': 2.14,
        'chemistry_GPA': 3.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Chemistry',
        'second_choice': 'Biotech',
        'third_choice': 'Physics'
    }, {
        'name': 'Natha Keefe',
        'physics_GPA': 3.14,
        'chemistry_GPA': 4.12,
        'math_GPA': 5.12,
        'computer_science': 4.54,
        'first_choice': 'Engineering',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, {
        'name': 'Joe Doe',
        'physics_GPA': 5.14,
        'chemistry_GPA': 5.12,
        'math_GPA': 4.12,
        'computer_science': 3.54,
        'first_choice': 'Physics',
        'second_choice': 'Biotech',
        'third_choice': 'Chemistry'
    }, ]]

