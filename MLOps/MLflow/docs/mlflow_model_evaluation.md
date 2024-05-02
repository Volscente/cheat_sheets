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

eval_df = pd.DataFrame(
    {
        "questions": [
            "What is MLflow?",
            "How to run mlflow.evaluate()?",
            "How to log_table()?",
            "How to load_table()?",
        ],
    }
)

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
### Basic Evaluation
Use examples with `inputs` and related `ground_truth` and measure how well the model performs.

```python
# Create evaluation question-expected-answer
eval_df = pd.DataFrame(
    {
        "inputs": [
            "How does useEffect() work?",
            "What does the static keyword in a function mean?",
            "What does the 'finally' block in Python do?",
            "What is the difference between multiprocessing and multithreading?",
        ],
        "ground_truth": [
            "The useEffect() hook tells React that your component needs to do something after render. React will remember the function you passed (we’ll refer to it as our “effect”), and call it later after performing the DOM updates.",
            "Static members belongs to the class, rather than a specific instance. This means that only one instance of a static member exists, even if you create multiple objects of the class, or if you don't create any. It will be shared by all objects.",
            "'Finally' defines a block of code to run when the try... except...else block is final. The finally block will be executed no matter if the try block raises an error or not.",
            "Multithreading refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process. Whereas multiprocessing refers to the ability of a system to run multiple processors in parallel, where each processor can run one or more threads.",
        ],
    }
)

with mlflow.start_run() as run:
    
    # Instance the model
    system_prompt = "Answer the following question in two sentences"
    basic_qa_model = mlflow.openai.log_model(
        model="gpt-3.5-turbo",
        task=openai.chat.completions,
        artifact_path="model",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "{question}"},
        ],
    )
    
    # Evaluate the model against the evaluation samples ground_truth values
    results = mlflow.evaluate(
        basic_qa_model.model_uri,
        eval_df,
        targets="ground_truth",  # specify which column corresponds to the expected output
        model_type="question-answering",  # model type indicates which metrics are relevant for this task
        evaluators="default",
    )
print(results.metrics)
```

### LLM-Judged Correctness with Another LLM
Use another LLM to evaluate the correctness of the first one.
```python
from mlflow.metrics.genai import EvaluationExample, answer_similarity

# Create an example to describe what answer_similarity means like for this problem.
example = EvaluationExample(
    input="What is MLflow?",
    output="MLflow is an open-source platform for managing machine "
    "learning workflows, including experiment tracking, model packaging, "
    "versioning, and deployment, simplifying the ML lifecycle.",
    score=4,
    justification="The definition effectively explains what MLflow is "
    "its purpose, and its developer. It could be more concise for a 5-score.",
    grading_context={
        "targets": "MLflow is an open-source platform for managing "
        "the end-to-end machine learning (ML) lifecycle. It was developed by Databricks, "
        "a company that specializes in big data and machine learning solutions. MLflow is "
        "designed to address the challenges that data scientists and machine learning "
        "engineers face when developing, training, and deploying machine learning models."
    },
)

# Construct the metric using OpenAI GPT-4 as the judge
answer_similarity_metric = answer_similarity(model="openai:/gpt-4", examples=[example])

# Use the metric into model.evaluate()
with mlflow.start_run() as run:
    results = mlflow.evaluate(
        basic_qa_model.model_uri,
        eval_df,
        targets="ground_truth",
        model_type="question-answering",
        evaluators="default",
        extra_metrics=[answer_similarity_metric],  # use the answer similarity metric created above
    )
```

Otherwise, it is possible to define a custom metric with LLM.
```python
from mlflow.metrics.genai import EvaluationExample, make_genai_metric

# Define e custom metric
professionalism_metric = make_genai_metric(
    name="professionalism",
    definition=(
        "Professionalism refers to the use of a formal, respectful, and appropriate style of communication that is tailored to the context and audience. It often involves avoiding overly casual language, slang, or colloquialisms, and instead using clear, concise, and respectful language"
    ),
    grading_prompt=(
        "Professionalism: If the answer is written using a professional tone, below "
        "are the details for different scores: "
        "- Score 1: Language is extremely casual, informal, and may include slang or colloquialisms. Not suitable for professional contexts."
        "- Score 2: Language is casual but generally respectful and avoids strong informality or slang. Acceptable in some informal professional settings."
        "- Score 3: Language is balanced and avoids extreme informality or formality. Suitable for most professional contexts. "
        "- Score 4: Language is noticeably formal, respectful, and avoids casual elements. Appropriate for business or academic settings. "
        "- Score 5: Language is excessively formal, respectful, and avoids casual elements. Appropriate for the most formal settings such as textbooks. "
    ),
    examples=[
        EvaluationExample(
            input="What is MLflow?",
            output=(
                "MLflow is like your friendly neighborhood toolkit for managing your machine learning projects. It helps you track experiments, package your code and models, and collaborate with your team, making the whole ML workflow smoother. It's like your Swiss Army knife for machine learning!"
            ),
            score=2,
            justification=(
                "The response is written in a casual tone. It uses contractions, filler words such as 'like', and exclamation points, which make it sound less professional. "
            ),
        )
    ],
    version="v1",
    model="openai:/gpt-4",
    parameters={"temperature": 0.0},
    grading_context_columns=[],
    aggregations=["mean", "variance", "p90"],
    greater_is_better=True,
)

# Use the metric in the evaluation
with mlflow.start_run() as run:
    results = mlflow.evaluate(
        basic_qa_model.model_uri,
        eval_df,
        model_type="question-answering",
        evaluators="default",
        extra_metrics=[professionalism_metric],  # use the professionalism metric we created above
    )
```

# Traditional Models Evaluation
## Evaluate with a Function
Once the `model` if fitted (`model.fit()`), it is possible to evaluate it through a function
that computes predictions for an `eval_data`.

```python
# Define a function that calls the model's predict method
def compute_predictions(X):
    return model.predict(X)


with mlflow.start_run() as run:
    # Evaluate the function without logging the model
    result = mlflow.evaluate(
        compute_predictions,
        eval_data,
        targets="label",
        model_type="classifier",
        evaluators=["default"],
    )

print(f"metrics:\n{result.metrics}")
print(f"artifacts:\n{result.artifacts}")
```

## Evaluate with Static Dataset
Use a dataset to statically compared `y_true` and `y_pred`.
```python
model.fit(...)

# Build the Evaluation Dataset from the test set
y_test_pred = model.predict(X=X_test)
eval_data = X_test
eval_data["label"] = y_test # y_true
eval_data["predictions"] = y_test_pred # y_pred


with mlflow.start_run() as run:
    # Evaluate the static dataset without providing a model
    result = mlflow.evaluate(
        data=eval_data, # Evaluate with a static dataset
        targets="label", # Column for y_true
        predictions="predictions", # Column for y_pred
        model_type="classifier",
    )
```