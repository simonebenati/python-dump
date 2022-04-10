import pprint
import time

start_time = time.time()

message = "Pass the variable a .txt file" #to be done
count = {}

for l in message.upper():
    count.setdefault(l , 0)
    count[l] = count[l]+1

pprint.pprint(count)

end_time = time.time()

print("Calculated in: " + str(round(end_time - start_time, 4)) + " seconds.")