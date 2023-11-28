import university_func
import data

if __name__ == '__main__':

    c = int(input())

    applicants_unsorted_lst = data.read_file()
    applicants_sorted_lst = university_func.sort_read_file(applicants_unsorted_lst)
    departments = data.new_sort_applicants(applicants_sorted_lst, c)
    data.save_to_file(departments)

