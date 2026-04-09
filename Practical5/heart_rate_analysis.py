import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

print(f"Patient number: {len(heart_rates)}", f"Mean heart rate: {sum(heart_rates) / len(heart_rates):.2f}", sep="\n")   # Calculate and print the number of patients and the mean heart rate, rounded to 2 decimal places

low = []
normal = []
high = []
for i in range(len(heart_rates)):   # Classify heart rates into low, normal, and high categories
    if  heart_rates[i] < 60:
        low.append(heart_rates[i])
    elif heart_rates[i] <= 120:
        normal.append(heart_rates[i])
    else:        
        high.append(heart_rates[i])
print("\nNumber:", f"Low heart rates: {len(low)}", f"Normal heart rates: {len(normal)}", f"High heart rates: {len(high)}", sep="\n")
print(f"\nThe most frequent heart rate category is: {'Low' if len(low) > len(normal) and len(low) > len(high) else 'Normal' if len(normal) > len(low) and len(normal) > len(high) else 'High'}")   # Determine and print the most frequent heart rate category

# Create a pie chart
labels = 'Low', 'Normal', 'High'
colors = ['lightskyblue', 'lightgreen', 'lightcoral']
sizes = [len(low), len(normal), len(high)]
figpath = "Practical5/heart_rate_distribution.png"
plt.pie(sizes, labels=labels, colors=colors, autopct='%0.1f%%')
plt.title('Heart Rate Distribution')
plt.savefig(figpath)
plt.show()