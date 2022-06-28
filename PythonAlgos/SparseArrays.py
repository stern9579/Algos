

def matchingStrings(strings, queries):
    strDict = {}
    output = []
    for string in strings:
        
        if string not in strDict.keys():
            strDict[string] = 1
        else:
            strDict[string] = strDict[string] + 1
    
    for query in queries:
        if query in strDict.keys():
            output.append(int(strDict[query]))
            # print(int(strDict[query]))
        else:
            output.append(int(0))
            
    return output