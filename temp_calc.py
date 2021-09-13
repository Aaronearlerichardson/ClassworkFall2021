def detect_fever(temp_list):
    fever_limit = 100.0
    for temp in temp_list:
        if temp >= fever_limit:
            return True
    return False
