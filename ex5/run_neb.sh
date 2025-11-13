for i in {1..1}
do

	#python3 adapt_data.py B_relax final.data

	nreplica=20
	dump_file=results_neb.dump
	mpirun -np ${nreplica} --oversubscribe lmp_mpi -partition ${nreplica}x1 -v dump_file ${dump_file} -v num_replicas ${nreplica} -in in.neb >> log.neb 


	rm screen*
	rm log.lammps*
done

tail -1 log.neb >> log2.neb
python3 parse_energy_barriers.py
python3 neb_final.py -o neb_movie -r results_neb.dump.*
rm log*
#rm results_neb*



