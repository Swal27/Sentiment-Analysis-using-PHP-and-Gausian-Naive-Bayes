import getopt, sys
import matplotlib.pyplot as plt

jumlah_positif = int(sys.argv[1])
jumlah_negatif = int(sys.argv[2])
jumlah_netral = int(sys.argv[3])

# Diagram donut
labels = ['Jumlah Positif', 'Jumlah Negatif']
sizes = [jumlah_positif, jumlah_negatif]
colors = ['purple', 'gold', 'lightskyblue']
explode = (0, 0)  # explode a slice

# Urutkan list sizes dari yang terendah ke tertinggi
sizes, labels = zip(*sorted(zip(sizes, labels)))

fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('donut.jpg', format='jpg')

# Diagram Bar
fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.bar(labels, sizes, color=colors)


plt.savefig('bar.jpg', format='jpg')

# Diagram Circle
fig, ax = plt.subplots(figsize=(500/96, 500/96), dpi=96)
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('pie.jpg', format='jpg')