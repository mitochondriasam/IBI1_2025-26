import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the data
    data = pd.read_csv("Practical10/dalys-rate-from-all-causes.csv")
    
    # data overview
    print(f"First 10 rows:\n{data.head(10)}")
    print(f"\nColumns 3 and 4:\n{data.columns[2:4]}")
    
    # show year and dalys columns in the first 10 rows
    print(f"\nYear and DALYs columns (first 10 rows):\n{data.iloc[:10, [2, 3]]}")
    
    # data info
    print(f"\nData Info:\n{data.info()}")
    
    # descriptive statistics
    print(f"\nDescriptive Statistics:\n{data.describe()}")
    
    # specific values
    print(f"\nSpecific Values:\n{data.iloc[0:3, [0, 1, 3]]}")  # First row
    
    afg = data[data['Entity'] == 'Afghanistan']
    first_10_afg = afg.head(10)
    max_year_afg = first_10_afg.loc[first_10_afg['DALYs'].idxmax(), 'Year']
    print(f"\nThe year with the maximum DALYs in the first 10 years for Afghanistan is: {max_year_afg}")
    # The year with the maximum DALYs in the first 10 years for Afghanistan is 1998
    
    # use a Boolean to show all years for which DALYs were recorded in Zimbabwe
    zimbabwe_mask = data['Entity'] == 'Zimbabwe'
    years_zimbabwe = data[zimbabwe_mask]['Year'].tolist()
    print(f"\nYears with DALYs data for Zimbabwe: {years_zimbabwe}")
    # the first year: 1990; the last year: 2019
    
    # countries with the maximum and mimumum DALYs in 2019
    data_2019 = data[data['Year'] == 2019]
    max_country_2019 = data_2019.loc[data_2019['DALYs'].idxmax(), 'Entity']
    min_country_2019 = data_2019.loc[data_2019['DALYs'].idxmin(), 'Entity']
    print(f"\nCountry with maximum DALYs in 2019: {max_country_2019}")
    print(f"Country with minimum DALYs in 2019: {min_country_2019}")
    # max: Lesotho; min: Singapore
    
    # created a plot showing the DALYS over time
    country_data = data[data['Entity'] == max_country_2019]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['DALYs'], marker='o', linestyle='-', color='red')
    plt.xlabel('Year')
    plt.ylabel('DALYs')
    plt.xticks(country_data['Year'], rotation=45)
    plt.title(f'DALYs Over Time in {max_country_2019}')
    plt.grid(True)
    plt.savefig('Practical10/DALYs_over_time_max_country.png')
    plt.close()
    
    country_data = data[data['Entity'] == min_country_2019]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['DALYs'], marker='o', linestyle='-', color='blue')
    plt.xlabel('Year')
    plt.ylabel('DALYs')
    plt.xticks(country_data['Year'], rotation=45)
    plt.title(f'DALYs Over Time in {min_country_2019}')
    plt.grid(True)
    plt.savefig('Practical10/DALYs_over_time_min_country.png')
    plt.close()
    
    # Question: How has the relationship between DALYs in China and the UK changed over time?
    china_data = data[data['Entity'] == 'China']
    uk_data = data[data['Entity'] == 'United Kingdom']

    # Plot DALYs over time for both countries
    plt.figure(figsize=(10, 6))
    plt.plot(china_data['Year'], china_data['DALYs'], label='China', marker='o', color='red')
    plt.plot(uk_data['Year'], uk_data['DALYs'], label='UK', marker='s', color='blue')
    plt.xlabel('Year')
    plt.ylabel('DALYs')
    plt.title('DALYs Over Time: China vs. UK')
    plt.legend()
    plt.grid(True)
    plt.savefig('Practical10/China_UK_DALYs_comparison.png')
    plt.close()

    # Summary statistic: Absolute difference in DALYs each year (to measure similarity)
    merged = pd.merge(china_data[['Year', 'DALYs']], uk_data[['Year', 'DALYs']], on='Year', suffixes=('_China', '_UK'))
    merged['Difference'] = abs(merged['DALYs_China'] - merged['DALYs_UK'])
    print(f"\nDALYs Difference (China - UK) over time:\n{merged[['Year', 'Difference']]}")
    avg_diff = merged['Difference'].mean()
    print(f"Average absolute difference: {avg_diff:.2f}")