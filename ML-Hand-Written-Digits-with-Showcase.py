import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'    # stop tensorflow from printing debug information, it needs to be on top of
import tensorflow as tf                     # tensorflow import
import numpy as np
import matplotlib.pyplot as plt


def show_example(count):
    print(f"This image contain a {np.argmax(predictions[count])}")
    print('Close the image to continue')
    plt.imshow(x_test[count])
    plt.show()


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)  # checking if over fitted

print('\n'*5)
print(f"loss: {format(val_loss, '.2f')}, accuracy: {format(val_acc, '.2f')}")

i = 0

if 'y' in input('\nWould you like to see some results? (y or n):'):
    predictions = model.predict([x_test])
    show_example(i)
    while True:
        if 'y' in input('\nwould you like to see more? (y or n):'):
            i += 1
            show_example(i)
        else:
            break
