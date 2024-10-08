import matplotlib.pyplot as plt
import pandas as pd

# Beispiel-Daten: Zahlen von 0 bis 9 und ihre Quadrate
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [i**2 for i in x]  # Quadratzahlen
z = [i**3 for i in x]   # Kubikzahlen

# Liniendiagramm erstellen
plt.plot(x, y, label='Quadratzahlen')
plt.plot(x, z, label='Kubikzahlen')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Quadratzahlen und Kubikzahlen von 0 bis 9')
plt.xlabel('Zahl')
plt.ylabel('Quadrat')

# Legende anzeigen
plt.legend()

# Diagramm als PNG speichern
plt.savefig('data_visualization.png', bbox_inches='tight')

# Diagramm anzeigen
# plt.show()

# Pandas Datenanalyse
dataX = pd.DataFrame({'X': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                             'Y': [i**2 for i in x],
                             'Z': [i**3 for i in x]})
print(dataX)

dataX.to_csv('zahlen.csv')