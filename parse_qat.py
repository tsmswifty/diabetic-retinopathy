import re
import matplotlib.pyplot as plt

accuracy_list = []

accuracy_pattern = re.compile(r"\]  \* Acc@1\s+([\d\.]+)")
for file_number in range(1, 7):
    filename = f"qatlog.txt.{file_number}"
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            accuracy_match = accuracy_pattern.search(line)
            if accuracy_match:
                accuracy = float(accuracy_match.group(1))
                accuracy_list.append(accuracy)
print("end")
print(accuracy_list)
print(len(accuracy_list))

num_epochs = len(accuracy_list)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

fig.suptitle("Accuracy vs. Epoch Number")

ax1.plot(range(num_epochs), accuracy_list)
ax1.set_ylabel("Accuracy")

ax2.plot(range(num_epochs), accuracy_list)
ax2.set_xlabel("Epoch Number")
ax2.set_ylabel("Accuracy")

plt.show()
