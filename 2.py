def find_common_participants(str1 , str2,spliter=",") :
    list1 = str1.split(spliter)
    list2 = str2.split(spliter)
    list3 = sorted(set(list1).intersection(list2))

    return list3



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group ,participants_second_group , "|" ))
