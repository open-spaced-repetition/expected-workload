# Spaced Repetition Workload Estimation

This project estimates the expected workload in a spaced repetition system based on different desired retention rates (DR). The estimation helps understand the trade-off between retention rate and total workload in spaced repetition. The estimation is based on the [FSRS-6](https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-Algorithm#fsrs-6) algorithm.


## Parameters

The estimation considers three types of costs:
- `LEARN_COST`: Cost of initial learning
- `RECALL_COST`: Cost of reviewing remembered cards
- `FORGET_COST`: Cost of relearning forgotten cards

## Estimation Methods

### Monte Carlo

It's just based on the simulator in [fsrs-optimizer](https://github.com/open-spaced-repetition/fsrs-optimizer).

Pros:
- Easy to implement

Cons:
- Not accurate
- Not efficient

### Recursion

The `expected_learn()` function calculates the expected workload using a deterministic approach. Unlike Monte Carlo simulations that use random sampling, this estimation:

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
   - Reaches maximum simulation days (365)
   - Product of probabilities along the path becomes too small (≤ 1e-5)
     - This means the contribution to total workload becomes negligible
     - Each branch's probability is multiplied by its parent's probability
     - When this cumulative probability becomes very small, the branch is terminated

Pros:
- More efficient than Monte Carlo

Cons:
- It tends to underestimate the workload for high desired retention

### Dynamic Programming

It's similar to the recursion method, but it discretizes the memory state space into a grid and calculates the expected workload for each state.

Pros:
- More efficient than Recursion
- More accurate for high desired retention

Cons:
- Hard to implement

For details, please see: [Dynamic Programming‐based Spaced Repetition Workload Estimator · open-spaced-repetition/expected-workload Wiki](https://github.com/open-spaced-repetition/expected-workload/wiki/Dynamic-Programming‐based-Spaced-Repetition-Workload-Estimator)
