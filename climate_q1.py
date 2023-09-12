import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect('climate.db')

cursor = connection.cursor()

years = []
co2 = []
temp = []

cursor.execute("select Year from climatedata")
current = cursor.fetchall()
for year in current:
    years.append(year)

cursor.execute("select CO2 from climatedata")
current = cursor.fetchall()
for item in current:
    co2.append(item)

cursor.execute("select Temperature from climatedata")
current = cursor.fetchall()
for item in current:
    temp.append(item)


connection.commit()
connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

