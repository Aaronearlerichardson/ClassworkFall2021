from BMI import bmi_calc

print("this is the blood_calc.py module")
print("It's name is {} ".format(__name__))


def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL analysis")
        print("2 - LDL analysis")
        print("3 - cholesterol analysis")
        print("4 - BMI calculation")
        print("9 - Quit")
        choice = input("Make a choice:\n")
        if not choice.isnumeric():
            print("Make your choice a number")
            continue
        choice = int(choice)
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_driver()
        elif choice == 2:
            LDL_driver()
        elif choice == 3:
            cholesterol_driver()
        elif choice == 4:
            bmi_calc.bmi_main()
    return


def HDL_driver():
    HDL_value = dl_input("HDL")
    HDL_answer = hdl_eval(HDL_value)
    dl_output("HDL", HDL_value, HDL_answer)


def dl_input(stat):
    hdl_value = int(input("Enter {} value ".format(stat)))
    return hdl_value


def dl_output(stat, DL_value, DL_answer):
    print("The {} value of {} is considered {}".format(stat,
                                                       DL_value,
                                                       DL_answer))
    return


def hdl_eval(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline low"
    else:
        return "Low"


def LDL_driver():
    ldl_input = dl_input("LDL")
    result = eval_LDL(ldl_input)
    dl_output("LDL", ldl_input, result)


def eval_LDL(LDL_val: int):
    if LDL_val >= 190:
        LDL_out = "very high"
    elif LDL_val >= 160:
        LDL_out = "high"
    elif LDL_val >= 130:
        LDL_out = "borderline high"
    else:
        LDL_out = "normal"

    return LDL_out


def cholesterol_driver():
    chol_val = dl_input("cholesterol")
    result = cholesterol_eval(chol_val)
    dl_output("cholesterol", chol_val, result)


def cholesterol_eval(val):
    if val > 240:
        return "High"
    elif val > 200:
        return "Borderline high"
    else:
        return "normal"


if __name__ == "__main__":
    interface()
