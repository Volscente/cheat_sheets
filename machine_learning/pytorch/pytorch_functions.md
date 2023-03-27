# Save & Load Models
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