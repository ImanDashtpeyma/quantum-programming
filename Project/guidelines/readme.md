# QPROG Project 2
## Dominating Set Using Grover's Algorithm

### Course
Quantum Programming (QPROG)  
Department of Computer and Systems Sciences  
Stockholm University

---

## Project Goal

The goal of this project is to implement a quantum solution for the Dominating Set problem using Grover's algorithm.  
The project consists of designing a verifier circuit for the problem and integrating it with Grover's search to find valid dominating sets.

The implementation follows strictly the project specification and uses only the allowed quantum gates.

---

## Problem Definition

Given:
- An undirected graph G = (V, E)
- An integer k

A **dominating set** S ⊆ V of size k satisfies:
- Every vertex v ∈ V is either in S, or
- There exists a vertex u ∈ S such that {u, v} ∈ E

The objective is to determine whether such a set exists and, if so, find it using Grover's algorithm.

---

## Technologies And Tools

- Python 3
- Qiskit
- Qiskit Aer Simulator
- MCXGate for multi-controlled operations

Only the following gates are used in circuit construction:
- X
- CNOT
- CCNOT
- Multi-controlled NOT (MCX)

---

## Project Structure

project-root/
│
├── implementation/
│ ├── graph.py
│ ├── adjacency.py
│ ├── dominated.py
│ ├── all_dominated.py
│ ├── grover_single.py
│ ├── grover_multiple.py
│
├── experiments/
│ ├── graphs/
│ ├── experiment_single_solution.py
│ ├── experiment_multiple_solutions.py
│ ├── results/
│
├── documentation/
│ └── report.pdf
│
└── README.md

yaml
Copiar código

---

## Step By Step Implementation Plan

### Step 1. Graph Representation

Implement a `Graph` class with:
- Number of vertices `n`
- Adjacency list `adj_list`

Required methods:
- `set_number_vertices(n)`
- `add_edge(u, v)`
- `read_from_file(filename)`
- `print()`

The graph file format:
- First line: number of vertices
- Each subsequent line: one edge `u v`

---

### Step 2. Adjacency Circuit

Implement the function:

Adj(G, circuit, A, B, b)

yaml
Copiar código

Behavior:
- Sets qubit `b` to 1 if and only if `{number(A), number(B)}` is an edge of G

Constraints:
- No auxiliary qubits
- Implemented using only multi-controlled NOT gates
- Two gates per edge, since the graph is undirected

---

### Step 3. Dominated Vertex Circuit

Implement the function:

Dominated(G, circuit, A1, ..., Ak, B, AUX, b)

yaml
Copiar código

Behavior:
- Sets qubit `b` to 1 if vertex `B` is dominated by at least one vertex in `{A1, ..., Ak}`

Checks:
- Equality `B == Ai`
- Adjacency `{B, Ai} ∈ E`

Requirements:
- Use OR logic
- Reuse auxiliary qubits
- AUX must start and end in state |0⟩

---

### Step 4. All Dominated Circuit

Implement the function:

AllDominated(G, circuit, A1, ..., Ak, AUX, b)

yaml
Copiar código

Behavior:
- Sets qubit `b` to 1 if all vertices in the graph are dominated

Logic:
- Sequential AND over all vertices
- Each Dominated check feeds into the global result

Auxiliary register must be reset after each operation.

---

### Step 5. Grover With One Solution

Implement Grover's algorithm assuming a single solution.

Details:
- Input size: k * log2(n) qubits
- Search space size: n^k
- Number of Grover iterations: approximately π/4 * sqrt(n^k)

The oracle uses the AllDominated circuit.

---

### Step 6. Experimental Evaluation With One Solution

Create test graphs with:
- 4, 8, and 16 vertices
- Dominating sets of size 2 and 4
- Exactly one valid solution

For each case:
- Run Grover
- Measure success probability
- Report number of iterations and outcomes

---

### Step 7. Grover With Multiple Solutions

Extend Grover to handle multiple solutions using adaptive iteration:

Procedure:
- Start with 1 Grover iteration
- Double iterations if no solution is found
- Stop at sqrt(n^k)

If no solution is found, report no dominating set.

---

### Step 8. Experimental Evaluation With Multiple Solutions

Repeat experiments using graphs with multiple valid dominating sets.

Measure:
- Detection success
- Iteration growth
- Stability of results

---

## Testing Strategy

For every function:
- Initialize input registers with values up to 4 bits
- Initialize auxiliary registers in |0⟩
- Measure output qubits
- Compare measured values with expected classical results

If simulation is not feasible due to qubit count, this is clearly stated in the report.

---

## Definition Of Done

The project is considered complete when:

- All required functions are implemented
- Only allowed quantum gates are used
- Auxiliary registers start and end in |0⟩
- Unit tests are provided for every function
- Grover works for single and multiple solutions
- Experimental evaluation is complete and reproducible
- Results are clearly reported and analyzed
- Code is clean, modular, and well documented
- The PDF report explains methodology, implementation, and experiments clearly

---

## Expected Outcome

- Correct identification of dominating sets using Grover's algorithm
- Clear demonstration of quadratic speedup compared to brute force
- Fully compliant implementation according to the project specification

---

## Notes

This project strictly follows the official project instructions.  
No additional assumptions or unsupported optimizations are introduced.