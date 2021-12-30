import keras

# This file contains the two main networks used in our experiments
# This can be easily extended to treat any problem with the same strucutre



def baseline_regression_no_lambda(num_classes):
    input1 = keras.layers.Input(shape=(8,))
    output = keras.layers.Dense(num_classes, activation="softmax")(input1)
    model = keras.Model(input1, output)
    model.compile(
        optimizer=keras.optimizers.RMSprop(),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

def baseline_network_no_lambda(num_classes):
    input1 = keras.layers.Input(shape=(8,))
    m1 = keras.layers.Dense(5, activation="relu")(input1)
    output = keras.layers.Dense(num_classes, activation="softmax")(m1)
    model = keras.Model(input1, output)
    model.compile(
        optimizer=keras.optimizers.RMSprop(),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model