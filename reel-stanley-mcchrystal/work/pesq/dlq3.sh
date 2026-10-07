#!/bin/bash
cd "$(dirname "$0")"
python3 wmstd.py 1920 night_vision_raid_Iraq:7,12,13,14 >> dl4.log 2>&1
python3 wmstd.py 1280 tactical_operations_center_Iraq:2 night_vision_raid_Iraq:5 >> dl4.log 2>&1
echo FIM >> dl4.log
