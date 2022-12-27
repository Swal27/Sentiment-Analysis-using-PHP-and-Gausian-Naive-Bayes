import getopt, sys
import matplotlib.pyplot as plt

for arg in sys.argv:
    print(arg)
jumlah_positif = sys.argv[1]
jumlah_negatif = sys.argv[2]
jumlah_netral = sys.argv[3]

# Diagram donut
labels = ['Jumlah Positif', 'Jumlah Negatif', 'Jumlah Netral']
sizes = [jumlah_positif, jumlah_negatif, jumlah_netral]
colors = ['yellowgreen', 'gold', 'lightskyblue']
explode = (0, 0, 0)  # explode a slice

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('donut.jpg', format='jpg')

# Diagram Bar
fig, ax = plt.subplots()
ax.bar(labels, sizes, color=colors)

plt.savefig('bar.jpg', format='jpg')

# Diagram Circle
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('pie.jpg', format='jpg')