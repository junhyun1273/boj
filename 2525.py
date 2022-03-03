# BOJ 2525

hour, minute = map(int, input().split())
cookTime = int(input())

ctHour = cookTime // 60
ctMinute = cookTime % 60

hour += ctHour
minute += ctMinute

if minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24:
    hour -= 24
    
print(hour, minute)