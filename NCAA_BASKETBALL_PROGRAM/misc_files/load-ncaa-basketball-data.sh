#!/bin/bash
###############################################################################
#Author: Ryan Marken
#Date: 11.17.2018
#Shell script to run data collection.
###############################################################################


python /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/src/update_schedule_previous_day.py > /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/ncaa-bb-dly.txt 2>&1 
python /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/src/update_picks_from_yesterday.py > /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/ncaa-bb-dly.txt 2>&1 
python /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/src/populate_schedule.py > /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/ncaa-bb-dly.txt 2>&1 
python /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/src/insert_picks.py > /home/pegasus/programming/python/CBAPP/NCAA_BASKETBALL_PROGRAM/misc_files/ncaa-bb-dly.txt 2>&1 