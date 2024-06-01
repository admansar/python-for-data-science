import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        df = load('life_expectancy_years.csv')
        if df is None:
            return None
        years = df.columns[:].tolist()[1:]
        countries = df.values.tolist()
        country_name = 'Morocco'
        ley = []
        for item in countries:
            if item[0] == country_name:
                ley = item[1:]
        if len(ley) == 0:
            return None
        plt.plot(years, ley)
        plt.title(country_name + ' life expectancy projection')
        xtick = [item for item in years if int(item) % 40 == 0]
        plt.xticks(xtick)
        plt.show()
    except Exception as e:
        print(f"Error : {e}")


if __name__ == "__main__":
    main()
