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

1. Download code  
...from https://github.com/MayorCurley/londontube.git  
2. Install londontubegraph module  
...python setup.py install  
3. Start up Python REPL  
...python  
...>>>  
4. Import londontubegraph  
...import londontubegraph as ltg  
5. Create LondonTube instance  
...london_tube = ltg.LondonTube()  
6. Invoke LondonTube.displayNeighbors() method  
...example  
...london_tube.displayNeighbors('East Ham', 4)  
