import pandas as pd


class Patient:

    def __init__(self, name, id_no, age):
        self.name = name
        self.id_no = id_no
        self.age = age
        self.tests = []

    def __repr__(self):
        return "{}: {}".format(self.name, self.id_no)


def class_work():
    new_patient = Patient("Ann Ables", 24, 33)
    return new_patient


def create_database_entry(patient_name: str, id_no, age):
    new_patient = Patient(patient_name, id_no, age)
    return new_patient


def main():
    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    db[x.id_no] = x
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 33, 33)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x

    #patient_id_tested = 24
    #test_done = ("HDL", 65)

    #patient = get_patient(db, patient_id_tested)
    #patient[3].append(test_done)

    #df = pd.DataFrame(db)
    print(db)#, df)


def print_database(db):
    locations = ["room 1", "room 4", "ER", "post-op"]
    for i, (patient, location) in enumerate(zip(db, locations)):
        print("{} - {} - {}".format(i, patient, location))


def print_patients_over_age(age, db):
    x = [patient for patient in db if patient[2] > age]
    for i in x:
        print(i[0])


def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient


if __name__ == "__main__":
    main()
