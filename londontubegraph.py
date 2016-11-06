"""
londontubegraph.py - traverse the London tube system (Graph Traversal)
"""

# NOTE: these whole modules don't have to be imported
import os
import csv

class LondonTube:
    """Represents the London Tube System and provides information 
    about its stations (platforms) and the relationship between those stations.

    The class member _stationGraphDict stores the information that is gathered
    from a CSV file downloaded from the London Tube System.  It is initialized
    and then shared among instances for efficiency sake.
    
    The station graph is stored as a dictionary of dictionaries for quick 
    lookup (hashing).  So the first key would be the station name (for example,
    'East Ham') and its value would be the station's various attributes in 
    dictionary form (such as its 'Tube Line' and 'Neighbor List').
    
    A graph is a series of Nodes (or Vertexes) and Edges which are paths to 
    adjacent Nodes.  This class refers to these adjacent Nodes as Neighbors.

    """
    
    _stationGraphDict = None
    
    def __new__(cls):
        print('Calling London Tube new')
        if not cls._stationGraphDict:
            cls._stationGraphDict = dict()
            cls.loadLondonTube(cls)
        return super(LondonTube, cls).__new__(cls)
    
    def __init__(self):
        print('Calling London Tube constructor')
        self.resultsFromStation = list()
        self.visitedList = list()

    def findNeighbors(self, platform, graph, steps, visitedList):
        print('findNeighbors: ' + platform + ', ' + str(steps) + ', ')
        for vl in visitedList:
            print(platform + ' vl: ' + vl)
        visitedList.append(platform)
        if steps < 0:
            return
        if steps == 0:
            print("adding............." + platform)
            self.resultsFromStation.append(platform)
            return
        for neighbor in graph[platform]['neighborList']:
            print('platform: ' + platform + ', neighbor: ' + neighbor + ', steps: ' + str(steps))
            if neighbor in visitedList:
                print('skipping ' + neighbor + ': ' + str(steps))
                continue
            #else:
                #print('appending ' + neighbor + ' (to visitedList): ' + str(steps))
                #visitedList.append(neighbor)
            print('calling ' + neighbor + ': ' + str(steps))
            self.findNeighbors(neighbor, graph, steps - 1, visitedList)
            
            
    @staticmethod
    def loadLondonTube(cls):
        print('loadLondonTube.................')
        london_tube_file = open('London tube lines.csv')
        reader = csv.DictReader(london_tube_file)
        # try block to close file
        createTubeGraph(cls._stationGraphDict, reader, 500, 'From Station', 'To Station')
        london_tube_file.close()
        
            
    def createTubeGraph(self, parentDict, reader, num, platformKey, neighborKey):
        print('createTubeGraph.................')
        idx = 0
        for row in reader:
            if row[platformKey] in parentDict:
                if platformKey not in parentDict[row[platformKey]]:
                    parentDict[row[platformKey]] = row
                if 'neighborList' not in parentDict[row[platformKey]]:
                    parentDict[row[platformKey]]['neighborList'] = list()
                if row[neighborKey] not in parentDict[row[platformKey]]['neighborList']:
                    parentDict[row[platformKey]]['neighborList'].append(row[neighborKey])
            else:
                parentDict[row[platformKey]] = row
                parentDict[row[platformKey]]['neighborList'] = list()
                parentDict[row[platformKey]]['neighborList'].append(row[neighborKey])
            if row[neighborKey] in parentDict:
                if 'neighborList' not in parentDict[row[neighborKey]]:
                    parentDict[row[neighborKey]]['neighborList'] = list()
                if row[platformKey] not in parentDict[row[neighborKey]]['neighborList']:
                    parentDict[row[neighborKey]]['neighborList'].append(row[platformKey])
            else:
                parentDict[row[neighborKey]] = dict()
                parentDict[row[neighborKey]]['neighborList'] = list()
                parentDict[row[neighborKey]]['neighborList'].append(row[platformKey])
            idx = idx + 1
            if idx >= num:
                break
                
    def printNeighbors(self):
        print(sorted(self.resultsFromStation))
        self.resultsFromStation = list()