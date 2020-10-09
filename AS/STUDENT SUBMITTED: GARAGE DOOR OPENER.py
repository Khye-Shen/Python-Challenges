transitions = {("button_clicked", "OPEN"): "CLOSING",
        ("button_clicked", "CLOSED"): "OPENING",
        ("button_clicked", "OPENING"): "STOPPED_WHILE_OPENING",
        ("button_clicked", "CLOSING"): "STOPPED_WHILE_CLOSING",
        ("button_clicked", "STOPPED_WHILE_OPENING"): "CLOSING",
        ("button_clicked", "STOPPED_WHILE_CLOSING"): "OPENING",
        ("cycle_complete", "OPENING"): "OPEN",
        ("cycle_complete", "CLOSING"): "CLOSED",
        ("cycle_complete", "EMERGENCY_OPENING"): "BLOCKED_OPEN",
        ("block_detected", "CLOSING"): "EMERGENCY_OPENING",
        ("block_detected", "OPENING"): "EMERGENCY_OPENING",
        ("block_detected", "OPEN"): "BLOCKED_OPEN",
        ("block_detected", "CLOSED"): "BLOCKED_CLOSED",
        ("block_detected", "STOPPED_WHILE_CLOSING"): "BLOCKED_STOPPED_CLOSING",
        ("block_detected", "STOPPED_WHILE_OPENING"): "BLOCKED_STOPPED_OPENING",
        ("block_cleared", "BLOCKED_OPEN"): "OPEN",
        ("block_cleared", "BLOCKED_CLOSED"): "CLOSED",
        ("block_cleared", "EMERGENCY_OPENING"): "OPENING",
        ("block_cleared", "BLOCKED_STOPPED_CLOSING"): "STOPPED_WHILE_CLOSING",
        ("block_cleared", "BLOCKED_STOPPED_OPENING"): "STOPPED_WHILE_OPENING"}

# Inputs
input1 = '''
button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete
'''

input2 = '''
button_clicked
cycle_complete
button_clicked
block_detected
button_clicked
cycle_complete
button_clicked
block_cleared
button_clicked
cycle_complete
'''


state = "CLOSED"
for command in input1.split():
    if (command, state) in transitions:
        state = transitions[(command,state)]
    out = ":> %s\nDoor: %s"%(command,state)
    print(out)
print("\n")


for command in input2.split():
    if (command,state) in transitions:
        state = transitions[(command,state)]
    out = ":> %s\nDoor: %s"%(command,state)
    print(out)