from BMI.get_inputs import get_height_input, get_weight_input
from BMI.utils import print_results, imp2si, sig_fig_round


def bmi_calc(weight, height):
    """function which takes a person's height and weight as a dictionary
    containing units, or as numbers alone assuming those are in si units,
    and returns their Body Mass Index (BMI) in kg/m^2 """
    si_weight = imp2si(weight, 2.205)  # lb / 2.205 = kg
    si_height = imp2si(height, 39.07)  # in / 39.07 = m

    bmi = sig_fig_round(si_weight / (si_height ** 2), 4)

    return bmi


def bmi_main():
    """The main calculation function"""
    weight = get_weight_input()
    height = get_height_input()
    bmi = bmi_calc(weight, height)
    print_results(bmi)


if __name__ == "__main__":
    bmi_main()
