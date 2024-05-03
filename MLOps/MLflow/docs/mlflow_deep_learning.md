# Native Library Support
## Keras
Initialise and compile model.

```python
import keras

# Model parameters
NUM_CLASSES = 10
INPUT_SHAPE = (28, 28, 1)

# Model initialisation
model = keras.Sequential([
    keras.Input(shape=INPUT_SHAPE),
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dense(NUM_CLASSES, activation="softmax")
])

# Compile
model.compile(loss=keras.losses.SparseCategoricalCrossentropy(), 
              optimizer=keras.optimizers.Adam(), 
              metrics=['accuracy'])
```

It would be possible to log the model by **epochs** or even by **batches**:
```python
# Log per epochs
run = mlflow.start_run()
model.fit(
    x_train,
    y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_split=0.1,
    callbacks=[mlflow.keras.MlflowCallback(run)],
)
mlflow.end_run()

# Or log by batches
with mlflow.start_run() as run:
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        validation_split=0.1,
        callbacks=[mlflow.keras.MlflowCallback(run, log_every_epoch=False, log_every_n_steps=5)],
    )
```

## PyTorch
At the moment it is not supported.