# 1. Convert the time entered in hh,min and sec into seconds.

hr = int(input('Enter the hours:'))
min = int(input('Enter the minutes: '))
sec =int(input('Enter the seconds: '))

total_sec= (hr*3600)+(min*60)+sec

print("Total Seconds = ",total_sec)


# Enter the hours:4
# Enter the minutes: 35
# Enter the seconds: 88 
# Total Seconds =  16588