# to import tensorflow and keras
# (tf.keras)
import tensorflow as tf
from tensorflow import keras

# to get the data
(train_images, train_labels), (test_images, test_labels) = \
  keras.datasets.mnist.load_data()

# to set the neural network model
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28,28)),
  keras.layers.Dense(128, activation=tf.nn.relu),
  keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(
  optimizer = tf.train.AdamOptimizer(),
  loss = 'sparse_categorical_crossentropy',
  metrics = ['accuracy']
)

# You train the model
model.fit(train_images, train_labels, epochs=5)

# To evaluate the model results
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test accuracy: ', test_acc)

# To make predictions
predictions = model.predict(test_images)