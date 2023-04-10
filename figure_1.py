import os



import pandas as pd

import glob

import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib

import matplotlib.pyplot as plt



full_path = "/Users/natalieandrus/PycharmProjects/capstone/"     #Change to your direct path



# open files

pd.options.display.max_rows = 10

df_catchment = pd.read_csv(full_path + 'catchmentMetadata.csv',encoding="ISO-8859-1")

df_evapotranspiration = sorted(glob.glob('Basin_ET_TS_for_model/*.csv'))     #insert your direct path and the file name

df_precipitation = sorted(glob.glob('Basin_Precip_TS_for_model/*.csv'))

df_temperate = sorted(glob.glob('Basin_Temp_TS_for_model/*.csv'))

flow_df = pd.read_csv(full_path + 'allDailyFlowData.csv')

globbyList = []



map(os.path.basename, glob.glob('Basin_ET_TS_for_model/*.csv'))



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







runoff_coeffs = [2, 3.4, 1, 6, 7, 4, 8, 5, 9, 11]

slope = calculate_slope(runoff_coeffs)

# print(slope)





















with open(full_path + 'Basin_Precip_TS_for_model/basin_1234150.csv') as file:

    font = {'family': 'sans-serif',

            'weight': 'normal',

            'size': 16}

    matplotlib.rc('font', **font)



    precip_df = pd.read_csv(file)



    try:

        # for loop going through flow data

        temp_df = flow_df[['1234150', 'date']]

        temp_df = temp_df.rename(columns={'date': 'Date'})

        merged_df = pd.merge(temp_df, precip_df, on = 'Date', sort=True, how='left')

        merged_df = merged_df.dropna()

        Q = merged_df['1234150']

        P = merged_df['precipitation']



        # send result to new dataframe

        plot1 = ((Q/P))

        merged_df['RC'] = plot1



        # this is capping the QP values

        merged_df = merged_df[merged_df.RC < 1.7e+06]

        for index, row in merged_df.iterrows():

            date = row[1]

            year = date[:4]

            month = date[5:7]

            day = date[8:]

            new_date = month + "/" + day + "/" + year

            merged_df.at[index, 'Date'] = new_date



        a_plot = merged_df[merged_df['Date'].str.contains("1999")]

        b_plot = merged_df[merged_df['Date'].str.contains("2000")]

        print(b_plot)



        df1 = a_plot.plot(x='Date',y='RC',c='Black')

        plt.title("Year 1 Runoff Ratio")

        plt.ylabel("Runoff (m^3/sec)")



        plt.show()



        df2 = b_plot.plot(x='Date', y='RC', c='Black')

        plt.title("Year 2 Runoff Ratio")

        plt.ylabel("Runoff (m^3/sec)")



        # click out of year one graph to view year 2

        plt.show()



    except Exception as e: print(e)
