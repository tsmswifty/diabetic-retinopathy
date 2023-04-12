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

fig, ax = plt.subplots()

fig.suptitle('Validation Accuracy')

ax.plot(range(num_epochs), accuracy_list, label='INT8 Quantized Model')
# ax.plot(range(num_epochs), accuracy_list, alpha=0.5, linestyle='--')

ax.set_xlabel('Epoch Number')
ax.set_ylabel('Accuracy')
ax.legend()

plt.show()
