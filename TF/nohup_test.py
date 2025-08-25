import csv
import time

with open('count_to_100.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Number'])
    for i in range(1, 3):
        print(i)
        time.sleep(5)
        writer.writerow([i])