# londontube

Coding challenge to traverse the London Tube System via platform and number of station steps

This application is written to meet the following requirements:

London Tube
Given a list of London Tube stations and lines, write an application to answer the following question:  
What stations have a minimum N stops from East Ham?  Print the results in alphabetical order.

For example, if N = 4, the results would be:

Abbey Road (lines = District, DLR)  
Bromley-by-Bow (lines = District)  
Canning Town (lines = District, Jubilee)  
Dagenham Heathway (lines = District)  
Leytonstone High Road (lines = District, Overground)  
Star Lane (lines = District, DLR)  
Stratford (lines = District, Jubilee)  

You may use any language and tools to write your application but please use GitHub.com to store your code.  

Resources  

·         London Tube Map: https://tfl.gov.uk/cdn/static/cms/images/tube-map.gif  
·         List of Tube stations: https://www.doogal.co.uk/london_stations.php (select "Download" then "Tube line data CSV" to download a list of stations and their lines)

### How to run London Tube

This was written on Windows with Python version 3.5.2

1. Download code  
   from https://github.com/MayorCurley/londontube.git  
2. Install londontubegraph module  
   python setup.py install  
3. Start up Python REPL  
   python  
   >>>  
4. Ensure the 'London tube lines.csv' file is in the working directory  
   This file contains the station information that is loaded  
   to create the graph  
5. Import londontubegraph  
   import londontubegraph as ltg  
6. Create LondonTube instance  
   london_tube = ltg.LondonTube()  
7. Invoke LondonTube.printNeighbors() method  
   The LondonTube class printNeighbors method has the following signature:  
   printNeighbors(self, startingStation, steps)  
   example:  
   london_tube.printNeighbors('East Ham', 4)  

### About LondonTube Class  

  """Represents the London Tube System and provides information  
  about its stations (platforms) and the relationship between those stations.

  The class member _stationGraphDict stores the information that is gathered  
  from a CSV file downloaded from the London Tube System. It is initialized  
  and then shared among instances for efficiency sake.  

  The station graph is stored as a dictionary of dictionaries for quick  
  lookup (hashing). So the first key would be the station name (for example,  
  'East Ham') and its value would be the station's various attributes in  
  dictionary form (such as its 'Tube Line' and 'Neighbor List').  
 
  A graph is a series of Nodes (or Vertexes) and Edges which are paths to  
  adjacent Nodes. This class refers to these adjacent Nodes as Neighbors.  
  """
  
  #### def _findNeighbors(self, platform, graph, steps, visitedList=None)
  
    """  
    Finds the neighbors of the platform (station) parameter that  
    are reached from the specified amount of steps.
    
    This method uses recursion to traverse the graph (that represents  
    the tube system) and retrieve the requested station neighbors.  
    """
    
  #### def loadLondonTube(cls)
  
    """  
    Loads the London Tube graph from an informational CSV file  
    """
    
  #### def _createTubeGraph(self, parentDict, reader, platformKey, neighborKey)
  
    """  
    Main workhorse for loading the London Tube graph.  
    
    The graph is stored as a dictionary of dictionaries.  The parent  
    dictionary contains the station name as a key (for quick lookup)  
    while the the child dictionary holds the attributes, such as the  
    neighbor list of the station.  
    
    The graph is designed so that each station holds its neighbor list  
    so the graph can be traversed by steps to find its requested neighbor  
    stations.  
    """
    
  #### def printNeighbors(self, startingStation, steps)
  
    """  
    This method allows the client to specify the station from  
    which they wish to start from and how many steps to take to find  
    its neighbors.  The neighbors and their respective lines are displayed.  
    """
    

