import os

import pandas as pd
import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

pd.options.display.max_rows = 10
df_catchment = pd.read_csv('catchmentMetadata.csv',encoding="ISO-8859-1")
df_evapotranspiration = sorted(glob.glob('Basin_ET_TS_for_model/*.csv'))
df_precipitation = sorted(glob.glob('Basin_Precip_TS_for_model/*.csv'))
df_temperate = sorted(glob.glob('Basin_Temp_TS_for_model/*.csv'))
flow_df = pd.read_csv('StreamTeam/allDailyFlowData.csv')
# print(flow_df)
globbyList = []
#
# print(df_evapotranspiration)
map(os.path.basename, glob.glob('Basin_ET_TS_for_model/*.csv'))
# df_precipitation.sort(key=lambda f: int(filter(str.isdigit, f)))
# for file in df_precipitation:
#
#     # print(df_evapotranspiration)
#
#     with open(file, 'r') as f:
#         precip_df = pd.read_csv(f)
#         filename_string = file.split('_')[-1].split('.')[0]
#         try:
#             temp_df = flow_df[[filename_string, 'date']]
#             merged_df = precip_df.merge(temp_df)
#             print(merged_df)
#         except:
#             # do nothing, precip id string does not exist in flow csv file
#             print(filename_string + " does not exist in flow data file")
#         break

with open('Basin_Precip_TS_for_model/basin_1134030.csv') as file:
    precip_df = pd.read_csv(file)
    # filename_string = file.split('_')[-1].split('.')[0]
    try:
        temp_df = flow_df[['1134030', 'date']]
        temp_df = temp_df.rename(columns={'date': 'Date'})
        # print(temp_df)
        # merged_df = precip_df.merge(temp_df)
        # merged_df = temp_df.merge(precip_df, how='inner')
        merged_df = pd.merge(temp_df, precip_df, how='inner')
        print(merged_df)
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