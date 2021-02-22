# A bus has to travel from A to B and the distance is d miles. There are many gas stations between A and B.
# The bus has initially g gallon of gas in tank. 1 gallon of gas travels 1 mile.
#
# Gas stations have inforamtion of remaining distance from station to destination b and max gas that can be filled from the station.
# Find the minimum number of stops for bus without running out of gas ever.
#
# eg: gas = 10 , distance = 20
# gasStation[] = {{16,3}, {10, 7}, {14, 11},{11, 5}, {7, 6}}
#
# o/p = 1
# If bus stops at the stop{14,11} that is 14 miles away from destination and fills 11 gallon then it can reach destination with 1 gallon spare.
# It can also stop as {16,3} and {10,7} but its 2 stops and at destination it runs out of gas.
# Similarly {11, 5}, {7, 6} has 2 stops but has 1 gallon spare at destination.
