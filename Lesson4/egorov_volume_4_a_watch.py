import time

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            time.sleep(0.11)
            print(hours, ':', minutes ,':', seconds)