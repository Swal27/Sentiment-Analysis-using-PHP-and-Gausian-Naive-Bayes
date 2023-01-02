import getopt, sys
import matplotlib.pyplot as plt


jumlah_positif = int(sys.argv[1])
jumlah_negatif = int(sys.argv[2])
jumlah_netral = int(sys.argv[3])

# Diagram donut
labels = ['Jumlah Positif', 'Jumlah Negatif', 'Jumlah Netral']
sizes = [jumlah_positif, jumlah_negatif, jumlah_netral]
colors = ['purple', 'gold', 'lightskyblue']
explode = (0, 0, 0)  # explode a slice

fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('donut_testing.jpg', format='jpg')

# Diagram Bar
fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.bar(labels, sizes, color=colors)

plt.savefig('bar_testing.jpg', format='jpg')

# Diagram Circle
fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('pie_testing.jpg', format='jpg')