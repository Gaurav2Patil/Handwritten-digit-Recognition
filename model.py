import tensorflow as tf
import numpy as np  
from keras.models import Sequential,load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Import Mnist dataset 
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Create the model
model = Sequential()
model.add(Conv2D(784, kernel_size=(3, 3), activation='relu', input_shape=(28,28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
with tf.device('/GPU:0'):
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10)

# Save the trained model
model.save('models/handwritten_digit_model.h5')
model.save('models/handwritten_digit.model')

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")

# Calculate and display training accuracy
train_loss, train_accuracy = model.evaluate(x_train, y_train)
print(f"Train accuracy: {train_accuracy * 100:.2f}%")

