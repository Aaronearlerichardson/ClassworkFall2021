import re
import math


def imp2si(value, div):
    """Takes a height or weight measurement in imperial units and divides that number by the appropriate constant to
    convert it to si units. If si units are given, si units will be returned. For units to be interpreted,
    inputs must be formatted as a dictionary with value = number and units = unit. Otherwise, this function returns
    the number given. """
    num_div = num_counter(div)
    if isinstance(value, dict):
        if is_imperial(value["units"]):
            return sig_fig_round(value["value"] / div, num_div)
        else:
            return value["value"]
    elif isinstance(value, (int, float)):
        return value
    else:
        raise ValueError("must be a number or dict")


def sig_fig_round(number, digits):
    "Rounds a number to a given amount of significant figures"
    integer_part = math.floor(number)
    sig_num = round(number, digits - len(str(integer_part)))
    return sig_num


def num_counter(num):
    "function that counts the number of significant digits in a given number"
    num = str(float(num))
    count = 0
    flipper = False
    for item in num.split("."):
        if flipper:
            while item.startswith("0"):
                item = item.lstrip("0")
        if item != "0":
            count += len(item)
        else:
            flipper = True

    return count


def is_imperial(unit):
    "checks string input to see if it matches any variation of the signs for pounds or inches"
    imperial_patterns = ("(?:in)(?:ch(?:es)?)?", "lbs?", "[Pp]ounds?")
    if any(re.match(pattern, unit) for pattern in imperial_patterns):
        return True
    else:
        return False


def eval_bmi(bmi_num: (int, float)):
    "This function evaluates the given bmi and places it in a clinical category"
    if bmi_num < 16.5:
        return "Severely Underweight"
    elif 16.5 <= bmi_num < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_num < 25:
        return "Normal"
    elif 25 <= bmi_num < 30:
        return "Overweight"
    else:  # bmi > 30
        return "Obese"


def print_results(bmi_num: (int, float)):
    "This prints the result of the clinical categorization"
    result = eval_bmi(bmi_num)
    print("The given BMI is {} which is clinically categorized as {}".format(bmi_num, result))


if __name__ == "__main__":
    bmi = float(input("what is bmi?"))
    print_results(bmi)
