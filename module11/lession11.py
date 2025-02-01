import datetime

currnet_datetime = datetime.datetime.now()

print("year:", currnet_datetime.year)
print("month:", currnet_datetime.month)
print("day:", currnet_datetime.day)
print("hour:", currnet_datetime.hour)
print("minute:", currnet_datetime.minute)
print("second:", currnet_datetime.second)


currnet_date = datetime.datetime.now().date()

print(currnet_date)

settime_date = datetime.datetime.now().time()

specific_time = datetime.date(2000, 2 ,3)

print(specific_time.year)
print(specific_time.month)
print(specific_time.day)

plusday = current_date + datetime.datatime(days=100)
print(plusday)

text = "this is the text i\n "



file_path = "example.txt"
file = open(file_path"r")
content = file.read(()
         print(content)

with open("example.txt","r") as file:
    lines = file.redlins()
    print(lines)




