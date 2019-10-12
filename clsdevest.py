import json
import matplotlib.pyplot as plt

# read file
with open('clustering_history.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
history = obj['prova']

# show values
#print(str(history[len(history)-1]))
max_distance = float(history[len(history)-1]['Distanza'])
x = []
y = []
for hist_elem in history:
    estimation = 100 * float(hist_elem['Distanza'])/max_distance
    x.append(hist_elem['Numero di cluster'])
    y.append(estimation)
    print (hist_elem['Numero di cluster'] + "   " + hist_elem['Distanza'] + " ==> " + str(estimation))

plt.plot(x,y)
plt.xlabel('number of cluster')
plt.ylabel('lost variance (% not exact)')
plt.show()
