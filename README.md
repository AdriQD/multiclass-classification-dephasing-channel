# multiclass-classification-dephasing-channel
here available the codes used in the homonymous article, link at: https://arxiv.org/abs/2108.01571

In this repository both the code for data generation part and the several neural networks model applied for numerical studies are available.
Necessary dependance for virtual environment are:
qutip, keras, msmath. 

The data generation code makes use of the python multiprocess library for parallel computation. 


## Networks

You can find the network we used in the `neural_networks` folder. The general training pipeline can be run using the 
Keras API. The parameters can be found in the paper.

```python

    es = EarlyStopping(monitor=MONITOR, patience=PATIENCE, mode='min', verbose=0, restore_best_weights=True)

    model.fit(train_input, train_labels,
              batch_size=BATCH_SIZE,
              epochs=EPOCHS,
              validation_data=(valid_input, valid_labels),
              callbacks=[es],
              verbose=1,
              shuffle=True)

```