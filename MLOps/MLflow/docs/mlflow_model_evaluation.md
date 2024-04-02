# General
## Definition
MLflow addresses these challenges head-on, offering a suite of automated tools that streamline the evaluation process, 
saving time and enhancing accuracy, helping you to have confidence that the solution that you’ve spent so much time
working on will meet the needs of the problem you’re trying to solve.

# LLMs Evaluation
## RAG Evaluation
Create a RAG system that answers questions based on the MLflow documentation.

Define some evaluation examples.
```python
from mlflow.metrics.genai import EvaluationExample

faithfulness_examples = [
    EvaluationExample(
        input="How do I disable MLflow autologging?",
        output="mlflow.autolog(disable=True) will disable autologging for all functions. In Databricks, autologging is enabled by default. ",
        score=2,
        justification="The output provides a working solution, using the mlflow.autolog() function that is provided in the context.",
        grading_context={
            "context": "mlflow.autolog(log_input_examples: bool = False, log_model_signatures: bool = True, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, extra_tags: Optional[Dict[str, str]] = None) → None[source] Enables (or disables) and configures autologging for all supported integrations. The parameters are passed to any autologging integrations that support them. See the tracking docs for a list of supported autologging integrations. Note that framework-specific configurations set at any point will take precedence over any configurations set by this function."
        },
    ),
    EvaluationExample(
        input="How do I disable MLflow autologging?",
        output="mlflow.autolog(disable=True) will disable autologging for all functions.",
        score=5,
        justification="The output provides a solution that is using the mlflow.autolog() function that is provided in the context.",
        grading_context={
            "context": "mlflow.autolog(log_input_examples: bool = False, log_model_signatures: bool = True, log_models: bool = True, log_datasets: bool = True, disable: bool = False, exclusive: bool = False, disable_for_unsupported_versions: bool = False, silent: bool = False, extra_tags: Optional[Dict[str, str]] = None) → None[source] Enables (or disables) and configures autologging for all supported integrations. The parameters are passed to any autologging integrations that support them. See the tracking docs for a list of supported autologging integrations. Note that framework-specific configurations set at any point will take precedence over any configurations set by this function."
        },
    ),
]
```

Use the `faithfulness` metric from `mlflow.metrics.genai`, which requires a `score` and a `justification`.
It involves the usage of another LLM to evaluate the output of the RAG system. Thus, it is a 
**SaaS Model Metric**.

```python
faithfulness_metric = faithfulness(model="openai:/gpt-4", examples=faithfulness_examples)
print(faithfulness_metric)
```

Use also a `relevance` metric and incorporates both into `mlflow.evaluate()`.
```python
from mlflow.metrics.genai import EvaluationExample, relevance

relevance_metric = relevance(model="openai:/gpt-4")

results = mlflow.evaluate(
    model,
    eval_df,
    model_type="question-answering",
    evaluators="default",
    predictions="result",
    extra_metrics=[faithfulness_metric, relevance_metric, mlflow.metrics.latency()],
    evaluator_config={
        "col_mapping": {
            "inputs": "questions",
            "context": "source_documents",
        }
    },
)
print(results.metrics)
```

## Question-Answering Evaluation
