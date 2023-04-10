import csv
import os

import matplotlib
import pandas as pd
import glob
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import statistics

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# open files
pd.options.display.max_rows = 10
df_catchment = pd.read_csv('catchmentMetadata.csv',encoding="ISO-8859-1")
df_evapotranspiration = sorted(glob.glob('Basin_ET_TS_for_model/*.csv'))
df_precipitation = sorted(glob.glob('Basin_Precip_TS_for_model/*.csv'))
df_temperate = sorted(glob.glob('Basin_Temp_TS_for_model/*.csv'))
flow_df = pd.read_csv('allDailyFlowData.csv')
globbyList = []
#
# print(df_evapotranspiration)
map(os.path.basename, glob.glob('Basin_ET_TS_for_model/*.csv'))
# df_precipitation.sort(key=lambda f: int(filter(stçr.isdigit, f)))







def calculate_RC(precip, flow): # calculate runoff coefficient for one day
    rc = flow/precip
    return rc

def calculate_slope(runoff_array):   #takes array of one basin's runoff coefficients and calculates the slope using linear regression
    # get x values (dates)
    counter = 1
    xes = []
    for i in range(len(runoff_array)):
        xes.append(counter)
        counter = counter + 1

    # create numpy arrays
    x = np.array(xes).reshape((-1, 1))
    y = np.array(runoff_array)

    # create instance of linear regression model and fit it to data, get slope
    model = LinearRegression().fit(x, y)
    slope = model.coef_
    return slope

# making figure 2
def make_figure2(slopes, ids, ids_array, chars_array):
    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 30}
    matplotlib.rc('font', **font)
    x_values = []
    y_values = []
    for i in range(len(slopes)):
        id = ids[i]
        slope = slopes[i]
        try:
            index = ids_array.index(float(id + ".0"))
            # print(index)
            char = chars_array[index]
            if char != "nan":
                x_values.append(char)
                y_values.append(slope)
        except Exception as e: continue

    plt.scatter(x_values, np.array(y_values), c = 'Black')
    plt.title("Changes in Runoff Ratios by Latitude")
    plt.ylabel("Change in Runoff Ratio (slope)")
    plt.xlabel("Latitude")
    plt.show()

    return

# magnitude graph
def magnitude_eval(slopes, ids, ids_array, chars_array):
    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 10}
    matplotlib.rc('font', **font)
    x_values = []
    y_values = []
    for i in range(len(slopes)):
        id = ids[i]
        slope = slopes[i]
        try:
            index = ids_array.index(float(id + ".0"))
            # print(index)
            char = chars_array[index]
            if char != "nan":
                x_values.append(char)
                y_values.append(slope)
        except Exception as e: continue

    plt.scatter(x_values, np.array(y_values), c = 'Black')
    plt.title("Changes in Runoff Ratios by")
    plt.ylabel("Change in Runoff Ratio (slope)")
    plt.xlabel("Continents")
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.show()

    return

# area graph
def area_eval(slopes, ids, ids_array, chars_array):
    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 10}
    matplotlib.rc('font', **font)
    x_values = []
    y_values = []
    for i in range(len(slopes)):
        id = ids[i]
        slope = slopes[i]
        try:
            index = ids_array.index(float(id + ".0"))
            # print(index)
            char = chars_array[index]
            if char != "nan":
                x_values.append(char)
                y_values.append(slope)
        except Exception as e: continue

    plt.scatter(x_values, np.array(y_values), c = 'Black')
    plt.title("Changes in Runoff Ratios by")
    plt.ylabel("Change in Runoff Ratio (slope)")
    plt.xlabel("Continents")
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.show()

    return

# continent graph
def continents_eval(slopes, ids, ids_array, chars_array):
    font = {'family': 'sans-serif',
            'weight': 'normal',
            'size': 10}
    matplotlib.rc('font', **font)
    x_values = []
    y_values = []
    for i in range(len(slopes)):
        id = ids[i]
        slope = slopes[i]
        try:
            index = ids_array.index(float(id + ".0"))
            # print(index)
            char = chars_array[index]
            if char != "nan":
                x_values.append(char)
                y_values.append(slope)
        except Exception as e: continue

    plt.scatter(x_values, np.array(y_values), c = 'Black')
    plt.title("Changes in Runoff Ratios by")
    plt.ylabel("Change in Runoff Ratio (slope)")
    plt.xlabel("Continents")
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=45)
    plt.show()

    return

id_array = []
slope_array = []


for file in df_precipitation:
    with open(file, 'r') as f:
        precip_df = pd.read_csv(f)
        filename_string = file.split('_')[-1].split('.')[0]
        try:
            temp_df = flow_df[[filename_string, 'date']]
            temp_df = temp_df.rename(columns={'date': 'Date'})
            merged_df = pd.merge(temp_df, precip_df, on = 'Date', sort=True, how='left')
            merged_df = merged_df.dropna()

            Q = merged_df[filename_string]
            P = merged_df['precipitation']
            # send result to new dataframe
            plot1 = ((Q / P))
            merged_df['RC'] = plot1

            # calculate slope
            merged_df = merged_df[merged_df.RC < 1.7e+06]
            array = merged_df['RC'].tolist()
            if len(array) > 3:
                slope = calculate_slope(array)[0]
                meannn = statistics.mean(array)
                if meannn != 0.0:
                    # print(str(slope) + ", " + str(meannn))
                    normalized_slope = slope / meannn
                    if abs(normalized_slope) > 0.01:
                        slope_array.append(normalized_slope)
                        id_array.append(filename_string)
        except Exception as e: continue

# make figure 2
chars_df = df_catchment
ids = chars_df['grdc_no'].tolist()
lat_chars = chars_df['new_lat.x']
#make_figure2(slope_array, id_array, ids, lat_chars)

# FIGURE 3 Continent barchart
value = pd.DataFrame(chars_df['Continent'].value_counts())
# these values were then input into excel to create a barchart
print(value)

# MAGNITUDE PLOT
magnitude_chars = chars_df['Magnitude']
# limit it at 40 to remove outliers
magnitude_chars = magnitude_chars[magnitude_chars < 40]
#magnitude_eval(slope_array, id_array, ids, magnitude_chars)

# AREA PLOT
area_chars = chars_df['garea_sqkm']

# limit it at 20000 to remove outliers
area_chars = area_chars[area_chars < 20000]
#area_eval(slope_array, id_array, ids, area_chars)

# CONTINENTS PLOT
continents_chars = chars_df['Continent']
#continents_eval(slope_array, id_array, ids, continents_chars)

