# HackathonGame

Game developed in python for teaching Quantum Computing. In this game the players will have access to several levels containing circuits 
that they will have to solve. To solve them, they will have access to several weapons that simulate the different possible output bits.
The objective is to attact with the weapon that corresponds to the most probable output state of our quantum circuit (the monster we are fighting to). In the one-qubit input case we will attack one time, however in the two-qubits case input we will need to attack twice, once for each qubit. 

What is actually happening is that we are measuring our circuit in a certain way with the different weapons, so we will win when our measure is equal to the bit 0 (one-qubit input case), or 00 (two-qubit input case). 

The game is available in a console version and in a more graphical version using pygame. In the graphical version there are still missing
some parts of the visualization of the data as well as the logical behaviour of the 2-q bit circuits.

Category: Teaching Quantum
