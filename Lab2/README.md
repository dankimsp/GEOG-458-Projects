# Lab2: Reclassification Vector Lab

### Daniel Kim

In this lab, we focused on creating a scripting tool using python. The scripting tool we built would create a new field within an inputed feature layer and reclassify the data for data visualization purposes.

My tool is located in: http://geog-gs01.geog.uw.edu:6080/arcgis/services/458_dankimsp/

Map of Seattle: 
  King County Population Density Reclassification:
![alt text](https://github.com/UW-Geog458-Win2018/dankimsp/blob/master/Lab2/King_toolresults.png)

Map of Nevada
  Population Densities of Census blocks in Nevada:

![alt text](https://github.com/UW-Geog458-Win2018/dankimsp/blob/master/Lab2/Nevada_cb_2016.png)

I created this data to represent 5 distinct densities of the different populations in each census block. 
- 0 representing populations under 1,000 people
- 1 representing populations between 1,000 to 2,000 people
- 2 representing populations between 2,000 to 5,000 people
- 3 representing populations between 5,000 to 900,000 people
- 4 representing populations between 900,000 to 999,999 people
The purpose was to create a visualization that allowed users to easily understand the population ranges living in each census block and make it easier for cartographers to symbolize the population data.
