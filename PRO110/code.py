import random
from cv2 import mean
import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

populationMean = statistics.mean(data)

def randMean(counter):
    dataset = []
    for i in range(0, counter):
        index = random.randint(0, len(data) - 1)
        value = data[index]
        dataset.append(value)
    randMean = statistics.mean(dataset)
    return randMean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0, 100):
        setMean = randMean(30)
        mean_list.append(setMean)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

population_mean = statistics.mean(data)
print("reading time mean:- ", population_mean)
mean_of_means = statistics.mean(mean)
print("sampling mean:- ", mean_of_means)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= randMean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()