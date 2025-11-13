#!/bin/bash

NP=4
INPUT="in.script"

for temp in {200..400..10}
do
  mpirun -np $NP lmp_mpi -in "$INPUT" -v dt 1e-3 -v tau_T 0.1 -v N 6 -v temp $temp
done
