import json

def calculatePercentageOfEachLocation(rootKResponsesByIpSrc, rootKTotalResponsesCount) :
    
    rootKLocationsTotalResponses = {}
        
    for ipSrcAddress in rootKResponsesByIpSrc :
     
        rootKLocationResponsesFromIPSrc = rootKResponsesByIpSrc[ipSrcAddress]
        
        for rootKLocationResponse in rootKLocationResponsesFromIPSrc :
                
            print(rootKLocationResponse)
                
            if rootKLocationResponse in rootKLocationsTotalResponses :
    
                rootKLocationsTotalResponses[rootKLocationResponse] += 1
                
            else :
                
                rootKLocationsTotalResponses[rootKLocationResponse] = 0
        
        rootKTotalResponsesCount += 1
        
    print(json.dumps(rootKLocationsTotalResponses))