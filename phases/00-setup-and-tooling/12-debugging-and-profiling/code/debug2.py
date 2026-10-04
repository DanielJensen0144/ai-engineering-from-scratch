# debug 2
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

def training_step(model, batch, criterion, optimizer):
    inputs, labels = batch
    outputs = model(inputs)
    loss = criterion(outputs, labels)

    # print(loss.item())
    if loss.item() > 100 or torch.isnan(loss):
        breakpoint()

    loss.backward()
    optimizer.step()

# --- Tiny model ---
model = nn.Sequential(
    nn.Linear(10, 32),
    nn.ReLU(),
    nn.Linear(32, 2),
)

# --- Fake dataset ---
X = torch.randn(64, 10)
y = torch.randint(0, 2, (64,))
loader = DataLoader(TensorDataset(X, y), batch_size=16)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# --- Case 1: normal run (loss should be ~0.7, no breakpoint) ---
for batch in loader:
    training_step(model, batch, criterion, optimizer)

# --- Case 2: trigger breakpoint via huge loss ---
# Scale up so CrossEntropyLoss blows past 100
bad_model = nn.Sequential(nn.Linear(10, 2))
with torch.no_grad():
    bad_model[0].weight.mul_(0)   # zero weights -> uniform logits
    bad_model[0].bias.copy_(torch.tensor([100.0, -100.0]))  # huge logit gap
bad_opt = torch.optim.SGD(bad_model.parameters(), lr=0.01)

batch = next(iter(loader))
training_step(bad_model, batch, criterion, bad_opt)   # hits breakpoint

# --- Case 3: trigger breakpoint via NaN loss ---
with torch.no_grad():
    bad_model[0].bias.copy_(torch.tensor([float('nan'), 0.0]))
training_step(bad_model, batch, criterion, bad_opt)   # hits breakpoint