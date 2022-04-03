from collections import defaultdict
import json
import sched

# Read Customer and Teller json data
fileHandler = open("CustomerData.json")
fileHandler2 = open("TellerData.json")

customer_data = json.load(fileHandler)
teller_data = json.load(fileHandler2)

# Close file handler process
fileHandler.close()
fileHandler2.close()

# Check flags, sentinel vals etc for scheduling logic; total_duration and schedule
total_duration = 0
schedule = defaultdict(lambda: -1)
schedule = {
    "sched": [
        {"teller_id": 0, "type2": -1, "customer_ids": [], "sched_time": 0, "multi": 0.0}
    ]
}
for entry in customer_data["Customer"]:
    total_duration += int(entry["duration"])

## print(len(customer_data["Customer"]))
## consider sched_time running from 480 down or 0 up
# Start scheduling each teller
for entry in teller_data["Teller"]:
    schedule["sched"].append(
        {
            "teller_id": entry["ID"],
            "type2": 0,
            "customer_ids": [],
            "sched_time": 0,
            "multi": 0.0,
        }
    )
    klast = schedule["sched"][-1]
    for entries in customer_data["Customer"]:
        if (
            int(entry["SpecialtyType"]) == int(entries["type"])
            and klast["sched_time"] <= 479
        ):
            klast["customer_ids"].append(entries["Id"])
            efficient_dur = float(entry["Multiplier"]) * int(entries["duration"])
            klast["sched_time"] += efficient_dur
            klast["type2"] = int(entry["SpecialtyType"])
            klast["multi"] = float(entry["Multiplier"])
            total_duration -= int(entries["duration"])

            # get index of entries
            ind = customer_data["Customer"].index(entries)
            # pop it from list of dict in-place
            customer_data["Customer"].pop(ind)

        else:
            continue

for rest_entry in customer_data["Customer"]:
    for tellers in schedule["sched"]:
        if (
            480 - int(rest_entry["duration"]) >= tellers["sched_time"]
            and tellers["type2"] != -1
        ):
            if int(rest_entry["type"]) == tellers["type2"]:
                efficient_dur = tellers["multi"] * int(rest_entry["duration"])
                tellers["customer_ids"].append(rest_entry["Id"])
                tellers["sched_time"] += efficient_dur
                total_duration -= int(rest_entry["duration"])

            else:
                tellers["customer_ids"].append(rest_entry["Id"])
                tellers["sched_time"] += int(rest_entry["duration"])
                total_duration -= int(rest_entry["duration"])

        else:
            continue
    ind = customer_data["Customer"].index(rest_entry)
    customer_data["Customer"].pop(ind)
print(total_duration)

# check what's been scheduled
for k in schedule["sched"]:
    print(k)
print(len(customer_data["Customer"]))


# print((data["Customer"].pop(5)))

# for i in data["Customer"]:
#     ind = data["Customer"].index(i)
#     print(ind)
