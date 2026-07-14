# coin-fsm-vending-machine
A simple vending machine simulator built as a finite state machine (FSM) in Python. The machine accepts 0.25 JD and 0.50 JD coins and dispenses a product once 1.00 JD has been reached.

The machine has 5 states, each representing the total amount inserted so far:

Each coin insertion transitions the machine from one state to the next based on the coin value:

Inserting 0.25 JD moves the state forward by one step (A→B→C→D→E).
Inserting 0.50 JD moves the state forward by two steps (capped at E).
Reaching state E triggers dispense_product().
Inserting a coin while in state E starts a new purchase (acts like a reset to B or C).

<img width="1920" height="1080" alt="A0" src="https://github.com/user-attachments/assets/ab0878d6-1f32-4521-8449-2f86d74afbfa" />

Requirements:
None, this project uses only the Python standard library.


