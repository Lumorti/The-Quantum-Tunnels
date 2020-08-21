#!/usr/bin/python3

# Load the main quantum circuit representing game logic (constant)
import qiskit # pip3 install qiskit
gameCircuit = qiskit.QuantumCircuit.from_qasm_file("game.qasm")

# Load the mapping of states to outputs (constant)
import json, gzip
outputData = json.loads(gzip.GzipFile("outputs.json.gz", 'r').read().decode("utf-8"))

# Start in the default state 
state = "0000000000000010011011"

# Game loop
while True:

    # Display the state
    try:
        print(outputData[state])
    except:
        print(outputData["error"])

    # Get the user's input
    classicalInput = input("              Command (try \"help\"): ")

    # Generate circuit combining user input and prev game state
    inputCircuit = qiskit.QuantumCircuit(qiskit.QuantumRegister(3, "inpt"), qiskit.QuantumRegister(2, "plhp"), qiskit.QuantumRegister(2, "enhp"), qiskit.QuantumRegister(4, "evnt"), qiskit.QuantumRegister(3, "item"), qiskit.QuantumRegister(8, "ancl"), qiskit.ClassicalRegister(22, "cout"))
    inputState = state[:-3] + {"h":"001","m":"011","a":"100","b":"101","f":"110","i":"111"}[classicalInput[0]]
    for i, char in enumerate(inputState[::-1]):
        if char == "1": inputCircuit.x(i)

    # Combine and run the circuit (one shot)
    state = list(qiskit.execute(inputCircuit + gameCircuit, qiskit.Aer.get_backend('qasm_simulator'), shots=1, backend_options={"method": "matrix_product_state"}).result().get_counts().keys())[0][0:22]

