import time

print(time.ctime(0)) // time since computer thinks time began
time.time() // seconds passed since epoch
print(time.ctime(time.time()))
print(time.localtime()) // creates time object based on current time
