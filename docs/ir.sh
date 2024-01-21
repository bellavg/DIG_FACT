#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --job-name=digin
#SBATCH --time=02:45:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=18
#SBATCH --output=slurm_output_%A.out

module purge
module load 2022
module load CUDA/11.8.0
module load Anaconda3/2022.05


conda env update  --file environment.yaml

# Activate your environment
source activate dig
#cd DIG
#pip install 
#pip install pyro-ppl
#pip install torch_geometric
#pip install torch_scatter 
#pip install torch_sparse 
#pip install torch_cluster 
#pip install torch_spline-conv

