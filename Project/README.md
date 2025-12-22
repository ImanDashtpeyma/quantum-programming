# Dominating Set Quantum Algorithm - Project Status

**Group:** Project-08  
**Students:** Jady Pâmella Barbacena da Silva & Iman Dashtpeyma  
**Last Updated:** December 22, 2025

---

## 📁 Project Structure

```
/Project/
├── project.ipynb          # Main implementation notebook (ALL CODE HERE)
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── documentation/
│   └── report.md         # Complete project report (PDF format as markdown)
├── resources/
│   └── (graph files)     # Test graph definitions
├── guidelines/
│   └── (reference)       # Project guidelines and specifications
└── experiments/
    └── (results)         # Experimental results and outputs
```

---

## ✅ What Has Been Completed

### Core Implementation
- ✅ **Graph class** with correct `adj_list` format (list of sublists, not dictionary)
- ✅ **Adjacency circuit (Adj)** - Uses only MCX gates, 2 per edge, no auxiliary qubits
- ✅ **Equality circuit** - Checks if two vertices are equal
- ✅ **Dominated circuit** - Fixed OR logic bug (was inverted due to extra X gate)
- ✅ **AllDominated circuit** - Verifies all vertices are dominated
- ✅ **AllDistinct circuit** - NEW! Ensures k vertices are distinct (no duplicates)
- ✅ **Oracle** - Fixed CCZ bug, now correctly uses CZ for phase flip
- ✅ **Grover's algorithm** - Both single and multiple solution variants
- ✅ **Diffusion operator** - Amplitude amplification

### Testing & Validation
- ✅ All unit tests passing (Equality, Adj, Dominated, AllDominated)
- ✅ 4-vertex graph experiments working (33.2% success rate)
- ✅ Classical verification functions
- ✅ Single-solution test graph (8-vertex two-stars)
- ✅ 16-vertex theoretical analysis

### Documentation
- ✅ Complete project report in `documentation/report.md`
- ✅ All code documented with docstrings
- ✅ Requirements.txt for easy setup

---

## 🔧 Known Issues & Limitations

### Scalability
- ⚠️ **8-vertex circuits require 30 qubits** - Too large for classical simulation (limit ~25-27 qubits)
- ⚠️ **16-vertex requires 43+ qubits** - Only theoretical analysis provided
- This is a **known limitation** documented in the report

### Why So Many Qubits?
The qubit count is high because:
1. **Input qubits:** k × ⌈log₂(n)⌉ for encoding k vertices
2. **AllDominated AUX:** O(n) qubits to store domination results for each vertex
3. **AllDistinct AUX:** O(k²) qubits for pairwise distinctness checks
4. **Intermediate computation:** Various auxiliary qubits for equality, adjacency

This is **correct** for the implementation approach but limits practical simulation.

---

## 🎯 What Needs Review

### Priority 1: Verify Core Logic
- [ ] **Check Dominated circuit** - Lines ~379-475 in project.ipynb
  - Verify OR logic is correct (should NOT invert result)
  - Check auxiliary qubit uncomputation
- [ ] **Check Oracle** - Lines ~902-956 in project.ipynb
  - Verify phase flip logic with CZ gate
  - Confirm both AllDominated AND AllDistinct are checked

### Priority 2: Review Experimental Results
- [ ] **Run project.ipynb from top to bottom**
  - All cells should execute without errors
  - Check test results match expected behavior
- [ ] **4-vertex experiment** - Cell around line 1752
  - Success rate should be 25-35%
  - Valid solutions should appear in top results

### Priority 3: Documentation
- [ ] **Read documentation/report.md**
  - Check if all sections are clear
  - Verify experimental results match actual output
  - Suggest improvements if needed

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Open project.ipynb in Jupyter/VS Code**

3. **Run all cells in order:**
   - Imports and setup
   - Graph class and helper functions
   - Circuit implementations (Adj, Equality, Dominated, etc.)
   - Oracle and Grover's algorithm
   - Experimental evaluation

4. **Check outputs:**
   - All test cells should show "✓" for passed tests
   - Experiment results should show valid dominating sets

---

## 📝 What Still Needs to Be Done

### Optional Improvements (Low Priority)
- [ ] Try to optimize qubit usage (if time permits)
- [ ] Add more test cases for edge cases
- [ ] Compare with classical brute-force timing

### Submission Checklist
- [x] Main implementation complete
- [x] All required circuits implemented
- [x] adj_list in correct format
- [x] Adj circuit with only MCX, no aux qubits
- [x] OR logic fixed (not XOR)
- [x] AllDistinct for proper subsets
- [x] 16-vertex theoretical analysis
- [x] PDF report created
- [ ] **Final review by both team members**
- [ ] **Test on fresh Python environment**
- [ ] **Submit to course platform**

---

## 🐛 Major Bugs Fixed

1. **Dominated circuit OR logic** - Removed extra `X(b)` gate that inverted result
2. **Oracle CCZ error** - Changed from `ccz(output, distinct, output)` to `cz(output, distinct)`
3. **Graph.adj_list format** - Changed from dict to list
4. **Missing AllDistinct** - Added circuit to ensure distinct vertices

---

## 📊 Key Results

| Graph Type | Vertices | k | Qubits | Success Rate | Status |
|------------|----------|---|--------|--------------|--------|
| Star graph | 4 | 2 | 21 | 33.2% | ✓ Working |
| Two-stars | 8 | 2 | 30 | N/A | Too large |
| Grid | 16 | 2 | 43 | N/A | Theoretical |

**Conclusion:** Algorithm works correctly on small graphs. Larger graphs exceed classical simulation capabilities, which is expected and documented.

---

## 💬 Questions for Iman

1. Have you reviewed the main implementation in `project.ipynb`?
2. Do the experimental results make sense to you?
3. Any suggestions for improving the report?
4. Should we add anything else before submission?

