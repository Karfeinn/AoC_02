def open_ids():
    with open("ids.txt", mode="r", encoding="utf-8") as id_file :
        interval_list = id_file.read().split(",")
    return interval_list

def is_id_valid(number):
    text_number = str(number)
    if len(text_number)%2 !=0 :
        return True

    first_part = text_number[:int(len(text_number)/2)]
    last_part = text_number[int(len(text_number)/2):]
    if first_part == last_part :
        return False
    
    return True

def all_id_in_interval(interval):
    ids_list = []
    limits = interval.split("-")
    id = int(limits[0])
    while id <= int(limits[1]):
        ids_list.append(id)
        id +=1
    return ids_list

def add_invalid_id():
    interval_list = open_ids()
    invalid_ids = []
    for interval in interval_list :
        ids_list = all_id_in_interval(interval)
        for id in ids_list :
            if not is_id_valid(id):
                invalid_ids.append(id)
    return sum(invalid_ids)

print(add_invalid_id())