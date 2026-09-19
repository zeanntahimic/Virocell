# Virocell

Virocell is a personal research-and-learning project that simulates how a virus interacts with a host cell, from the molecular kinetics of replication inside a single cell up to the spread of infection across a population of cells. The project has a deliberate dual purpose: to build hands-on programming skill (numerical simulation, agent-based modeling, eventually stochastic methods) while learning real microbiology, biochemistry, and cell biology by implementing the actual mechanisms rather than reading about them abstractly.

The simulation is grounded in real virology wherever possible rather than invented rules. It starts from the classic TIV (Target–Infected–Virus) model used in within-host viral dynamics research (Nowak & May), and grows in biochemical detail from there: intracellular replication kinetics (transcription, translation, assembly) modeled with real rate laws like mass-action and Michaelis-Menten kinetics, spatial spread across a grid of cells, and eventually stochastic simulation for the low molecule-count regimes where deterministic equations break down.

Why this project exists

Most simulations either sacrifice biological accuracy for simplicity, or sacrifice code clarity for scientific rigor. Virocell is an attempt to hold onto both, built incrementally, one feature at a time, so that every added layer of realism corresponds to something genuinely learned.

Current status

This is an active work in progress, built in public. Development follows a phased roadmap:

Phase 0 — Baseline TIV model (target cells, infected cells, free virus)
Phase 1 — Intracellular replication kinetics
Phase 2 — Spatial, agent-based cell-to-cell spread
Phase 3 — Stochastic simulation (Gillespie SSA) for low-count regimes
Phase 4 — Immune response (stretch goal)

Expect the codebase and this README to evolve as each phase is implemented.

Built with

Python, NumPy, SciPy, Matplotlib, and (later) GillesPy2 for stochastic simulation.