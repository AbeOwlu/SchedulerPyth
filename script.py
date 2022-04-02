from collections import defaultdict
import json
import sched

# Read Customer and Teller json data
fileHandler = open("CustomerData.json")
fileHandler2 = open("TellerData.json")

customer_data = json.load(fileHandler)
teller_data = json.load(fileHandler2)

# Check flag variables for scheduling; total_duration and schedule
total_duration = 0
schedule = defaultdict(lambda: 0)
schedule = {"sched": [{"teller_id": 0, "customer_ids": [], "sched_time": 0}]}
for entry in customer_data["Customer"]:
    total_duration += int(entry["duration"])

## print(len(customer_data["Customer"]))
## consider sched_time running from 480 down or 0 up
# Start scheduling each teller
for entry in teller_data["Teller"]:
    schedule["sched"].append(
        {"teller_id": entry["ID"], "customer_ids": [], "sched_time": 0}
    )
    klast = schedule["sched"][-1]
    for entries in customer_data["Customer"]:
        if (
            int(entry["SpecialtyType"]) == int(entries["type"])
            and klast["sched_time"] < 450
        ):
            klast["customer_ids"].append(entries["Id"])
            efficient_dur = float(entry["Multiplier"]) * int(entries["duration"])
            klast["sched_time"] += efficient_dur
            total_duration -= int(entries["duration"])

            # get index of entries
            ind = customer_data["Customer"].index(entries)
            # pop it from list of dict in-place
            customer_data["Customer"].pop(ind)

        else:
            continue

## check what's been scheduled
# for k in schedule["sched"]:
#     print(k)
# print(len(customer_data["Customer"]))
# print(total_duration)

for rest_entry in customer_data["Customer"]:
    pass

# print((data["Customer"].pop(5)))

# for i in data["Customer"]:
#     ind = data["Customer"].index(i)
#     print(ind)

fileHandler.close()
fileHandler2.close()
