import pandas as pd
import matplotlib.pyplot as plt


def plot_yearly_gdp(df_gdp):
    plt.figure(dpi=144)

    countries = df_gdp.columns
    for country in countries:
        plt.plot(df_gdp.index, df_gdp[country], label=country)

    plt.legend()
    plt.yscale('log')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.title('GDP Change')
    plt.show()
    return


def plot_yearly_gdp_relative(df_gdp):

    plt.figure(dpi=144)

    countries = df_gdp.columns
    for country in countries:
        if '_rel' not in country or 'United States' in country:
            continue

        plt.plot(df_gdp.index, df_gdp[country], label=country.strip('_rel'))

    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Relative GDP (% US $)')
    plt.show()
    return


df_gdp = pd.read_csv('./Unit02/GDP_2015dollars.csv', index_col='Year')
# df_gdp.head()
# plot_yearly_gdp(df_gdp)

for country in df_gdp.columns:
    df_gdp[country + '_rel'] = (df_gdp[country] /
                                df_gdp['United States']) * 100

df_gdp.head()
#  print(df_gdp)
plot_yearly_gdp_relative(df_gdp)
