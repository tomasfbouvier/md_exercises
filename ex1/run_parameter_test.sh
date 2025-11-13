#!/bin/bash

NP=2
INPUT="in.script"

# --- Baseline values ---
BASE_dt=0.001
BASE_tau_T=0.1
BASE_N=2
BASE_T=300

for dt in 0.0001 0.0005 0.001 0.003 0.01; do
	mpirun -np $NP lmp_mpi -in "$INPUT" -v dt "$dt" -v tau_T "$BASE_tau_T" -v N "$BASE_N" -v temp "$BASE_T"
done

for tau_T in 0.01 0.1 1.0; do
  mpirun -np $NP lmp_mpi -in "$INPUT" -v dt "$BASE_dt" -v tau_T "$tau_T" -v N "$BASE_N" -v temp "$BASE_T"
done

for N in 2 3 4 5 6 8; do
  mpirun -np $NP lmp_mpi -in "$INPUT" -v dt "$BASE_dt" -v tau_T "$BASE_tau_T" -v N "$N" -v temp "$BASE_T"
done

echo "All single-variable scans completed."

