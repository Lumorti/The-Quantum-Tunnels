# The Quantum Tunnels

A dungeon crawler designed for a quantum computer as a series of 17000 quantum gates.

But don't worry, you can play along at home using a simulator!

### Features

 - 16 different possible encounters (some friendly, some not)
 - 7 different items with unique effects
 - multiple endings: some good, some bad, one true
 - rock/paper/scissors style combat system (but predictable if you take notes)
 - ASCII art, can be played in just a terminal
 - quantum puns and weird characters

### How It Works

 - the game is represented by a 22-qubit quantum state
 - each turn you can change the first 3 qubits to choose your action (handled by "run.py")
 - the state is then put through the quantum circuit (given by "game.qasm") to produce the next state
 - each possible measured state has a corresponding ASCII output (stored in "outputs.json")

![Pauli the Excluder](https://github.com/lumorti/The-Quantum-Tunnels/blob/master/images/pauli.png?raw=true)

### Dependencies

Requires Python and [Qiskit](https://qiskit.org/), 

Qiskit can be installed easily using pip:
```bash
pip3 install qiskit
```

### Usage 

Download the latest release [here](https://github.com/Lumorti/The-Quantum-Tunnels/releases/), or alternatively clone this repository.

Then run "run.py" as you would a normal Python script, e.g. on Linux:
```bash
python3 run.py
```

### Achievements

You'll have to keep track of these yourself. Ranked in order of difficulty. 

Bonus points if you speedrun getting all of these.

 - [EASY] die by eating too much
 - [EASY] die by tunnelling too far
 - [EASY] die by swapping health with a corridor
 - [EASY] die by breaking the game
 - [EASY] die by ignoring the bartender's warnings
 - [MEDIUM] find every different friendly event (over multiple runs)
 - [MEDIUM] complete a run having full health at the end
 - [MEDIUM] complete a run having no item at the end
 - [MEDIUM] loop back to the start
 - [MEDIUM] defeat every different enemy (over multiple runs)
 - [HARD] complete a run without ever taking damage
 - [HARD] defeat every different enemy (in a single run)
 - [HARD] return the bartender's missing chain
 - [HARD] reach the true end
 - [HARD] complete a run with each item (over multiple runs)

### More Screenshots

![The Unitary Operator](https://github.com/lumorti/The-Quantum-Tunnels/blob/master/images/unit.png?raw=true)

![The Infinite Potential Well](https://github.com/lumorti/The-Quantum-Tunnels/blob/master/images/well.png?raw=true)

![The Entangler](https://github.com/lumorti/The-Quantum-Tunnels/blob/master/images/entang.png?raw=true)
