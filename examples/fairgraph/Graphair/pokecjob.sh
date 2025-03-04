#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gpus=4
#SBATCH --nodes=1
#SBATCH --job-name=pokec
#SBATCH --time=01:00:00
#SBATCH --output=slurm_output_%A.out
#SBATCH --mem-per-gpu=15GB


module purge
module load 2022
module load Anaconda3/2022.05
module load CUDA/11.8.0

# Activate your environment
source activate dig

srun python -u run_graphair_pokec.py
