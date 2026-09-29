# Dominating Set Using Grover's Algorithm

**Course:** QPROG - Quantum Programming  
**Institution:** Stockholm University, Department of Computer and Systems Sciences  
**Students:** Jady Pâmella Barbacena da Silva & Iman Dashtpeyma  
**Group:** Project-08  
**Date:** December 2025

---

## Project Overview

This project implements a quantum solution for the **Dominating Set problem** using **Grover's algorithm**. Given a graph G=(V,E) and an integer k, we find a dominating set of size k using quantum search with quadratic speedup over classical brute-force.

---

## Project Structure

```
/Project/
├── project.ipynb          # Main implementation (ALL CODE HERE)
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── documentation/
│   └── report.md          # Complete project report
├── experiments/
│   ├── graphs/            # Test graph files (.txt)
│   └── results/           # Experimental results
└── guidelines/            # Project specifications
```

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Notebook
```bash
jupyter notebook project.ipynb
```
Or open in VS Code and run all cells.

### 3. Verify Results
All test cells should show ✓ for passed tests.

---

## Implementation Checklist (100%)

| Section | Description | Status |
|---------|-------------|--------|
| 1.1 (12.5%) | Graph class with adj_list | ✓ |
| 1.2 (12.5%) | Adjacency circuit (MCX only, no aux) | ✓ |
| 1.3 (12.5%) | Dominated vertex circuit (OR logic) | ✓ |
| 1.4 (12.5%) | AllDominated circuit (AND logic) | ✓ |
| 1.5 (12.5%) | Grover with one solution | ✓ |
| 1.6 (12.5%) | Experimental evaluation (1 solution) | ✓ |
| 1.7 (12.5%) | Grover with multiple solutions | ✓ |
| 1.8 (12.5%) | Experimental evaluation (multiple) | ✓ |

---

## Key Results

| Graph | Vertices | k | Qubits | Success Rate | Status |
|-------|----------|---|--------|--------------|--------|
| Star  | 4 | 2 | 21 | 33.2% | ✓ Working |
| Two-Stars | 8 | 2 | 30 | N/A | ⚠ Too large |
| Grid  | 16 | 2 | 43 | N/A | Theoretical |

---

## IBM Quantum Cloud Testing

### Why IBM Cloud?
Our 8-vertex and 16-vertex circuits exceed classical simulation limits (>25 qubits). IBM Quantum provides access to real quantum hardware with 100+ qubits.

### How to Test on IBM Quantum

1. **Create IBM Quantum Account**
   - Go to https://quantum.ibm.com/
   - Sign up for free

2. **Get API Token**
   - Go to Account Settings
   - Copy your API token

3. **Install IBM Runtime**
   ```bash
   pip install qiskit-ibm-runtime
   ```

4. **Modify the code to use IBM backend:**
   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   
   # Save your credentials (only once)
   QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_TOKEN")
   
   # Connect to IBM Quantum
   service = QiskitRuntimeService()
   backend = service.least_busy(operational=True, simulator=False)
   
   # Run on real hardware
   job = backend.run(transpile(circuit, backend), shots=1024)
   result = job.result()
   ```

### IBM Quantum Limitations
- Free tier: limited queue time
- Error rates: ~0.1-1% per gate
- Connectivity: not all qubits connected
- Our 30-qubit circuit may need optimization for real hardware

---

## Potential Improvements

### 1. Qubit Optimization
- Use qubit reuse (measure and reset)
- Implement more efficient ancilla management

### 2. Error Mitigation
- Add error mitigation techniques for NISQ devices
- Use zero-noise extrapolation (ZNE)

### 3. Alternative Approaches
- QAOA (Quantum Approximate Optimization Algorithm)
- Variational Quantum Eigensolver (VQE)

### 4. Performance Enhancements
- Pre-computation of optimal iterations
- Parallel classical verification

---

## Technical Specifications

### Allowed Gates
As specified in the project requirements:
- X (NOT)
- CNOT (Controlled-NOT)
- CCNOT (Toffoli)
- MCX (Multi-controlled NOT)

### Auxiliary Qubit Management
All auxiliary registers:
- Start in state |0⟩
- Reset to |0⟩ after each operation
- Reused across multiple computations

---

## Files Description

| File | Description |
|------|-------------|
| `project.ipynb` | Main notebook with all implementations |
| `documentation/report.md` | Complete project report with test evidence |
| `experiments/graphs/*.txt` | Graph definition files |
| `experiments/results/*.txt` | Experimental results |
| `requirements.txt` | Python package dependencies |

---

## References

1. Grover, L. K. (1996). A fast quantum mechanical algorithm for database search.
2. Nielsen & Chuang (2010). Quantum Computation and Quantum Information.
3. Qiskit Documentation: https://qiskit.org/

---

## Authors

- **Jady Pâmella Barbacena da Silva**
- **Iman Dashtpeyma**

Stockholm University, December 2025

# Quantum Programming - QPROG

This repository contains implementations and exercises from the Quantum Programming (QPROG) course at Stockholm University.

## Repository Structure

### Lecture03
Code examples from lectures on Bell States and GHZ (Greenberger-Horne-Zeilinger) states.

**Included notebooks:**
- Bell State with BasicSimulator and Aer
- Bell State with IBM Quantum
- Generalized GHZ with Aer and IBM Quantum

### Lecture05
Implementation examples of Grover's quantum search algorithm.

**Python scripts:**
- Multiple controls
- Oracle circuits
- Diffusion operator
- Quantum search with single and multiple solutions

### Assignment02
Implementation of the Bernstein-Vazirani algorithm using Qiskit. The algorithm allows discovering a hidden binary string in a single quantum query.

**Main files:**
- `bernstein_vazirani.ipynb` - Complete protocol implementation
- `requirements.txt` - Project dependencies

### Assignment03
Implementation of Quantum Fourier Transform (QFT) and classical-to-quantum circuit conversion.

**Main files:**
- `question1_qft.ipynb` - Quantum Fourier Transform implementation
- `question2_classical_to_quantum.ipynb` - Conversion of classical boolean circuits to reversible quantum circuits
- `resources/` - Support files and templates

## Technologies Used

- **Qiskit 2.2.3** - Main quantum computing framework
- **Qiskit Aer 0.17.2** - Quantum simulators
- **Python 3.x** - Programming language
- **Jupyter Notebooks** - Interactive development environment
- **NumPy** - Mathematical operations
- **Matplotlib** - Circuit and result visualization

## How to Use

1. Clone the repository:
```bash
git clone https://github.com/jadypamella/quantum-programming.git
cd quantum-programming
```

2. Install dependencies (example for Assignment02):
```bash
pip install -r Assignment02/requirements.txt
```

3. Open Jupyter notebooks:
```bash
jupyter notebook
```

## Instructor

- **Professor Mateus de Oliveira Oliveira** - Stockholm University

## Authors

- **Jady Pâmella Barbacena da Silva**
- **Erik Lind Gou-Said** (Assignment02)
- **Navyashree Suryanarayana Rao Prasanna** (Assignment03)

## Course

**Institution:** Stockholm University  
**Period:** H2025  
**Course:** Quantum Programming (QPROG)
