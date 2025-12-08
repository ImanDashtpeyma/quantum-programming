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