# StreamTeam

Outline(3/19)

Introduction

Rivers and streams have maintained and modified ecosystems by mediating ecosystem structure and facilitating nutrient cycling for billions of years, but in recent years, water sources have become increasingly controlled and altered by humans, such as building dams and climate change.

The catchment area is a collection of rainfall over a natural drainage area.  In hydrolysis, it's the partition, storage, and release of water. The catchment area can also be used to study and model the water balance of an area. 

The runoff ratio, or the fraction of runoff generated by a given amount of precipitation, is how we measure hydrolysis and watershed in a given area. It's the proportion of rainfall that does not infiltrate(not absorbed into the catchment), and is not taken up by evapotranspiration, and thus ends up as runoff. 

We will need to calculate the slope of all runoff coefficients from daily data for each stream, then plot these slopes against a number of x-values (for example, number of dams or latitude) to identify characteristics of basins with highly changing runoff coefficients
divide slope by mean to get percent change
do it years at a time, not all of the data we have
we will identify characteristics common in basins with highly changing runoffs to quantify how much human activity impacts water runoff globally

Results: What we're looking for

-Name general basin characteristics
-What kinds of basins tend to have highly changing runoff ratios? for example, certain soil types, certain precipitation levels, etc
-Identify cities/geographical areas based on above basin characteristics
-Show which parts of the world are most affected by changing runoff ratios
-Predict areas that are likely to be susceptible to changing runoff ratios in the future
figures
-Box and whisker plot for statistically significant basin characteristics
world (or US) map marking percent change of runoff ratios per location
-Empirical distribution for the prob of local spatial similarity in streamflow metric


Repoducibility(04/05)

Requirements:
All the code is in python. It was orignially coded in the PyCharm IDE and it runs on Windows and MAC machines.

The package dependencies include:
pandas
numpy
sklearn
matplotlib
matplotlib.pyplot

To install dependencies:
1. Install pip
  python -m pip install -U pip
  
2. Install "dependecy"
  python -m pip install -U matplotlib
  You can replace matplotlib with any dependency package.
  


The data is contained in BoxDrive. The files are a few GBS. To avoid downloading them to your computer, we will use the Box app instead.

To get the files on your local machine follow these steps:

1.
follow this link to get access to the files from your box account. 
https://byu.box.com/s/oqvmb58twh5c84xbvg7egecnlhdw8syr

2.
Once the files are shared on your Box, download the box app onto your personal computer using this link. Make sure you select the correct operating system of your device.
https://www.box.com/resources/downloads

3.
Once you get the app download, check your file explorer for the box tab. Click the tab and the folder named "Stream Team Dream Team" should be present. Click the folder and the databases will be there. This image below is an example of the boxapp in windows file explorer.

![image](https://user-images.githubusercontent.com/56054621/230814321-1ea02fab-b1ec-4b22-a50c-51216842cbd3.png)

4.
To get the files to your IDE of choice, you have to copy the direct path from file Explorer.
From the file explorer, right click on the file you want
Click on properties.
Properties contains the direct path minus the file name. You will need to copy the direct path and write in the file name when you want to read the csv's in your code.

Here's a picture of what it should look like when you click properties. 
![image](https://user-images.githubusercontent.com/56054621/230815828-539eb2cd-8214-4cf5-83ec-7808b8160876.png)


In figure_1.py, the full path needs to be changed to your full path on line 19
For line 25 - 35, all the files in parentheses need to be changed to the full path name. 

In home.py, the full path needs to be changed to your full path on line 19
For line 27 - 35, all the files in parentheses need to be changed to the full path name.

Make sure you swith the backslashes to forward slahes. 

Here's an example:

df_catchment = pd.read_csv('C:/Users/atamb/Box/Stream Team Dream Team/allDailyFlowData.csv',encoding="ISO-8859-1")

Figure 1(03/23)

Check Figure_1.py for code:
https://github.com/RepTambe/StreamTeam/blob/main/figure_1.py


For figure 1:
When you run the code you'll get the year one plot first. Then when you exit out of it, year 2 will pop up. 
<img width="1472" alt="Screen Shot 2023-04-10 at 9 46 37 AM" src="https://user-images.githubusercontent.com/56054621/230939212-3dee4110-4d64-4e5e-894c-1efbe0c613df.png">

Figure 2(03/08/23)

![image](https://user-images.githubusercontent.com/56054621/230939583-cedfb843-2dd4-49f5-afe9-5c3310c26ebf.png)

Check home.py for code:
https://github.com/RepTambe/StreamTeam/blob/main/home.py

Figure 2 is line 211

Figure 3 is line 222

Area plot is 229

Continents is 233

To see a certain plot, uncomment the line, comment out the other plots. 




