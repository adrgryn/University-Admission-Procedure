import university_func
import data

if __name__ == '__main__':

    c = int(input())

    applicants_unsorted_lst = university_func.read_file()
    applicants_sorted_lst = university_func.sort_read_file(applicants_unsorted_lst)
    applicants_data_lst = data.applicants_lst(applicants_sorted_lst)
    departments = data.new_sort_applicants(applicants_data_lst, c)

    for key, values in departments.items():
        print(f'\n{key}')
        for value in values:
            # name_gpa = f"{value['name']} {value['GPA']}"
            # print(value)
            print(f"{value.name} {value.GPA}")




