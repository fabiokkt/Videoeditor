#!/bin/bash
# fila de download do Commons por prioridade (rodar como tarefa de fundo: bash work/pesq/dlq.sh)
cd "$(dirname "$0")"
python3 wmstd.py 1920 night_vision_raid_Iraq:8,3,0,5,1,7 tactical_operations_center_Iraq:7,2,11 Stanley_A_McChrystal:1,101,91,103 Kandahar_Airfield_boardwalk:2,3 >> dl2.log 2>&1
echo FIM >> dl2.log
