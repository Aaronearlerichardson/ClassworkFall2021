import pandas as pd


def create_database_entry(patient_name: str, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient


def main():
    db = []
    x = create_database_entry("Ann Ables", 120, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 24, 31)
    db.append(x)
    x = create_database_entry("Chris Chou", 33, 33)
    db.append(x)
    x = create_database_entry("David Dinkins", 14, 34)
    db.append(x)
    
    patient_id_tested = 24
    test_done = ("HDL", 65)
    
    patient = get_patient(db, patient_id_tested)
    patient[3].append(test_done)
    
    db = pd.Dataframe(db)
    var = pd.Dataframe

    print_database(db)


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
