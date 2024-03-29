# covid_simulation
Simulating the spread of COVID like Virus using Python and Probability Theory.

## Task 1 
The program creates a Person class which allows creation of objects for records stored in the text-file.
The data is cleaned and split in to segmented lists for simplicity. Additionally the social connections for each person
object are stored within a separate list. We also maintain a dictionary which stores the  object value for each person.
This dictionary is used for searching the object value by using the person's name which is utilised while adding the
social connections. Thus the program is aimed at creating objects and mapping their social connections.

Here's an example of what the program would do:

![python console screenshot](https://github.com/simransinghgulati/covid_simulation/blob/main/console_screenshot.png?raw=true)

In the next file, it autotmates this process for all the records in given text file.

## Task 2
The program aims at creating objects for the patient records stored in text file and maps them to their associated friends.
Each object is initialised with a first name, last name and some initial health points. Followed by running a simulation
to model the spread of disease from one patient to another achieved via the use of certain rules guiding the people's
meeting probability and change in health points for every interaction. Lastly the program records the number of
contagious patients at the end of each day.

## Task 3
On plotting graphs for the given scenarios, we conclude :

**Scenario A** : Yes, results match the prediction as the count escalates exponentially between day 5 and 20 and hits 200 very quickly.

![python terminal screenshot](https://github.com/simransinghgulati/covid_simulation/blob/main/terminal_A.png?raw=true)

![graph 1](https://github.com/simransinghgulati/covid_simulation/blob/main/scenario_A.png?raw=true)

**Scenario B** : Considering it an unlucky case, we see a gradual spread spread in the virus. Not as sudden as the Scenario A but the virus does hit a total count of 80+ cases.

![python terminal screenshot](https://github.com/simransinghgulati/covid_simulation/blob/main/terminal_B.png?raw=true)

![graph 2](https://github.com/simransinghgulati/covid_simulation/blob/main/scenario_B.png?raw=true)

**Scenario C** : There's an unprecedented rise and fall in number of cases by a unit or two. The curve doesn't flatten out, instead it barely grows and hits a low count of 7 cases at the 90th day.

![python terminal screenshot](https://github.com/simransinghgulati/covid_simulation/blob/main/terminal_C.png?raw=true)

![graph 3](https://github.com/simransinghgulati/covid_simulation/blob/main/scenario_C.png?raw=true)

## Simulation results
My algorithm received the highest grade in the class and below is the graphical represenation of the same.
![simulation](https://github.com/simransinghgulati/covid_simulation/blob/main/simulation_results.png?raw=true)
