from collections import Counter
import csv

with open("drugs.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    type_counter = Counter()
    for type in csv_reader:
       type_counter.update([type["type"]])

general_type = []
general_type_count = []

for data in type_counter.most_common(5):
    general_type.append(data[0])
    general_type_count.append(data[1])

print(general_type)
print(general_type_count)