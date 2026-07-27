import sys, os, datetime

state_arg = sys.argv[1].lower() if len(sys.argv) > 1 else 'chase'
actor = sys.argv[2] if len(sys.argv) > 2 else 'Visitor'

valid_states = ['idle', 'patrol', 'alert', 'chase', 'attack', 'search']

matched_state = 'chase'
for s in valid_states:
    if s in state_arg:
        matched_state = s
        break

state_upper = matched_state.upper()
timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

diagrams = {
    'patrol': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: 🔥 [PATROL] 🔥
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [>>> PATROL <<<] --(Player Spotted)--> [ALERT] --------(Target Locked)-------> [CHASE]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [SEARCH] <------(Damage Taken)------- [ATTACK]
=======================================================================================""",

    'alert': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: ⚠️ [ALERT] ⚠️
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [PATROL] -------(Player Spotted)-----> [>>> ALERT <<<] -(Target Locked)-------> [CHASE]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [SEARCH] <------(Damage Taken)------- [ATTACK]
=======================================================================================""",

    'chase': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: ⚡ [CHASE] ⚡
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [PATROL] -------(Player Spotted)------> [ALERT] --------(Target Locked)------> [>>> CHASE <<<]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [SEARCH] <------(Damage Taken)------- [ATTACK]
=======================================================================================""",

    'attack': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: 💥 [ATTACK] 💥
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [PATROL] -------(Player Spotted)------> [ALERT] --------(Target Locked)-------> [CHASE]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [SEARCH] <------(Damage Taken)------- [>>> ATTACK <<<]
=======================================================================================""",

    'search': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: 🔍 [SEARCH] 🔍
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [PATROL] -------(Player Spotted)------> [ALERT] --------(Target Locked)-------> [CHASE]
    ^                                                                            |
    |                                                                            v
 [IDLE] <-------(Target Lost)----------- [>>> SEARCH <<<] <-(Damage Taken)---- [ATTACK]
=======================================================================================""",

    'idle': f"""========================================================================================
[AI CONTROLLER]: SENTINEL_FSM_v2.4 // ACTIVE STATE: 💤 [IDLE] 💤
[LAST TRIGGER]: Handled command by @{actor} at {timestamp}
========================================================================================
 [PATROL] -------(Player Spotted)------> [ALERT] --------(Target Locked)-------> [CHASE]
    ^                                                                            |
    |                                                                            v
 [>>> IDLE <<<] <-(Target Lost)--------- [SEARCH] <------(Damage Taken)------- [ATTACK]
======================================================================================="""
}

readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

new_diagram = diagrams[matched_state]

import re
pattern = re.compile(r'```gcode\n.*?\n```', re.DOTALL)
if pattern.search(content):
    updated_content = pattern.sub(f'```gcode\n{new_diagram}\n```', content)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Successfully updated FSM state to {matched_state}")
else:
    print("Could not find gcode block in README.md")
