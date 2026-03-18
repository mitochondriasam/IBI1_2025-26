import pandas as pd
import matplotlib.pyplot as plt

def calculate_percentage_change(initial, final):
    if initial == 0:
        return float('inf')  # Infinite percentage change if initial value is zero
    return ((final - initial) / initial) * 100

tsv_path = "Practical5/pop.tsv"
df = pd.read_csv(tsv_path, sep="\t")
print(df)

df['Growth_Rate'] = df.apply(lambda row: calculate_percentage_change(row['Population 2020 (millions)'], row['Population 2024 (millions)']), axis=1)

df.sort_values(by='Growth_Rate', ascending=False, inplace=True)
print(df[['Country', 'Growth_Rate']])
print(f"Largest increase: {df.iloc[0]['Country']}", f"Largest decrease: {df.iloc[-1]['Country']}", sep="\n")

colors = ['lightcoral' if rate < 0 else 'lightgreen' for rate in df['Growth_Rate']]
figpath = "Practical5/population_growth_rate.png"
plt.bar(df['Country'], df['Growth_Rate'], color=colors)
plt.xlabel('Country')
plt.ylabel('Growth Rate (%)')
plt.title('Population Growth Rate by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(figpath)
plt.show()