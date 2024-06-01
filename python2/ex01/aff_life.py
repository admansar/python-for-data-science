import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    df = load('life_expectancy_years.csv')
    if df is None:
        return None
    years = np.array(df.columns[:]).tolist()[1:]
    countries = np.array(df).tolist()
    ley = []
    country_name = 'Morocco'
    for item in countries:
        if item[0] == country_name:
            ley = item[1:]
    if len(ley) == 0:
        return None
    plt.plot(years, ley)
    plt.title(country_name + ' life expectancy projection')
    xtick = []
    for item in years:
        if int(item) % 40 == 0:
            xtick.append(item)
    plt.xticks(xtick)
    plt.show()


if __name__ == "__main__":
    main()
