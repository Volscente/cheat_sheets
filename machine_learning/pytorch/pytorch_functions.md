# Save & Load Models
## Theory
### What is a `state_dict`?
In PyTorch, the learnable parameters (i.e. weights and biases) of an `torch.nn.Module` model are 
contained in the model’s parameters (accessed with `model.parameters()`). 
A state_dict is simply a Python dictionary object that maps each layer to its parameter tensor. 
Note that only layers with learnable parameters (convolutional layers, linear layers, etc.) 
and registered buffers (batchnorm’s running_mean) have entries in the model’s state_dict. 
Optimizer objects (`torch.optim`) also have a state_dict, which contains information about the optimizer’s state, 
as well as the hyperparameters used.

## Entire Model
``` python
# Print model's state_dict
print("Model's state_dict:")

# Fetch model's weights
for param_tensor in model.state_dict():
    
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())
    
# Save the model
torch.save(model.state_dict(), './<model_file_path>.pt')

# Load model
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load('./<model_file_path>.pt'))
model.eval()
```