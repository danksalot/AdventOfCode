import re
import math

with open('testInput') as inFile:
	i = [ list( map( int, re.findall( "-?\d+", l ) ) ) for l in inFile.read().splitlines() ]
s = { ( sx, sy, abs( sx - bx ) + abs( sy - by ) ) for sx, sy, bx, by in i }

# Part 1
xl = math.inf
xh = -math.inf
for sx, sy, sc in s:
    dx = sc - abs( 2000000 - sy )
    if dx > 0:
        xl = min( xl, sx - dx )
        xh = max( xh, sx + dx )
print( xh - xl )

# Part 2
for sensorX, sensorY, distance in s:
    for rotationalOffset in range(distance + 1 ):
        for candX, candY in ( ( sensorX - distance - 1 + rotationalOffset, sensorY - rotationalOffset ),
                        ( sensorX + distance + 1 - rotationalOffset, sensorY - rotationalOffset ),
                        ( sensorX - distance - 1 + rotationalOffset, sensorY + rotationalOffset ),
                        ( sensorX + distance + 1 - rotationalOffset, sensorY + rotationalOffset ) ):
            print('Checking', candY, candX)
            if ( 0 <= candX <= 20 and
                 0 <= candY <= 20 and
                 all( abs( candX - ox ) + abs( candY - oy ) > od
                      for ox, oy, od in s ) ):
                print(distance, rotationalOffset,  candX * 4000000 + candY )
                exit()