#!/bin/bash
# Run LAMMPS while varying one variable at a time (no nested loops)

NP=2
INPUT="in.parameter_test"

for temp in 200 225 250 275 300 325 350 375 400; do
  mpirun -np $NP lmp_mpi -in "$INPUT" -v dt 1e-3 -v tau_T 0.1 -v N 6 -v temp $temp
done

echo "All single-variable scans completed."

