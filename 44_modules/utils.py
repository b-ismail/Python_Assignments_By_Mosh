def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(input_list):
    highest = int(input_list[0])
    for item in input_list:
        if int(item) > highest:
            highest = int(item)
    return highest