# Trip Cluster Tool


This is a [Nodejs](https://docs.npmjs.com/getting-started/installing-node)
web application. The Weighted-Kmeans algorithm is used for clustering. The App can show clustering results after each iterations on the map. This is a simplified version of Travel Cluster Tool.
## Set Up
#### From GitHub
1. Download the folder
2. Go to the root of the folder, and run some npm commands in the terminal/cmd. If 'npm' is not found, then you may need to install nodejs first...
    * npm install
    * npm install --save express
    * npm install --save Blob
    * npm install --save child-process
    * npm install --save http-errors
    * npm install --save jade
    * npm install --save jsdom
    * npm install --save morgan
    * npm install --save fs
    * npm install --save socket.io
   
#### From Lab Computer I
1. Go to the root foler './Trips_Cluster_Tool'
2. The district geojson file is stored in './public/data/geoInfo'. The geojson file has been converted to EPSG4326. 
3. The csv source file is './public/data/Origin_Dest_Zones_by_Trip_Purpose_3776.csv'. Please be cautious that the csv file should use EPSG3776 as Spatial reference. EPSG3776 is a local spatial reference which uses meters. The reason why not using EPSG4326 is that 4326 is a global reference which is not in meters. It will be unprecise if we use EPSG4326 to calculate the distance.
4.'./data/result_total.csv' is trips of all methods. './data/result_transit.csv' is trips of transit.

## Generate Data Source
1. The './data/result_total.csv' and './data/result_transit.csv' are generated from 'trips_1.csv' and 'TAZ1669.csv' stored in './public/python/data'. 
2. './public/python/filterTrips.py' is a python script which could generate './data/result_total.csv' and './data/result_transit.csv'.
3. If you have updated the data stored in './public/python/data', you should use a cmd/terminal to run 'python35 filterTrips.py'. After about 2 minutes, the './public/data/result_total.csv' and './public/data/result_transit.csv' will finish updating process.

## Run The Application
#### 1. Use your terminal going to the root './Trips_Cluster_Tool' and type 'npm start'
1. You can see some messages in the terminal.

#### 2. Use Google Chrome or Firefox to browse "https://localhost:3044". Firefox may work better than Google Chrome. 

## Current Issues:
1. Sometimes, when you click on a line, the application may not show dots properly. You should terminate the browser and restart the browser.

## Some Tips:
1. All the lines are clickable, no matter it is a blue(single) line or red(clustered) line.
2. The slider can let the app run Kmeans continuously, but 20 iterations may be good enough. Don't leave it run forever(though it will stop after 200 iterations), it may occupy your cpu resource.
3. This version of flow cluster tool only uses one thread to do K-Means clustering.

