"""
Student Name - Simran Singh GULATI
Student ID - 31125301
Date Created - June 05, 2020
Last Modified - June 07, 2020

Overview:
The program aims at creating objects for the patient records stored in text file and maps them to their associated friends.
Each object is initialised with a first name, last name and some initial health points. Followed by running a simulation
to model the spread of disease from one patient to another achieved via the use of certain rules guiding the people's
meeting probability and change in health points for every interaction. Lastly the program records the number of
contagious patients at the end of each day.
"""
from a2_31125301_task1 import *
import random

class Patient(Person):
    # class constructor
    def __init__(self, first_name, last_name, health):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.friends = list()

    # return patient's health point
    def get_health(self):
        return self.health

    # sets patient's health points
    def set_health(self, new_health):
        self.new_health = new_health
        self.health = new_health

    # returns if a patient is contagious or not
    def is_contagious(self):
        if self.health<50:
            return True
        else:
            return False

    # to infect patient objects with a viral load value
    def infect(self, viral_load):

        self.viral_load = viral_load

        # health points before meeting
        hp_a = self.get_health()

        if hp_a <= 29:
            hp_b = hp_a - (0.1 * viral_load)
        elif  29 < hp_a < 50:
            hp_b = hp_a - (1 * viral_load)
        else:
            # for health points 50 and above
            hp_b = hp_a - (2 * viral_load)

        if hp_b < 0:
            # minimum health possible is zero
            hp_b = 0

        # update health points after meeting
        self.set_health(hp_b)

    # each day when patient sleeps, he recovers 5 health points
    def sleep(self):
        # maximum health is set to 100
        if self.health > 95:
            self.health = 100
        else:
            self.health += 5


"""
flow of code :
1. run simulation for each day
2. iterate over each patient every day
3. check if a patient is contagious or not
4. skip to next patient if not contagious OTHERWISE infect friends
5. check if a friend is also contagious and infect patient
6. record number of contagious patients at the end of each day in a list
"""
def run_simulation(days, meeting_probability, patient_zero_health):
    # call load_patient to create objects and initialise default health for every object
    patients = load_patients(75)
    # alter patient zero's health as per test case
    patients[0].set_health(patient_zero_health)

    # initialise an empty list to keep track of contagious count each day
    contagious_people =[]

    for day in range(days):
        count = 0
        for patient in patients:
            for friend in patient.get_friends():
                chance = random.random()
                if chance <= meeting_probability:

                    if patient.is_contagious():
                        # health points of the patient transmitting the viral load
                        hp_c = patient.get_health()
                        # viral load the patient passes
                        lv = 5 + ((hp_c - 25) ** 2) / 62
                        # friend who has to be infected
                        friend.infect(lv)

                    if friend.is_contagious():
                        # health points of the friend transmitting back to the patient
                        hp_c = friend.get_health()
                        # viral load the friend transmits
                        lv = 5 + ((hp_c - 25) ** 2) / 62
                        patient.infect(lv)

        for patient in patients:
            if patient.is_contagious():
                # record patient count
                count+=1
            patient.sleep()
        contagious_people.append(count)

    return contagious_people

def load_patients(initial_health):
    # initiating an empty list to import data from text file
    data = []

    # open given file in read mode
    with open('a2_sample_set.txt', 'r') as file:
        # store each line in the file into the list created above - data[]
        for record in file:
            data.append(record.strip().replace(":", ",").split(", "))

    # data[] contains 200 records with the patients's name and a list of their friends
    # extract the patient names and friends-list onto two separate lists
    patient_list = []
    friends_list = []
    for record in data:
        patient_list.append(record[0].split())  # need first and last name separately for the class constructor
        friends_list.append(record[1:])

    # creating an object for each name in people_list and storing objects in a new list
    patient_object_list = []
    for each_patient in patient_list:
        patient_object_list.append(Patient(each_patient[0], each_patient[1], initial_health))

    # call get_name() on every object
    names_list = []
    for each_object in patient_object_list:
        names_list.append(each_object.get_name())

    # combine names and their respective objects in a dictionary
    name_object = dict(zip(names_list, patient_object_list))

    """
    1. iterate over each patient's friends
    2. look up each friend's associated object in name_object dictionary
    3. call add_friend() with friend's object
    """

    for person, friends in zip(patient_object_list, friends_list):
        for friend in friends:
            person.add_friend(name_object[friend])

    return patient_object_list


if __name__ == '__main__':

    # test_result = run_simulation(15, 0.8, 49)
    # print(test_result)

    test_result = run_simulation(40, 1, 1)
    print(test_result)

    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
