#!/bin/bash
###############################################################################
#Author: Ryan Marken
#Date: 11.17.2018
#Shell script to run data collection.
###############################################################################


python ../src/update_schedule_previous_day.py > ncaa-bb-dly.txt 2>&1 
python ../src/update_picks_from_yesterday.py > ncaa-bb-dly.txt 2>&1 
python ../src/populate_schedule.py > ncaa-bb-dly.txt 2>&1 
python ../src/insert_picks.py > ncaa-bb-dly.txt 2>&1 