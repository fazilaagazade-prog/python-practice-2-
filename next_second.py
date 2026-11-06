hour, minute, second = input("Saat deqiqe saniye yazin (mes: 23 59 59): ").split()

hour = int(hour)
minute = int(minute)
second = int(second)

second += 1

if second == 60:
    second = 0
    minute += 1

if minute == 60:
    minute = 0
    hour += 1

if hour == 24:
    hour = 0

print(hour, minute, second)