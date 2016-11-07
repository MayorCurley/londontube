"""
londontubegraph.py - traverse the London tube system (Graph Traversal)
"""

# NOTE: these whole modules don't have to be imported
import os
import csv
from collections import OrderedDict

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
    
    # stores the information about the London Tube System and its stations
    # the 'London tube lines.csv' file is loaded in to this collection
    _stationGraphDict = None
    
    def __new__(cls):
        print('Calling London Tube new')
        
        if not cls._stationGraphDict:
            cls._stationGraphDict = dict()
            cls.loadLondonTube(cls)
        
        return super(LondonTube, cls).__new__(cls)
    
    def __init__(self):
        print('Calling London Tube constructor')

    def findNeighbors(self, platform, graph, steps, visitedList=[]):
        print('findNeighbors: ' + platform + ', ' + str(steps) + ', ')
        for vl in visitedList:
            print(platform + ' vl: ' + vl)
        
        resultStations = []
        visitedList.append(platform)
        
        if steps < 0:
            return sorted(set(resultStations))
        
        if steps == 0:
            print("adding............." + platform)
            resultStations.append(platform)
            return sorted(set(resultStations))
        
        for neighbor in graph[platform]['neighborList']:
            print('platform: ' + platform + ', neighbor: ' + neighbor + ', steps: ' + str(steps))
            if neighbor in visitedList:
                print('skipping ' + neighbor + ': ' + str(steps))
                continue
            #else:
                #print('appending ' + neighbor + ' (to visitedList): ' + str(steps))
                #visitedList.append(neighbor)
            print('calling ' + neighbor + ': ' + str(steps))
            resultStations += self.findNeighbors(neighbor, graph, steps - 1, visitedList)
        
        return sorted(set(resultStations))
            
            
    @staticmethod
    def loadLondonTube(cls):
        print('loadLondonTube.................')
        
        london_tube_file = open('London tube lines.csv')
        reader = csv.DictReader(london_tube_file)
        
        try:
            createTubeGraph(cls._stationGraphDict, reader, 500, 'From Station', 'To Station')
        finally:
            london_tube_file.close()
        
            
    def createTubeGraph(self, parentDict, reader, platformKey, neighborKey):
        print('createTubeGraph.................')
        #idx = 0
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
            #idx = idx + 1
            #if idx >= num:
            #    break
                
    def printNeighbors(self, startingStation, steps):
        startingStationTubeLine = self._stationGraphDict[startingStation]['Tube Line']
        rs = self.findNeighbors(startingStation, self._stationGraphDict, steps)
        
        for neighbor in rs:
            neighborStationTubeLine = self._stationGraphDict[neighbor]['Tube Line']
            tubeLines = OrderedDict.fromkeys([startingStationTubeLine,neighborStationTubeLine])
            print(neighbor + ' (lines = ' + ', '.join(tubeLines) + ')')