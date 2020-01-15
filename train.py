import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization


if __name__ == '__main__':

  model = Sequential()
  model.add(Dense(1350, activation='relu', input_dim=1350))
  model.add(Dropout(0.8))
  model.add(BatchNormalization())
  model.add(Dense(128, activation='relu'))
  model.add(Dropout(0.5))
  model.add(BatchNormalization())
  model.add(Dense(15, activation='softmax'))

  model.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

  #history = model.fit(X_train, y_train, epochs=100, batch_size=50, validation_split=0.1)
