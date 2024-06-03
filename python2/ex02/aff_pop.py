import matplotlib.pyplot as plt
from load_csv import load


def country_data(countries: list, country_name: str) -> list:
    """
    country_data(countries : list, country_name: str) -> list
    read the data from the list and creat a list with the name of
    the country_name given as a list
    """
    for it in countries:
        if it[0] == country_name:
            return (it[1:])
    return None


def clean_data(pt: list) -> list:
    """
    clean the data from the string M(millions) and K (thousand)
    to a float number
    """
    popu = []
    for it in pt:
        if 'M' or 'm' in it:
            tmp = float(it[:-1]) * 1e6
        elif 'K' or 'k' in it:
            tmp = float(it[:-1]) * 1e3
        else:
            tmp = float(it)
        popu.append(tmp)
    return popu


def main():
    df = load('population_total.csv')
    if df is None:
        raise Exception("population_total.csv is not there")
    years = [int(item) for item in df.columns[:].tolist()[1:]]
    countries = df.values.tolist()
    coutries_to_be_in_graph = ['France', 'Morocco', 'Madagascar']
    pt = [country_data(countries, name) for name in coutries_to_be_in_graph]
    popu = [clean_data(item) for item in pt]
    plt.xlim(1790, 2050)
    for i in range(len(popu)):
        plt.plot(years, popu[i], label=coutries_to_be_in_graph[i])
    plt.title('population projection')
    xtick = [it for it in years if it % 40 == 0 and it < 2080]
    ytick = [0, 2e7, 4e7, 6e7]
    plt.xticks(xtick)
    plt.yticks(ytick, ['0', '2M', '4M', '6M'])
    plt.legend()
    plt.show()
    # label in plot and plt.legend for the mini table


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error : {e}")
