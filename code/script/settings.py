""""
This File describes the fixed parameter of the program
@author: Kodai Ito, 2015/10/07
"""
import logging
logging.basicConfig(level="INFO")
# Commmon Parameter
YEAR = 15                   #year
DISCOUNT_RATE = 0.07        #7%

# About VLCC
VLCC_DEADWEIGHT = 300000    #ton
VLCC_VELOCITY = 30          #km/h
VLCC_DISTANCE = 10605       #km
WS_RATE = 0.7               #70%
VLCC_FC = 100               #ton/day fuel consumption
VLCC_BUILD = 120000000      #USD to build
VLCC_OPE = 200000			#Operation cost
VLCC_OTHER = 100000			#Other cost

# source of building cost: http://marketrealist.com/2013/07/new-capesize-price-jumps-most-in-5-years-positive-for-dry-bulk-shipping-stocks/

# About BulkCapesize
# Cape Garland
# http://www.marinetraffic.com/ais/details/ships/shipid:728792/mmsi:371691000/imo:9397846/vessel:CAPE_GARLAND
#BC_DEADWEIGHT = 178394    	#ton
#BC_VELOCITY = 18.5        	#km/h
#BC_DISTANCE = 5472	      	#km  Japan to Australlia
BC_BUILD = 60000000      	#USD to build # This must be changed!!!!!
BC_OPE = 100000				#Operation cost
BC_OTHER = 80000			#Other cost

# About BulkPanamax
# http://hudsonshipping.com/?q=node/95
#BP_DEADWEIGHT = 72000     	#ton
#BP_VELOCITY = 26.5        	#km/h
#BP_DISTANCE = 5472	      	#km  Japan to Australlia # This must be changed
BP_BUILD = 40000000       	#USD to build # This must be changed!!!!!
BP_OPE = 70000				#Operation cost
BP_OTHER = 70000			#Other cost

# About BulkSupramax
# http://hudsonshipping.com/?q=node/95
#BS_DEADWEIGHT = 55000     	#ton
#BS_VELOCITY = 26.5        	#km/h
#BS_DISTANCE = 5472	      	#km  Japan to Australlia # This must be changed
BS_BUILD = 20000000       	#USD to build # This must be changed!!!!!
BS_OPE = 50000				#Operation cost
BS_OTHER = 20000			#Other cost

