import numpy as np
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Conv2D, MaxPool2D, Dense
from tensorflow.keras.utils import to_categorical

X_train = mnist.train_images()
y_train = mnist.train_labels()
X_test = mnist.test_images()
y_test = mnist.test_labels()

X_train = X_train / 255
X_test = X_test / 255

X_train = np.expand_dims(X_train, axis=3)

X_test = np.expand_dims(X_test, axis=3)

model = Sequential([
  Conv2D(16, 3, input_shape=(28,28,1)),
  MaxPool2D(pool_size=2, strides=2),
  Conv2D(2, 3),
  MaxPool2D(pool_size=2, strides=2),
  Flatten(),
  Dense(128, activation='relu'),
  Dense(10, activation='softmax')
])

model.summary()

model.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

y_train_ohe = to_categorical(y_train)
y_test_ohe = to_categorical(y_test)

history = model.fit(X_train,y_train_ohe, epochs=10, validation_data=(X_test,y_test_ohe), batch_size=300)

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], c='red', label='Train Data')
plt.plot(history.history['val_accuracy'], c='blue', label='Validation Data')
