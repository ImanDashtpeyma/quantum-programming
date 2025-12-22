# QPROG Project 2 Submission Checklist
## Dominating Set Using Grover's Algorithm

Use this checklist before creating the final ZIP file.  
All items must be completed for full compliance.

---

## 1. Project Structure

- [ ] ZIP file contains exactly three folders:
  - [ ] documentation/
  - [ ] implementation/
  - [ ] experiments/

- [ ] Folder names are spelled exactly as required.
- [ ] No extra files or folders at the root level.

---

## 2. Graph Implementation

- [ ] `Graph` class implemented.
- [ ] Attributes:
  - [ ] `n` number of vertices.
  - [ ] `adj_list` adjacency list.

- [ ] Methods implemented:
  - [ ] `set_number_vertices(n)`
  - [ ] `add_edge(u, v)`
  - [ ] `read_from_file(filename)`
  - [ ] `print()`

- [ ] Graph files use `.txt` extension.
- [ ] Graph file format is correct.

---

## 3. Adjacency Circuit

- [ ] Function `Adj(G, circuit, A, B, b)` implemented.
- [ ] Correctly detects `{number(A), number(B)} ∈ E`.
- [ ] Graph is treated as undirected.
- [ ] Exactly two multicontrolled NOT gates per edge.
- [ ] No auxiliary qubits used.
- [ ] Only allowed gates are used.

---

## 4. Dominated Vertex Circuit

- [ ] Function `Dominated(G, circuit, A1...Ak, B, AUX, b)` implemented.
- [ ] Checks equality `B == Ai`.
- [ ] Checks adjacency `{B, Ai} ∈ E`.
- [ ] OR logic implemented correctly.
- [ ] Output qubit `b` initialized to |0⟩.
- [ ] Auxiliary register reused correctly.
- [ ] AUX starts and ends in |0⟩.

---

## 5. All Dominated Circuit

- [ ] Function `AllDominated(G, circuit, A1...Ak, AUX, b)` implemented.
- [ ] Verifies all vertices are dominated.
- [ ] AND logic implemented sequentially.
- [ ] Output qubit reflects global domination.
- [ ] AUX reset after each operation.

---

## 6. Oracle Construction

- [ ] Oracle correctly marks valid dominating sets.
- [ ] Oracle uses the `AllDominated` circuit.
- [ ] Phase flip applied correctly.
- [ ] No measurement inside the oracle.

---

## 7. Grover Algorithm Single Solution

- [ ] Grover implementation for one solution completed.
- [ ] Correct number of Grover iterations used.
- [ ] Diffusion operator implemented correctly.
- [ ] Search space size is n^k.
- [ ] Measurement performed only after Grover iterations.

---

## 8. Grover Algorithm Multiple Solutions

- [ ] Adaptive Grover implemented.
- [ ] Iteration count doubles when no solution is found.
- [ ] Maximum iterations capped at sqrt(n^k).
- [ ] Correct handling of multiple valid solutions.
- [ ] Correct termination conditions implemented.

---

## 9. Experimental Evaluation Single Solution

- [ ] Graphs with 4 vertices created.
- [ ] Graphs with 8 vertices created.
- [ ] Graphs with 16 vertices created.
- [ ] Dominating sets of size 2 tested.
- [ ] Dominating sets of size 4 tested.
- [ ] Exactly one solution per test case.
- [ ] Results recorded and reproducible.

---

## 10. Experimental Evaluation Multiple Solutions

- [ ] Graphs with multiple dominating sets created.
- [ ] Experiments executed successfully.
- [ ] Success probability reported.
- [ ] Iteration behavior analyzed.
- [ ] Results stored in experiments/results/.

---

## 11. Testing And Validation

- [ ] Each function tested independently.
- [ ] Inputs use at most 4-bit registers.
- [ ] Auxiliary registers initialized to |0⟩.
- [ ] Output registers measured and verified.
- [ ] Expected classical results documented.
- [ ] Limitations explicitly stated if simulation is infeasible.

---

## 12. Code Quality

- [ ] Code is modular and readable.
- [ ] Functions follow project naming conventions.
- [ ] No unused or dead code.
- [ ] Comments explain logic clearly.
- [ ] No forbidden gates used anywhere.

---

## 13. Report (PDF)

- [ ] Report is in `documentation/report.pdf`.
- [ ] Project goal clearly explained.
- [ ] Dominating Set problem formally defined.
- [ ] Circuit design explained step by step.
- [ ] Grover integration described clearly.
- [ ] Experimental setup documented.
- [ ] Results presented using tables or figures.
- [ ] Analysis and discussion included.
- [ ] Limitations discussed honestly.

---

## 14. Final Verification

- [ ] All required project steps implemented.
- [ ] All constraints respected.
- [ ] ZIP file opens correctly.
- [ ] Project runs on a clean environment.
- [ ] Submission deadline confirmed.

---

## Ready For Submission

- [ ] All checklist items completed.
- [ ] Project ZIP is final and verified.

