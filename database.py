print("this is the database.py module")
print("It's name is {} ".format(__name__))

import blood_calc as bc

answer = bc.hdl_eval(55)

print("the analysis of 55 HDL is {}".format(answer))

answer2 = bc.eval_LDL(200)
