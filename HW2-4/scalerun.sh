#PBS -V
#PBS -q fill
#PBS -l nodes=1:ppn=8

cd $PBS_O_WORKDIR

hostname

module unload mpi
module load openmpi/2.1.6
module load scale

scalerte -m -I 8  2_4
