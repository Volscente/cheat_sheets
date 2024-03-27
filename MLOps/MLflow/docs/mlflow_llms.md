# MLflow Deployments Server
## Definition
It was previously known as MLflow AI Gateway, and 
it simplifies interactions with multiple LLM providers.

Through the usage of `YAML` files, it streamlines the interactions with LLM providers.

## Configuration
### 1. Installation
```bash
pip install 'mlflow[genai]'
```

### 2. Setup API Key
```bash
# Take as example OpenAI
export OPENAI_API_KEY=your_api_key_here
```

### 3. Create Configuration File
It sets up different routes for different services offered by the LLM provider (e.g., OpenAI).

This is an example:
```yaml
endpoints:
- name: completions
  endpoint_type: llm/v1/completions
  model:
      provider: openai
      name: gpt-3.5-turbo
      config:
          openai_api_key: $OPENAI_API_KEY

- name: chat
  endpoint_type: llm/v1/chat
  model:
      provider: openai
      name: gpt-4
      config:
          openai_api_key: $OPENAI_API_KEY

- name: chat_3.5
  endpoint_type: llm/v1/chat
  model:
      provider: openai
      name: gpt-3.5-turbo
      config:
          openai_api_key: $OPENAI_API_KEY

- name: embeddings
  endpoint_type: llm/v1/embeddings
  model:
      provider: openai
      name: text-embedding-ada-002
      config:
          openai_api_key: $OPENAI_API_KEY
```

It is also possible to have different endpoints to different model versions.
```yaml
endpoints:
  - name: completions
    endpoint_type: llm/v1/completions
    model:
      provider: openai
      name: gpt-3.5-turbo
      config:
        openai_api_key: $OPENAI_API_KEY
  - name: completions-gpt4
    endpoint_type: llm/v1/completions
    model:
      provider: openai
      name: gpt-4
      config:
        openai_api_key: $OPENAI_API_KEY
```

### 4. Start Server
```bash
mlflow deployments start-server --config-path <path_config.yaml>

mlflow deployments start-server --config-path {path_config.yaml} --port {port} --host {host} --workers {worker count}
```

Usually it starts at `http://localhost:5000` and it is possible to check its
documentation by navigating to that URL (`http://localhost:5000/docs`).

### 5. Send Request
It is possible to call a specific endpoint from the Deployment Server, one of the
endpoints defined in the `YAML` file.

```python
from mlflow.deployments import get_deploy_client

client = get_deploy_client("http://localhost:5000")
name = "completions"
data = dict(
    prompt="Name three potions or spells in harry potter that sound like an insult. Only show the names.",
    n=2,
    temperature=0.2,
    max_tokens=1000,
)

response = client.predict(endpoint=name, inputs=data)
print(response)
```