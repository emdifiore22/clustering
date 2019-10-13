import json
import sys
from math import pow
import numpy as np

user_input = []
for par in sys.argv:
    user_input.append(par)

clusters = []
averages = []

for i in range(1, int(user_input[1])+1):
    array_cl = []
    clusters.append(array_cl)

npcomponents = int(user_input[2])
total_len = 0

def read_file():
    # read file
    with open('cluster_6.json', 'r') as myfile:
        data = myfile.read()

    # parse file
    obj = json.loads(data)
    elements = obj['Cluster']
    total_len = len(elements)

    print "Numero di elementi:  " + str(total_len)

    for elem in elements:
        for i in range(1, int(user_input[1])+1):
            if int(elem['Cluster']) == i:
                clusters[i-1].append(elem)

# print to test the number of elements in each cluster
# N.B.: clisters vector start from 0, cluster 1 elements are in clusters[0]

   # for e in clusters:
       # print len(e)

def cluster_averages():

    for cluster in clusters:
        nelem = len(cluster)
        ncluster = cluster[0]['Cluster']
        print ("Elementi cluster " + ncluster + ":  " + str(nelem))

        # per ogni elemento del cluster
        sum = [0] * npcomponents
        avg = []
        for elem in cluster:
            for i in range(1, npcomponents+1):
                sum[i-1] = sum[i-1] + float(elem['Principale'+str(i)])

        for s in sum:
            avg.append(s/int(nelem))
        averages.append(avg)


def intra_cluster_deviance():
    intra_cluster = 0
    for cluster in clusters:
        ncluster = int(cluster[0]['Cluster'])
        sum = 0
        for elem in cluster:
            for i in range(1, npcomponents+1):
                sum = sum + pow(float(elem['Principale'+str(i)])-averages[ncluster-1][i-1], 2)
        intra_cluster = intra_cluster + sum

    print "Devianza intra-cluster: " + str(intra_cluster)

def inter_cluster_deviance():
    inter_cluster = 0
    i = 0
    for avg in averages:
        nelem = len(clusters[i])
        sum = 0
        for x in avg:
            sum = sum + pow(x, 2)
        inter_cluster = inter_cluster + nelem * sum
        i += 1

    print "Devianza inter-cluster: " + str(inter_cluster)


read_file()
cluster_averages()
intra_cluster_deviance()
inter_cluster_deviance()
