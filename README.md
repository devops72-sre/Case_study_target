# Case_study_target

Case Study for target

- Install the requirements if not installed.

    `pip install -r requirements.txt`
    
 - Run the commands as below to tell you how long it is until
the next bus on “BUS ROUTE” leaving from “BUS STOP NAME” going “DIRECTION”
using the api defined at http://svc.metrotransit.org/, where
  
   - “BUS ROUTE” will be a substring of the bus route name which is only in one bus
route

   - “BUS STOP NAME” will be a substring of the bus stop name which is only in one bus
stop on that route

   - “DIRECTION” will be “north” “east” “west” or “south”
   
 - Eg, if you wanted to know the next bus leaving from our Brooklyn Park campus to
our downtown campus:
 
    $ python nextbus.py “Express - Target - Hwy 252 and 73rd Av P&R - Mpls” “Target
    North Campus Building F” “south”
    
      2 Minutes 

(note that that won’t return anything if the last bus for the day has already left)

