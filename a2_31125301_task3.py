"""
Student Name - Simran Singh GULATI
Student ID - 31125301
Date Created - June 08, 2020
Last Modified - June 08, 2020

On plotting graphs for the given scenarios, we conclude :
Scenario A : Yes, results match the prediction as the count escalates exponentially between day 5 and 20 and hits 200 very quickly.
Scenario B : Considering it an unlucky case, we see a gradual spread spread in the virus. Not as sudden as the Scenario A but the virus does hit a total count of 80+ cases.
Scenario C : There's an unprecedented rise and fall in number of cases by a unit or two. The curve doesn't flatten out, instead it barely grows and hits a low count of 7 cases at the 90th day.
"""

from a2_31125301_task2 import *
import matplotlib.pyplot as plt

# to plot day vs count graph
def visual_curve(days, meeting_probability, patient_zero_health):
    # call run_simulation and store the results for plotting
    result = run_simulation(days, meeting_probability, patient_zero_health)
    print(result)
    # plot graph with number of days on X axis and patient count on Y axis
    plt.plot(result)
    plt.xlabel('Days')
    plt.ylabel('Count')
    plt.show()

if __name__ == '__main__':

    days = int(input("Enter number of days: "))
    meeting_probability = float(input("Enter meeting probability: "))
    patient_zero_health = int(input("Enter health of Patient Zero: "))

    visual_curve(days, meeting_probability, patient_zero_health)

