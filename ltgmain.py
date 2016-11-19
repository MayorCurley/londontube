import sys
import londontubegraph as ltg

def main(argv = None):
    if argv is None:
        argv = sys.argv

    station_input = ''
    
    while station_input != 'exit':

        station_input = input('What station would you like to start from? (type exit to end program)  ')
        if station_input != 'exit':
            step_input = input('How many steps from the station would you like to go?  (positive numbers only)  ')

        if station_input and station_input != 'exit' and step_input:
            london_tube = ltg.LondonTube()

            print('')
            print('')
            if int(step_input) >= 0:
                print('==========================================================================')
                print('Tubes just steps away')
                print('==========================================================================')

            london_tube.printNeighbors(str(station_input), int(step_input))

            print('')
            print('')
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

