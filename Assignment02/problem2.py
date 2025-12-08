from qiskit import QuantumCircuit

# Task 1
def inner_product(circuit, a):
    pass

# Task 1 Test
def test_circuit_1():
    a = "01101"
    n=len(a)
    circuit = QuantumCircuit(n+1, 0)
    inner_product(circuit, a)
    print(circuit)


# Task 2
def hadamards(circuit):
    pass

# Task 2 Test
def test_circuit_2():
    circuit = QuantumCircuit(5, 0)
    hadamards(circuit)
    print(circuit)

#Task 3
def bernstein_vazirani(a):
    pass

# Task 3 Test
def test_circuit_3():
    a = "01101"
    circuit = bernstein_vazirani(a)
    print(circuit)
