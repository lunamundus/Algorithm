while True:
    len_list = sorted(list(map(int, input().split())))
    
    if len_list[0] == len_list[1] == len_list[2] == 0:
        break

    if len_list[2] ** 2 == len_list[0] ** 2 + len_list[1] ** 2:
        print("right")
    else:
        print("wrong")