# Lab 2
# 
### Daniel Kim


# importing arcpy
import arcpy


# Defining parameters that user will input
orig_shapefile = arcpy.GetParameterAsText(0)
infield = arcpy.GetParameterAsText(1)
outfield = arcpy.GetParameterAsText(2)
reclasstable = arcpy.GetParameterAsText(3)
notfoundvariable = arcpy.GetParameterAsText(4)
output_shapefile = arcpy.GetParameterAsText(5)


# Creates a copy of original shapefile into the output shapefile name
# Looked up the parameters on ArcGIS website
arcpy.CopyFeatures_management(orig_shapefile, output_shapefile)


# Add a field to the newly copied shapefile and name it with user input
# Looked up the parameters on ArcGIS website
arcpy.AddField_management(output_shapefile, outfield, 'DOUBLE')


# Create a update cursor for the copied feature class
field = [infield, outfield]
class_cursor = arcpy.da.UpdateCursor(output_shapefile, field)


# Create a search cursor for the reclass table 
# had to remind myself of the parameters on arcgis website
field1 = ['lowerbound', 'upperbound', 'value']
reclass_cursor = arcpy.da.SearchCursor(reclasstable, field1)


# Iterate through the copied shapefile and determine if the value of the infield matches 
# the boundaires presented in the reclass table. 
# If not, replace with the output of the notfoundvariable if user doesn't want to keep the original value
for row in class_cursor:
    for row0 in reclass_cursor:
        if (row[0] >= row0[0] and row[0] <= row0[1]):
            row[1] = row0[2]
            break # breaks from loop when value within reclasstable is found
                  # found this strategy in stackoverflow
    if (row[1] == 0):
        row[1] = notfoundvariable
    reclass_cursor.reset() # resets the reclass table cursor to iterate again with
                           # every row in the feature class
    class_cursor.updateRow(row) # Updates Feature class cursor to save changes


# delete cursors
del reclass_cursor, class_cursor
