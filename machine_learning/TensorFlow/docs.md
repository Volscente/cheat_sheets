# Introduction
## Definition
TensorFlow is an open-source, high-performance library for numerical computation. It is especially useful for GPU computations, written in a high-level programming language like Python.
## DAG (Direct Acyclic Graphs)
The way TensorFlow works is that you create a directed graph, or a DAG, to represent the computation that you want to do. In this way, what matters for executing the TF code is only the DAG
representation. Thus it can be easily ported to different programming languages and hardware.
## TensorFlow Execution Engine
It executes the DAG based on the hardware underneath (CPU, GPU or TPU)
## API Architecture
![img_tf_docs_1.png](./../../images/machine_learning/img_tf_docs_1.png)
# TensorFlow Tensors
## Constant vs Variables
The function `tf.constant([3, 2])` produces a Tensor of contanst that can not be modified.

On the other hand, `x = tf.Variable(2.0, dtype=tf.float32, name='my_variable` initialises a Tensor that can change value over time.
Very useful if you need, for example, have a Tensor of weights of a Neural Network.

The value of the Variable can be change through:
- `x.assign(3.0)`
- `x.assign_add(4.0)`
- etc.
# TensorFlow Data
## Definition
The module `tf.data` is a module to build efficient Data Pipeline of data preprocessing steps.
## Dataset Class
It represents a sequence of elements. It could represent, for example, a set of data points with the corresponding
labels.
# TensorFlow Model
## Sequential API
It allows to create a model that is composed by several sequential layers, with a single input/output.
## Functional API
It allows to create an arbitrary model, not only a Sequential Model. It is however limited in customization.
That's why we want the Subclassing API.
## Subclassing API
Implements everything from scratch.
Like in the example below:
![Subclassing Example](./../../images/machine_learning/img_tf_docs_2.png)
# TensorFlow Transform
## Definition
This API is dedicated to processing data for train, prediction and evaluation processes. It is strictly related to Apache Beam, which performs the so called *Analyze* phase, while TensorFlow Transform does the *Transformation* phase.
## PTransforms
These are two methods for *Analyze and Transform* a dataset:
- **AnalyzeAndTransformDataset** - It is executed in Beam to create a training dataset (like *fit_transform* in Scikit-Learn)
- **TransformDataset** - It is executed in Beam to create the evaluation dataset (like *transform* in Scikit-Learn)

Before you call the **AnalyzeAndTransformDataset** (Analyze phase), save the transformation function and then re-use it in the **TransformDataset** (Transform phase) to create the evaluation dataset.