import airlines
import matplotlib.pyplot as plt
import numpy as np


print("Welcome. We will give you a bar chart of delays caused by security issues in various airports across the U.S.")

airlines_data = airlines.get_data()

finalData = {}
for i in range(len(airlines_data)):
    if airport not in finalData:
        delays = airlines_data[i]["Airport"]["Code"]
        if airport not in finalData:
            delays = airlines_data[i]["Statistics"]["# of Delays"]["Security"]
            finalData.update({airport:delays})
        else:
            finalData[airport]+=airlines_data[i]["Statistics"]["# of Delays"]["Security"]
print(finalData)
plt.bar(range(len(finalData)), list(finalDAta.values()), align = 'center',color = "#50DBG6")
plt.xticks(range(len(finalData)), list(finalData.keys()))
plt.xlabel("Airports")
plt.ylabel("# of Delays")
plt.title("How many airport delays are caused by security issues?")
plt.xticks(color = 'black', rotation = 90, fontsize = '7', horizontalalignment = 'center')
plt.show()
save = input("Would you like to save this graph?\n")
if save == "yes"
    filename = input("What would you like to save this file as? \n")
    plt.savefig(filename+".png")
    print("Your file has been saved.")
else:
    print("Ok. Goodbye")
