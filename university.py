from university_func import mean_score, bar_level, make_a_dict, sort_output_func


if __name__ == '__main__':

    a = int(input())
    b = int(input())
    applicants_dict = make_a_dict(a)
    out_list = sort_output_func(b, applicants_dict)
    for x in out_list:
        print(x)