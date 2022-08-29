from ast import For
import pandas as pd
import matplotlib.pyplot as plt
import rootAParse
import rootKParse

import utils.PercentageUtils as PercentageUtils

import json
from pathlib import Path

#######################################################
# ROOT A

rootAJSONFilePaths = ('../Medição 1 A IPV4.json', '../Medição 2 A IPV4.json', '../Medição 3 A IPV6.json', '../Medição 4 A IPV6.json')

rootAFilePathIndex = 1
        
for rootAMetricFilePath in rootAJSONFilePaths :

    rootAResponsesByIpSrc = rootAParse.parseMetrics(rootAMetricFilePath)

    # rootAResponsesByIpSrc : { "IPVX" : [ "dst_addr" ] }
    
    rootATotalResponsesCount = 0
       
    rootALocationsTotalResponses = {}
       
    for ipSrcAddress in rootAResponsesByIpSrc :
        
        rootALocationResponsesFromIPSrc = rootAResponsesByIpSrc[ipSrcAddress]
        
        for rootALocationResponse in rootALocationResponsesFromIPSrc :
                
            print(rootALocationResponse)
                
            if rootALocationResponse in rootALocationsTotalResponses :
    
                rootALocationsTotalResponses[rootALocationResponse] += 1
                
                rootATotalResponsesCount += 1

            else :
                
                rootALocationsTotalResponses[rootALocationResponse] = 0
                
                rootATotalResponsesCount += 1

    print(json.dumps(rootALocationsTotalResponses))

    print(rootATotalResponsesCount)
    
    percentagesPerLocation = []
    
    totalPercentage = 0
    
    for rootALocation in rootALocationsTotalResponses :
        
        locationTotal = rootALocationsTotalResponses[rootALocation]
        
        locationPercentage = locationTotal * 100 / rootATotalResponsesCount
        
        percentagesPerLocation.append( { rootALocation : locationPercentage } )  
        
        totalPercentage += locationPercentage

    
    print(percentagesPerLocation)
    
    
    print(json.dumps(percentagesPerLocation, indent=4))

    rootAMetricFilePath = rootAMetricFilePath.replace(r'.', '')   
   
    rootAMetricFilePath = rootAMetricFilePath.replace(r'/', '')
    
    rootAMetricFilePath = rootAMetricFilePath.replace('json', '')
    
    # var2017 = []
    
    var022 = []
    
    index = ['Test']
    
    locationKeys = []
    
    locationOthersKey = 'Outros'
    
    locationOthersPercentage = 0
    
    index = 1
    
    for locationDict in percentagesPerLocation :
    
        locationKey = list(locationDict)[0]
        
        locationPercentage = locationDict[locationKey]
        
        if locationPercentage > 1.0 :
        
            var022.append(locationDict[locationKey])
        
            locationKeys.append(locationKey)
            
            print(locationKey)
        
        else :
        
            locationOthersPercentage += locationPercentage      
    
        if len(percentagesPerLocation) == index :

            var022.append(locationOthersPercentage)
            
            locationKeys.append(locationOthersKey)
        
        index += 1 
    
    print(locationKeys)

    print(var022)
    
    yearOfMeasurement = '2022' 
    
    if ( rootAFilePathIndex%2==0 ) :
        
        yearOfMeasurement = '2017'
        
   
    if ( rootAFilePathIndex > 2 ) :
            
        yearOfMeasurement += ' IPV6'
        
    else :
        
        yearOfMeasurement += ' IPV4'
    
    df = pd.DataFrame({
        # '2017': var2017,
        yearOfMeasurement : var022
        
        }, index=locationKeys)
    
    ax = df.plot(subplots=True, kind='pie',
        figsize=(20, 18), autopct='%1.1f%%')
    
    # ax.pie()
    
    # plt.figure(figsize=(20, 3))  # width:20, height:3
    
    # plt.bar((locationKeys), var022, align='edge', width=0.3)

    plt.savefig( rootAMetricFilePath + '.png' )
    
    rootAFilePathIndex += 1

    # plt.show()



    
    # print(rootALocationsTotalResponses)

    # var2017 = [0.1, 17.5, 40, 48, 52, 69, 88]
    # var022 = [2, 8, 70, 1.5, 25, 12, 28]
    # index = ['snail', 'pig', 'elephant',
    #          'rabbit', 'giraffe', 'coyote', 'horse']
    # df = pd.DataFrame({'2017': var2017,
    #                    '2022': var022}, index=index)
    # ax = df.plot.bar(rot=0)

    # plt.savefig( rootKMetricFilePath + '.png' )

    # plt.show()


