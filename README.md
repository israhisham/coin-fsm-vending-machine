# coin-fsm-vending-machine
A simple vending machine simulator built as a finite state machine (FSM) in Python. The machine accepts 0.25 JD and 0.50 JD coins and dispenses a product once 1.00 JD has been reached.

The machine has 5 states, each representing the total amount inserted so far:

Each coin insertion transitions the machine from one state to the next based on the coin value:

        +0.25         +0.25         +0.25         +0.25
   A ----------> B ----------> C ----------> D ----------> E
   |                                                        |
   +--------------------------+0.50 (from A, B, C, or D)----+

E → dispenses product, then resets to B or C on the next coin.

Inserting 0.25 JD moves the state forward by one step (A→B→C→D→E).
Inserting 0.50 JD moves the state forward by two steps (capped at E).
Reaching state E triggers dispense_product().
Inserting a coin while in state E starts a new purchase (acts like a reset to B or C).

Requirements:
None, this project uses only the Python standard library.
