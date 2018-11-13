import csv
outputFileNameOfTransit = '../data/result_transit.csv'
outputFileNameOfTotal = '../data/result_total.csv'
travelZoneDistrictCentroidDict={}

with open('./data/TAZ1669.csv','r') as source:
    reader = csv.reader(source,delimiter = ',')
    for i in reader:
        travelZoneDistrictCentroidDict[i[0]] = [i[1],i[2],i[3]]
    source.close()

#Generate './public/data/result_transit.csv'
transitResult = {}

with open("./data/trips_1.csv",'r') as tripData:
    print('start')
    reader = csv.reader(tripData,delimiter = ',')
    for i in reader:
        break
    for i in reader:
        if i[26]!='TR':
            continue #if generate result_transit.csv
        splitPurpose = i[7].split('_')
        purpose = None
        if splitPurpose[1] == 'O':
            purpose = 'O'
        elif splitPurpose[1]=='W':
            purpose = 'W'
        elif splitPurpose[1]=='B':
            purpose = 'B'
        elif splitPurpose[0]=='PSE' and splitPurpose[1] == 'S':
            purpose = 'PSE_S'
        elif splitPurpose[1] == 'S':
            purpose = 'Other_S'
        if tuple([travelZoneDistrictCentroidDict[i[10]][0],travelZoneDistrictCentroidDict[i[11]][0],purpose]) in transitResult:
            transitResult[tuple([i[10],i[11],purpose])] += 1 ####Trips/1???
        else:
            transitResult[tuple([i[10],i[11],purpose])] = 1

print('Start writing into output file')


with open(outputFileNameOfTransit,'w') as myfile:
    myfile.close()

csvWriter = csv.writer(open(outputFileNameOfTransit,'w', newline=''))
csvWriter.writerow(['OriginZoneTAZ1669EETP','OriginZoneDistrictTAZ1669EETP','DestZoneTAZ1669EETP','DestZoneDistrictTAZ1669EETP','Purpose_Category','Total','Origin_XCoord','Origin_YCoord','Dest_XCoord','Dest_YCoord'])
for k,v in transitResult.items():

    print(travelZoneDistrictCentroidDict[str(k[0])])

    OriginDistrict= travelZoneDistrictCentroidDict[str(k[0])][0]
    DestDistrict = travelZoneDistrictCentroidDict[str(k[1])][0]
    OriginX = travelZoneDistrictCentroidDict[str(k[0])][1]
    OriginY = travelZoneDistrictCentroidDict[str(k[0])][2]
    DestX = travelZoneDistrictCentroidDict[str(k[1])][1]
    DestY = travelZoneDistrictCentroidDict[str(k[1])][2]
    Weight = v
    csvWriter.writerow([k[0],OriginDistrict,k[1],DestDistrict,k[2],Weight,OriginX,OriginY,DestX,DestY])


#Generate './public/data/result_total.csv'
totalResult = {}
with open("./data/trips_1.csv",'r') as tripData:
    print('start')
    reader = csv.reader(tripData,delimiter = ',')
    for i in reader:
        break
    for i in reader:

        splitPurpose = i[7].split('_')
        purpose = None
        if splitPurpose[1] == 'O':
            purpose = 'O'
        elif splitPurpose[1]=='W':
            purpose = 'W'
        elif splitPurpose[1]=='B':
            purpose = 'B'
        elif splitPurpose[0]=='PSE' and splitPurpose[1] == 'S':
            purpose = 'PSE_S'
        elif splitPurpose[1] == 'S':
            purpose = 'Other_S'
        if tuple([travelZoneDistrictCentroidDict[i[10]][0],travelZoneDistrictCentroidDict[i[11]][0],purpose]) in totalResult:
            totalResult[tuple([i[10],i[11],purpose])] += 1 ####Trips/1???
        else:
            totalResult[tuple([i[10],i[11],purpose])] = 1

print('Start writing into output file')


with open(outputFileNameOfTotal,'w') as myfile:
    myfile.close()

csvWriter = csv.writer(open(outputFileNameOfTotal,'w', newline=''))
csvWriter.writerow(['OriginZoneTAZ1669EETP','OriginZoneDistrictTAZ1669EETP','DestZoneTAZ1669EETP','DestZoneDistrictTAZ1669EETP','Purpose_Category','Total','Origin_XCoord','Origin_YCoord','Dest_XCoord','Dest_YCoord'])
for k,v in totalResult.items():

    print(travelZoneDistrictCentroidDict[str(k[0])])

    OriginDistrict= travelZoneDistrictCentroidDict[str(k[0])][0]
    DestDistrict = travelZoneDistrictCentroidDict[str(k[1])][0]
    OriginX = travelZoneDistrictCentroidDict[str(k[0])][1]
    OriginY = travelZoneDistrictCentroidDict[str(k[0])][2]
    DestX = travelZoneDistrictCentroidDict[str(k[1])][1]
    DestY = travelZoneDistrictCentroidDict[str(k[1])][2]
    Weight = v
    csvWriter.writerow([k[0],OriginDistrict,k[1],DestDistrict,k[2],Weight,OriginX,OriginY,DestX,DestY])
