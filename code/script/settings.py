""""
This File describes the fixed parameter of the program
@author: Kodai Ito, 2015/10/07
"""

# Commmon Parameter
YEAR = 20                   #year
DISCOUNT_RATE = 0.07        #7%

# About VLCC
VLCC_DEADWEIGHT = 300000    #ton
VLCC_VELOCITY = 30          #km/h
VLCC_DISTANCE = 10605       #km
BCI_RATE = 0.7               #70%
VLCC_FC = 100               #ton/day fuel consumption
VLCC_BUILD = 150000000      #USD to build

# About BulkCapesize
# Cape Garland
# http://www.marinetraffic.com/ais/details/ships/shipid:728792/mmsi:371691000/imo:9397846/vessel:CAPE_GARLAND
BC_DEADWEIGHT = 178394    #ton
BC_VELOCITY = 18.5        #km/h
BC_DISTANCE = 5472	      #km  Japan to Australlia
BC_BUILD = 100000000      #USD to build # This must be changed!!!!!

# About BulkPanamax
# http://hudsonshipping.com/?q=node/95
BP_DEADWEIGHT = 72000    #ton
BP_VELOCITY = 26.5        #km/h
BP_DISTANCE = 5472	      #km  Japan to Australlia # This must be changed
BP_BUILD = 50000000      #USD to build # This must be changed!!!!!

# About BulkSupramax
# http://hudsonshipping.com/?q=node/95
BS_DEADWEIGHT = 55000    #ton
BS_VELOCITY = 26.5        #km/h
BS_DISTANCE = 5472	      #km  Japan to Australlia # This must be changed
BS_BUILD = 30000000      #USD to build # This must be changed!!!!!

