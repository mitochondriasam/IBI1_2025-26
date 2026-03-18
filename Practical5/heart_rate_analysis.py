import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

print(f"Patient number: {len(heart_rates)}", f"Mean heart rate: {sum(heart_rates) / len(heart_rates):.2f}", sep="\n")

low = []
normal = []
high = []
for i in range(len(heart_rates)):
    if  heart_rates[i] < 60:
        low.append(heart_rates[i])
    elif heart_rates[i] <= 120:
        normal.append(heart_rates[i])
    else:        
        high.append(heart_rates[i])
print("Number:", f"Low heart rates: {len(low)}", f"Normal heart rates: {len(normal)}", f"High heart rates: {len(high)}", sep="\n")

# Create a pie chart
labels = 'Low', 'Normal', 'High'
sizes = [len(low), len(normal), len(high)]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Heart Rate Distribution')
plt.show()