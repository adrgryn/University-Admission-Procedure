import university_func
import data

if __name__ == '__main__':
    while True:
        try:
            c = int(input("Define possible numbers of students for department\n"))
            break
        except ValueError:
            print('Your input should be a digit\n')

    applicants_unsorted_lst = data.read_file()
    applicants_sorted_lst = university_func.sort_read_file(applicants_unsorted_lst)
    departments = data.new_sort_applicants(applicants_sorted_lst, c)
    print(departments)
    data.save_to_file(departments)

