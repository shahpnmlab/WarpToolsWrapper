#!/bin/bash

# Specify a job name
#SBATCH -J warp
#SBATCH -A stuart.prj
#SBATCH -p gpu_relion
#SBATCH -o warp-%j.out
#SBATCH -e warp-%j.err
#SBATCH -N 1
#SBATCH --cpus-per-task 1
#SBATCH --gpus 4

echo "------------------------------------------------"
echo "Slurm Job ID: $SLURM_JOB_ID"
echo "Run on host: "`hostname`
echo "Operating system: "`uname -s`
echo "Username: "`whoami`
echo "Started at: "`date`
echo "------------------------------------------------"

bash /Users/ps/data/wip/WarpToolsWrapper/warpTools_20240613_133120.sh

bash /Users/ps/data/wip/WarpToolsWrapper/warpTools_20240613_133125.sh

bash /Users/ps/data/wip/WarpToolsWrapper/warpTools_20240613_133719.sh

bash /Users/ps/data/wip/WarpToolsWrapper/warpTools_20240613_133808.sh

bash /Users/ps/data/wip/WarpToolsWrapper/warpTools_20240613_133830.sh
