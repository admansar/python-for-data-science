from load_csv import load
from matplotlib import pyplot as plt


def main():
    df1 = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    df2 = load('life_expectancy_years.csv')
    needed_year = '1900'
    income = df1[needed_year].tolist()
    ley = df2[needed_year].tolist()
    plt.title(needed_year)
    plt.xlabel('Gross domestic product')
    plt.ylabel('life expectancy')
    plt.xlim(300, 1e4)
    plt.minorticks_on()
    plt.semilogx(income, ley, marker='o', linestyle='None')
    plt.xticks([300, 1e3, 1e4], ['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error : {e}")
