"""
Student Name - Simran Singh GULATI
Student ID - 31125301
Date Created - June 01, 2020
Last Modified - June 04, 2020

Overview:
The program creates a Person class which allows creation of objects for records stored in the text-file.
The data is cleaned and split in to segmented lists for simplicity. Additionally the social connections for each person
object are stored within a separate list. We also maintain a dictionary which stores the  object value for each person.
This dictionary is used for searching the object value by using the person's name which is utilised while adding the
social connections. Thus the program is aimed at creating objects and mapping their social connections.

"""
class Person:
    # each object is initialised with a first name and last name
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = list() # to store references to other objects

    # to add social connections for each object
    def add_friend(self, friend_person):
        self.friend_person = friend_person
        self.friends.append(self.friend_person)

    # to return name of the associated object
    def get_name(self):
        return self.first_name + " " + self.last_name

    # to return objects of a person's friends
    def get_friends(self):
        return self.friends

"""
objective :
1. retrieve data from data-set
2. create an object for each record in the file
3. call add_friend() for each friend
4. return a list of objects
"""
def load_people():
    # initiating an empty list to import data from text file
    data = []

    # open given file in read mode
    with open('a2_sample_set.txt', 'r') as file:
        # store each line in the file into the list created above - data[]
        for record in file:
            data.append(record.strip().replace(":", ",").split(", "))

    # extract the person's name and friends-list onto two separate lists
    people_list = []
    friends_list = []
    for record in data:
        people_list.append(record[0].split()) # need first and last name separately for the class constructor
        friends_list.append(record[1:])

    # creating an object for each name in people_list and storing objects in a new list
    person_object_list = []
    for each_person in people_list:
        person_object_list.append(Person(each_person[0],each_person[1]))

    # call get_name() on every object
    names_list = []
    for each_object in person_object_list:
        names_list.append(each_object.get_name())

    # combine names and their respective objects in a dictionary
    name_object = dict(zip(names_list, person_object_list))

    """
    flow :
    1. iterate over each person's friends
    2. look up each friend's associated object via name_object dictionary
    3. call add_friend() with friend's object as parameter
    """

    for person, friends in zip(person_object_list, friends_list):
        for friend in friends:
            person.add_friend(name_object[friend])

    return person_object_list

if __name__ == '__main__':
    load_people()