#######################################################
# ROOT K

rootKJSONFilePaths = ('../Medição 5 K IPV4.json', '../Medição 6 K IPV4.json', '../Medição 7 K IPV6.json', '../Medição 8 K IPV6.json')

rootKFilePathIndex = 1

for rootKMetricFilePath in rootKJSONFilePaths :

    rootKResponsesByIpSrc = rootKParse.parseMetrics(rootKMetricFilePath)
    
    # rootKResponsesByIpSrc : { "IPVX" : [ "dst_addr" ] }
        
    rootKTotalResponsesCount = 0
    
    rootKLocationsTotalResponses = {}
        
    for ipSrcAddress in rootKResponsesByIpSrc :
     
        rootKLocationResponsesFromIPSrc = rootKResponsesByIpSrc[ipSrcAddress]
        
        for rootKLocationResponse in rootKLocationResponsesFromIPSrc :
                
            print(rootKLocationResponse)
                
            if rootKLocationResponse in rootKLocationsTotalResponses :
    
                rootKLocationsTotalResponses[rootKLocationResponse] += 1
        
                rootKTotalResponsesCount += 1
                
            else :
                
                rootKLocationsTotalResponses[rootKLocationResponse] = 0
                
                rootKTotalResponsesCount += 1
                
    print(json.dumps(rootKLocationsTotalResponses))
        
    print(rootKTotalResponsesCount)
    
    percentagesPerLocation = []
    
    totalPercentage = 1
    
    for rootKLocation in rootKLocationsTotalResponses :
        
        locationTotal = rootKLocationsTotalResponses[rootKLocation]
        
        locationPercentage = locationTotal * 100 / rootKTotalResponsesCount
        
        percentagesPerLocation.append( { rootKLocation : locationPercentage } ) 
        
        totalPercentage += locationPercentage

    print(totalPercentage)
    
    # exit()

    print(json.dumps(percentagesPerLocation, indent=4))

    rootKMetricFilePath = rootKMetricFilePath.replace(r'.', '')   
   
    rootKMetricFilePath = rootKMetricFilePath.replace(r'/', '')
    
    rootKMetricFilePath = rootKMetricFilePath.replace('json', '')
    
    # var2017 = []
    
    var022 = []
    
    index = ['Test']
    
    locationKeys = []
    
    locationOthersKey = 'Outros'
    
    locationOthersPercentage = 0
    
    index = 1
    
    for locationDict in percentagesPerLocation :
    
        locationKey = list(locationDict)[0]
        
        locationPercentage = locationDict[locationKey]
        
        if locationPercentage > 1.0 :
        
            var022.append(locationDict[locationKey])
        
            locationKeys.append(locationKey)
            
            print(locationKey)
        
        else :
        
            locationOthersPercentage += locationPercentage      
    
        if len(percentagesPerLocation) == index :

            var022.append(locationOthersPercentage)
            
            locationKeys.append(locationOthersKey)
        
        index += 1 
    
    print(locationKeys)

    print(var022)

    # Example START
    
    # var2017 = [0.1, 17.5, 40, 48, 52, 69, 88]
    # var022 = [2, 8, 70, 1.5, 25, 12, 28]
    # index = ['snail', 'pig', 'elephant',
    #          'rabbit', 'giraffe', 'coyote', 'horse']
    # df = pd.DataFrame({'2017': var2017,
    #                    '2022': var022}, index=index)
    
    # Example END
    
    yearOfMeasurement = '2022'
    
    if ( rootKFilePathIndex%2==0 ) :
        
        yearOfMeasurement = '2017'
    
    
    if ( rootKFilePathIndex > 2 ) :
            
        yearOfMeasurement += ' IPV6'
        
    else :
        
        yearOfMeasurement += ' IPV4'
    
    df = pd.DataFrame({
        # '2017': var2017,
        yearOfMeasurement : var022
        }, index=locationKeys)
    
    
    ax = df.plot(subplots=True, kind='pie',
        figsize=(28, 24), autopct='%1.1f%%')
    
    
    # plt.figure(figsize=(20, 3))  # width:20, height:3
    
    # plt.bar((locationKeys), var022, align='edge', width=0.3)

    plt.savefig( rootKMetricFilePath + '.png' )
    
    rootKFilePathIndex+=1

    # plt.show()


    ##########################################################3
    #  COMPARAÇÃO ANO 2017 E ANO 2022

