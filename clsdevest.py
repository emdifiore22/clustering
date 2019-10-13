import json
import sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def cluster_deviance_estimation():

    user_input = []

    for par in sys.argv:
        user_input.append(par)

    print ("### This script will find the number of cluster with maximum of " + user_input[1] + "% of lost deviance")
    print ("### Add '-g' to get the associated graph")
    print ("### (this is only an estimation and this values are not exact)")

    # read file
    with open('clustering_history.json', 'r') as myfile:
        data = myfile.read()

    # parse file
    obj = json.loads(data)
    history = obj['prova']

    # show values
    # print(str(history[len(history)-1]))
    max_distance = float(history[len(history)-1]['Distanza'])

    # axes
    x = []
    y = []

    for hist_elem in history:
        # estimation of lost deviance for each number of cluster
        estimation = 100 * float(hist_elem['Distanza'])/max_distance
        x.append(hist_elem['Numero di cluster'])
        y.append(estimation)
        # print values on command line
        print (hist_elem['Numero di cluster'] + "   " + hist_elem['Distanza'] + "   ==> " + str(estimation))

    i = 0
    for prob in y:
        if prob < float(user_input[1]):
            last = i
            # print("I found this: " + str(prob) + " ==> " + str(x[i]))
        i += 1

    print ("===> Estimation: " + str(y[last]) + " /" + str(x[last]))

    if len(user_input) == 3:
        if user_input[2] == "-g":
            plt.plot(x, y)
            plt.axis([0, 50, 0, 50])
            plt.axvline(x=x[last], color='r')
            plt.xlabel('number of cluster')
            plt.ylabel('lost variance (% not exact)')
            plt.show()


cluster_deviance_estimation()

