Mongo Database Name: World_Data

Collection Names:
  airports
  states
  volcanos
  earthquakes
  meteorites
  
  Batch file run from Windows based platform with geojson files in this location:
    C:\Users\Admin\OneDrive\4553-Spatial-DS\Spatial-DS-Weems\Assignments\program_5\geojson\
  
  Batch file needs to be in Mongo folder /bin
 
    
Example Queries:

py query1.py DFW LAX 500
py query1.py LAX DFW 500
py query1.py DFW OHD 500
py query1.py OHD DFW 500

py query2.py earthquakes magnitude 3 min 5 3000
py query2.py volcanos altitude 1000 min 0 3000
py query2.py meteors mass 1000 min 3 3000
py query2.py 2000

py query3.py volcano 15 5

