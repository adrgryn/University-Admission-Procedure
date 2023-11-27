import university_func
import data

if __name__ == '__main__':

    c = int(input())

    applicants_unsorted_lst = data.read_file()
    applicants_sorted_lst = university_func.sort_read_file(applicants_unsorted_lst)
    departments = data.new_sort_applicants(applicants_sorted_lst, c)

    for key, values in departments.items():
        print(f'\n{key}')
        if key == "Biotech":
            for value in values:
                # print(value)
                print(f"{value.name} {value.chemistry_score}")
        if key == "Chemistry":
            for value in values:
                # print(value)
                print(f"{value.name} {value.chemistry_score}")
        if key == "Engineering":
            for value in values:
                # print(value)
                print(f"{value.name} {value.computer_science}")
        if key == "Mathematics":
            for value in values:
                # print(value)
                print(f"{value.name} {value.math_score}")
        if key == "Physics":
            # print(values)
            for value in values:
                # print(value)
                print(f"{value.name} {value.physic_score}")


