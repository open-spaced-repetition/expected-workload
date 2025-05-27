# Spaced Repetition Workload Simulation

This project simulates the expected workload in a spaced repetition system based on different desired retention rates (DR). The simulation helps understand the trade-off between retention rate and total workload in spaced repetition. The simulator is based on the [FSRS-6](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm#fsrs-6) algorithm.

## Workload Estimation

### Cost Model
The simulation considers three types of costs:
- `LEARN_COST`: Cost of initial learning
- `RECALL_COST`: Cost of reviewing remembered cards
- `FORGET_COST`: Cost of relearning forgotten cards

### Workload Calculation Process
The `expected_learn()` function calculates the expected workload using a deterministic approach. Unlike Monte Carlo simulations that use random sampling, this simulation:

1. **Deterministic Calculation**
   - Uses expected values instead of random outcomes
   - Calculates exact probabilities for each possible state
   - Produces identical results for the same input parameters
   - More efficient than running multiple random simulations

2. **Recursive Expectation**
   For each review state:
   - Calculates exact probability of successful recall
   - If successful (probability = p):
     - Applies recall cost weighted by p
     - Updates stability and difficulty
     - Schedules next review
   - If failed (probability = 1-p):
     - Applies forget cost weighted by (1-p)
     - Updates stability and difficulty
     - Schedules next review

3. **Termination Conditions**
   - Reaches maximum simulation days (1000)
   - Product of probabilities along the path becomes too small (≤ 1e-6)
     - This means the contribution to total workload becomes negligible
     - Each branch's probability is multiplied by its parent's probability
     - When this cumulative probability becomes very small, the branch is terminated

### Visualization
The simulation generates two plots:
1. Accumulated workload over time for different desired retention
2. Total workload vs. desired retention

This helps visualize:
- How workload accumulates over time
- The relationship between desired retention and total effort required
- Optimal desired retention for balancing workload and learning effectiveness

## Usage

The simulation runs with a range of desired retention (DR) from 0.7 to 0.99, showing how different retention goals affect the total workload required.