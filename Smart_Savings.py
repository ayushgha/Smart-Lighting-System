import pyrebase
import matplotlib.pyplot as plt

config = {
  "apiKey": "AIzaSyCu7tEk3wCkMDYPKaipZnVixo_Gn6FghZM",
  "authDomain": "pythonfire-37436.firebaseapp.com",
  "databaseURL": "https://pythonfire-37436.firebaseio.com",
  "storageBucket": "pythonfire-37436.appspot.com"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()

show = db.child('Status').get()
cost = db.child('cost').get()

#print(show.val())

output = show.val()

time = []
stat = []
for i in output:
    for j in output[i]:
      time.append(j)
      stat.append(output[i][j])
#print(time)
#print(stat)
#print(len(stat))
#print(cost.val())
c = (cost.val())
total_cost = []
for i in c:
    total_cost.append(c[i])

electricity_used = max(total_cost)
#print(electricity_used)

without_smart_automation_electricity = 20

ele = [electricity_used,without_smart_automation_electricity]
label = ['''electricity_used
          _with_smart_automation''','''electricity_used_without_
          smart_automation_''']


plt.bar(label,ele)
plt.title('''Comparision of cost in the past 1 minute
      (Smart Lighting vs Normal lighting)''')
plt.show()

savings_considering_same_rate_smart_in_a_month =  (without_smart_automation_electricity*60*24*30) -(electricity_used*60*24*30)
print("SAVINGS",savings_considering_same_rate_smart_in_a_month)

