import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data")

    tax = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = pd.Series(range(1880, 2051))
    y1 = tax.slope * x1 + tax.intercept
    plt.plot(x1,y1, "r", label="Fit: 1880-2050")

    df_tax = df[df["Year"] >= 2000]
    re = linregress(df_tax['Year'], df_tax['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = re.slope * x2 + re.intercept
    plt.plot(x2, y2, "g", label="Fit: 2000-2050")

    plt.xlabel("Year")
    plt.ylabel("Sea Level")
    plt.title("Rise in Sea Level")
    plt.legend()

    plt.savefig("sea_level_plot.png")
    return plt.gca()