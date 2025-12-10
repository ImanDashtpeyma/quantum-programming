# Assignment 03 - Problem Set III - QPROG

**Students:** Jady Pâmella Barbacena da Silva and Navyashree Suryanarayana Rao Prasanna  
**Course:** QPROG - Quantum Programming  
**Date:** December 8, 2025

---

## Question 1: Quantum Fourier Transform (3 points)

### Task 1.2 (1 point): `apply_qft(n, circuit)`
Implements QFT on the first n qubits.

### Task 1.3 (1 point): `apply_iqft(n, circuit)`
Implements Inverse QFT with negative phase shifts.

### Task 1.4 (1 point): Generalized Functions
- `apply_qft_gen(qubits, circuit)` - QFT on arbitrary qubit list
- `apply_iqft_gen(qubits, circuit)` - Inverse QFT on arbitrary qubit list

---

## Question 2: Classical to Quantum (7 points + 2 bonus)

### Task 2.3 (1.5 points): `convert_step_1`
Converts classical gates to quantum using ancilla at |0⟩.
Supports: AND, OR, XOR, NOT, NAND

### Task 2.4 (1.5 points): `convert_step_2`
Applies gates from Step 1 in reverse order.

### Task 2.5 (1.5 points): `convert`
Complete Uf transformation: |x⟩|0⟩|0⟩ → |x⟩|f(x)⟩|0⟩

### Task 2.6 (2.5 points): Controlled Versions
All operations controlled by qubit i:
- `convert_contr_step_1(qc, i)`
- `convert_contr_step_2(qc, i)`
- `convert_contr(qc, i)`

### Task 2.7 (2 BONUS points): Extended Gate Set
OR, XOR, and NAND gates implemented in all methods.

---

## Files

- `question1_qft.ipynb` - Question 1 implementations and tests
- `question2_classical_to_quantum.ipynb` - Question 2 implementations and tests

---

## Implementation Details

### Question 1
- QFT uses Hadamard gates and controlled phase gates
- Phase angles: π/2^k
- SWAP gates to reverse qubit order
- Inverse QFT: reverse order, negative phases

### Question 2
- Converts AND, OR, XOR, NOT, NAND gates
- Uses Toffoli (CCX) and CNOT (CX) gates
- Output preservation through ancilla duplication
- Uncompute cleans up internal qubits only
- Controlled versions use multi-controlled gates