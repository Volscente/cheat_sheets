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

## Endpoints
### Definition
They are defined in the `YAML` file and acts as a proxy between the service provider and the user.

### Parameters
- **endpoint_type** - They are either `llm/v1/completions`, `llm/v1/embeddings` and `llm/v1/chat`
- **model** - It has a `provider`, `name` and `config` ([here](https://mlflow.org/docs/latest/llms/deployments/index.html#provider-specific-configuration-parameters) 
is a list of each model specific configurations required)
- **renewal_period** - The time unit of the rate limit, one of [second|minute|hour|day|month|year]
- **calls* - The number of calls this endpoint will accept within the specified time unit

### Example
```yaml
endpoints:
  - name: completions
    endpoint_type: llm/v1/chat
    model:
      provider: openai
      name: gpt-3.5-turbo
      config:
        openai_api_key: $OPENAI_API_KEY
    limit:
      renewal_period: minute
      calls: 10
```

# Evaluation
## Example
```python
import mlflow
import openai
import os
import pandas as pd
from getpass import getpass

eval_data = pd.DataFrame(
    {
        "inputs": [
            "What is MLflow?",
            "What is Spark?",
        ],
        "ground_truth": [
            "MLflow is an open-source platform for managing the end-to-end machine learning (ML) "
            "lifecycle. It was developed by Databricks, a company that specializes in big data and "
            "machine learning solutions. MLflow is designed to address the challenges that data "
            "scientists and machine learning engineers face when developing, training, and deploying "
            "machine learning models.",
            "Apache Spark is an open-source, distributed computing system designed for big data "
            "processing and analytics. It was developed in response to limitations of the Hadoop "
            "MapReduce computing model, offering improvements in speed and ease of use. Spark "
            "provides libraries for various tasks such as data ingestion, processing, and analysis "
            "through its components like Spark SQL for structured data, Spark Streaming for "
            "real-time data processing, and MLlib for machine learning tasks",
        ],
    }
)

with mlflow.start_run() as run:
    system_prompt = "Answer the following question in two sentences"
    # Wrap "gpt-4" as an MLflow model.
    logged_model_info = mlflow.openai.log_model(
        model="gpt-4",
        task=openai.chat.completions,
        artifact_path="model",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "{question}"},
        ],
    )

    # Use predefined question-answering metrics to evaluate our model.
    results = mlflow.evaluate(
        logged_model_info.model_uri,
        eval_data,
        targets="ground_truth",
        model_type="question-answering",
    )
    print(f"See aggregated evaluation results below: \n{results.metrics}")

    # Evaluation result for each data record is available in `results.tables`.
    eval_table = results.tables["eval_results_table"]
    print(f"See evaluation table below: \n{eval_table}")
```

## Metrics
### Types
- **SaaS Model Metrics** - They use another SaaS Model (e.g., OpenAI) to provide an evaluation of one specific prompt
- **Function-based Row Metrics** - They use specific metrics like ROUGE

### SaaS Model Metrics
It is also possible to use another LLM as a `extra_metrics` that acts like a Judge. 
Check the list of available judges [here](https://mlflow.org/docs/latest/llms/llm-evaluate/index.html#metrics-with-llm-as-the-judge).

### Function-based Row Metrics
MLflow LLM evaluation includes **default** collections of metrics for pre-selected tasks, e.g, “question-answering”.
They are then passed as an argument to the `mlflow.evaluate` function.
```python
results = mlflow.evaluate(
    model,
    eval_data,
    targets="ground_truth",
    model_type="question-answering",
)
```
It is also possible to have custom metrics in addition to the default ones.
```python
results = mlflow.evaluate(
    model,
    eval_data,
    targets="ground_truth",
    model_type="question-answering",
    extra_metrics=[mlflow.metrics.latency()],
)
```
Or exclude the default metrics entirely by not passing the `model_type` argument.
```python
results = mlflow.evaluate(
    model,
    eval_data,
    targets="ground_truth",
    extra_metrics=[mlflow.metrics.toxicity(), mlflow.metrics.latency()],
)
```



