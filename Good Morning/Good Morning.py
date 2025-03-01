import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if(timestamp >= 6 and timestamp <= 12):
    print("Good Mornibg")
elif(timestamp >= 12 and timestamp <= 16):
    print("Good Afternoon")
elif(timestamp >= 16 and timestamp <= 20):
    print("Good Evening")
else: #(timestamp >= 20 and timestamp <= 24)
    print("Good Night")
