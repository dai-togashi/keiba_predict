import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.layers.normalization import BatchNormalization

model = Sequential()
model.add(Dense(1350, activation='relu', input_dim=1350))
model.add(Dropout(0.8))
model.add(BatchNormalization())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(BatchNormalization())
model.add(Dense(15, activation='softmax'))

adam = Adam()
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

#history = model.fit(X_train, y_train, epochs=100, batch_size=50, validation_split=0.1)

import numpy as np
#data = np.random.random((100, 1350))
#print(data)
#labels = np.random.randint(10, size=(100, 1))
#print(labels)
#history = model.fit(data, labels, epochs=100, batch_size=50, validation_split=0.1)

#y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
#print(y_test)

print(np.random.randint(10, size=(100, 1)))