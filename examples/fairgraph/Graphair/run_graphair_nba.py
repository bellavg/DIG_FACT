from dig.fairgraph.method.run import run
from dig.fairgraph.dataset import POKEC, NBA
import torch

# Load the dataset
nba = NBA()

# Train and evaluate
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
run_fairgraph = run()
run_fairgraph.run(device,dataset=nba,model='Graphair',epochs=100,test_epochs=100,
            lr=1e-4,weight_decay=1e-5)