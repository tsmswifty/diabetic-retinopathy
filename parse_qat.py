import re
import matplotlib.pyplot as plt

accuracy_list = []

accuracy_pattern = re.compile(r"\]  \* Acc@1\s+([\d\.]+)")
for file_number in range(1, 8):
    filename = f"qatlog.txt.{file_number}"
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            accuracy_match = accuracy_pattern.search(line)
            if accuracy_match:
                accuracy = float(accuracy_match.group(1))
                accuracy_list.append(accuracy)

reg_vit = []

with open('loss_acc.txt.vit.new', 'r') as file:
    for line in file:
        # Split the line into a list of values using the comma as the delimiter
        line_values = line.strip().split(',')

        # Get the fourth-to-last value
        value = float(line_values[-4])

        # Add the value to the array
        reg_vit.append(value*100)

print("end")
print("max non-quantized accuracy: ", max(reg_vit))
print("max quantized accuracy: ", max(accuracy_list))

num_epochs = min(len(accuracy_list), len(reg_vit))

fig, ax = plt.subplots()

fig.suptitle('Validation Accuracy')

ax.plot(range(num_epochs), accuracy_list[:num_epochs], label='INT8 Quantized Model')
ax.plot(range(num_epochs), reg_vit[:num_epochs], color="orange", label='Unquantized Model')

ax.set_xlabel('Epoch Number')
ax.set_ylabel('Accuracy')
ax.legend()

plt.show()
plt.savefig("valacc.png")
