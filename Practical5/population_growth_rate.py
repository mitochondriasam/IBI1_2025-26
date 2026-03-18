import pandas as pd
import matplotlib.pyplot as plt

def calculate_percentage_change(initial, final):
    try:
        return ((final - initial) / initial) * 100
    except ZeroDivisionError:   # Handle division by zero if initial population is zero, though unlikely in this context
        return float('inf') if final > 0 else float('-inf')

tsv_path = "Practical5/pop.tsv"
df = pd.read_csv(tsv_path, sep="\t")
print(df)

# Calculate growth rates and add as a new column
df['Growth_Rate'] = calculate_percentage_change(df['Population 2020 (millions)'], df['Population 2024 (millions)'])

df.sort_values(by='Growth_Rate', ascending=False, inplace=True)     # Sort the DataFrame by growth rate in descending order
print(df[['Country', 'Growth_Rate']])
print(f"Largest increase: {df.iloc[0]['Country']}", f"Largest decrease: {df.iloc[-1]['Country']}", sep="\n")

colors = ['lightcoral' if rate < 0 else 'lightgreen' for rate in df['Growth_Rate']]     # For increase and decrease, use different colors
figpath = "Practical5/population_growth_rate.png"
plt.bar(df['Country'], df['Growth_Rate'], color=colors)
plt.xlabel('Country')
plt.ylabel('Growth Rate (%)')
plt.title('Population Growth Rate by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(figpath)
plt.show()