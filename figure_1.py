import os

import pandas as pd
import glob
import numpy as np
from sklearn.linear_model import LinearRegression

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
# df_precipitation.sort(key=lambda f: int(filter(str.isdigit, f)))
# for file in df_precipitation:
#     with open(file, 'r') as f:
#         precip_df = pd.read_csv(f)
#         filename_string = file.split('_')[-1].split('.')[0]
#         try:
#             temp_df = flow_df[[filename_string, 'date']]
#             temp_df = temp_df.rename(columns={'date': 'Date'})
#             merged_df = pd.merge(temp_df, precip_df, on = 'Date', sort=True, how='left')
#
#             print(merged_df)
#         except Exception as e: print(e)




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










with open(https://byu.box.com/s/rkvltad09y6jk6k40si0ve8sm6ub5156) as file:
    precip_df = pd.read_csv(file)

    # print(precip_df)
    # filename_string = file.split('_')[-1].split('.')[0]
    try:
        # for loop going through flow data
        temp_df = flow_df[['1234150', 'date']]
        temp_df = temp_df.rename(columns={'date': 'Date'})
        merged_df = pd.merge(temp_df, precip_df, on = 'Date', sort=True, how='left')
        merged_df = merged_df.dropna()
        # leftfor index, row in merged_df.iterrows():
        #     if (row['precipitation'] != 'NaN') and (row['1234150'] != 'NaN') and (row['precipitation'] != 'nan') and (row['1234150'] != 'nan'):
        #         print(row['precipitation'])
        #         print(row['1234150'])
        # print(merged_df)
        Q = merged_df['1234150']
        P = merged_df['precipitation']
        # send result to new dataframe
        plot1 = ((Q/P))
        merged_df['RC'] = plot1

        # print(merged_df['QP'])
        # print(merged_df.to_string())
        # this is capping the QP values
        merged_df = merged_df[merged_df.RC < 1.7e+06]
        print(merged_df.to_string())


        df1 = merged_df.plot(x='Date',y='RC',c='Black')
        # df1.title('Hello')
        plt.title("Daily Runoff Ratio")
        plt.ylabel("Runoff (m^3/sec)")
        plt.show()

    except Exception as e: print(e)

# flow_df_1134030 = flow_df[["date", "1134030"]]
# flow_df_1134030['1134030'].dropna().unique()
# # print(flow_df_1134030)
#
# # tick_spacing = 365
#
# y = list(flow_df_1134030["1134030"])
# x = np.array(list(flow_df_1134030.index))
# plt.plot(x, y)
# plt.xlabel("Time (days)")
# plt.ylabel("Daily flow")
# plt.title("Yearly Water Cycles")
# plt.xticks(np.arange(min(x), 3600, 365.0))
# plt.show()

# BIG CALCULATION
# Isolate and iterate through the two columns
# --- two years? ---
# Calculate slope for each river
# Create new dataframe?





# create figure and go do something else

# print(flow_df_1134030)
