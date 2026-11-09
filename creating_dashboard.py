from matplotlib import pyplot as plt
from collections import Counter
import csv
plt.style.use("ggplot")

fig, axes = plt.subplots(2,3, figsize=(15,10))
fig.suptitle("Drug Data Dashboard", fontsize=16, fontweight='bold', y=1)

toxicity = [0.1, 0.2, 0.05, 0.1, 0.3, 0.4, 0.1, 0.25, 0.5, 0.35]
activity = ['0.75', '0.7', '0.85', '0.9', '0.95', '0.65', '0.8', '0.88', '0.72', '0.66']
solubility = [0.8, 0.6, 0.9, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.7]
molecular_weight = [180, 206, 129, 334, 493, 308, 312, 602, 454, 320]
drugs = ['Aspirin', 'Ibuprofen', 'Metformin', 'Penicillin', 'Imatinib', 'Warfarin', 'Oseltamivir', 'Remdesivir', 'Methotrexate', 'Chloroquine']

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

axes[0,0].plot(activity, marker='o', color='blue', label="Activity Trend")
axes[0, 0].legend()
axes[0, 0].set_title("Activity Trend")

axes[0, 1].bar(range(len(drugs)), activity, color='steelblue', label="Activity Bar Chart")
axes[0, 1].legend()
axes[0, 1].set_title("Activity Bar Chart")

axes[0, 2].barh(drugs, molecular_weight, color='orange', label='Molecular weight')
axes[0, 2].legend()
axes[0, 2].set_title("Molecular weight")

axes[1, 0].scatter(toxicity, activity, color='red', s=100, label="Toxicity vs Activity")
axes[1, 0].legend()
axes[1, 0].set_title("Toxicity vs Activity" ,loc='center', y=-0.25)

axes[1, 1].hist(molecular_weight, bins=5, color='green', edgecolor='black', label="molecular_weight Distribution")
axes[1, 1].legend()
axes[1, 1].set_title("Molecular Weight Distribution" ,loc='center', y=-0.25)

#labels = 
axes[1, 2].pie(general_type_count, labels=general_type, autopct='%1.1f%%', shadow=True, wedgeprops={'edgecolor' : 'black'}, startangle=90)
axes[1, 2].set_title("Pie chart: Types of Drugs" ,loc='center', y=-0.25)
plt.tight_layout()
plt.savefig("Dashboard.png", dpi=300, bbox_inches='tight')
plt.show()