import matplotlib.pyplot as plt
import tensorflow as tf


def plot_data(x, y, gtitle, tlabel, xlabel, ylabel):
  plt.plot(x, y, label=tlabel, color="b")
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(gtitle)
  plt.legend()
  plt.show()

def plot_data_losses(x, train_loss, val_loss, gtitle, xlabel, ylabel):
  plt.plot(x, train_loss, label="Training loss", color="b")
  plt.plot(x, val_loss, label="Val loss", color="r")
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(gtitle)
  plt.legend()
  plt.show()

#Datos sinteticos

#Datos de entrenamiento
tiempo = tf.constant([5, 7, 12, 16, 20], dtype=tf.float32) #V independiente
masa = tf.constant([40, 120, 180, 210, 240], dtype=tf.float32) #V dependiente

#Datos de validacion
val_tiempo = tf.constant([40, 80], dtype=tf.float32)
val_masa = tf.constant([480, 960], dtype=tf.float32)

plot_data(tiempo, masa, "Masa durante reaccion quimica", "Masa con el tiepo", "Tiempo", "Masa")

#Funcion costo MSE
class MSE(tf.Module):

  def __init__(self):
    super().__init__()

  def __call__(self, Y, Yp):
    e = Y - Yp #error
    se = tf.multiply(e, e) #error cuadrado
    mse = tf.reduce_mean(se, axis=0) #como promedio de los errores cucadrados
    return mse

# Construccion modelo de regresion lineal simple
# vamos a incluir: compile(), prediction(), step(), fit()
# incluir los conceptos: step, batch, epoch

class SimpleLinearregression (tf.Module):
  def __init__(self, input_dim=1, name=None):
    super().__init__(name=name)
    rand_w = tf.random.normal([input_dim])
    rand_b = tf.random.normal([1])
    self.w = tf.Variable(rand_w, name = "w", dtype=tf.float32)
    self.b = tf.Variable(rand_w, name = "b", dtype=tf.float32)
    self.loss_function = None
    self.learning_rate = None

  def prediction(self, X):
    x = tf.constant(X, dtype=tf.float32)
    y = tf.multiply(X, self.w)+self.b
    return y

  def __call__(self, X):
    y = self.prediction(X)
    return y

  def step(self, X, Y):
    with tf.GradientTape() as tape:
      Yp = self.prediction(X)
      loss = self.loss_function(Y, Yp)

    grads = tape.gradient(loss, self.trainable_variables)

    for g, v in zip(grads, self.trainable_variables):
      v.assign_sub(self.learning_rate * g)

    new_Yp = self.prediction(X)
    new_loss = self.loss_function(Y, new_Yp)
    return new_loss

  def compile(self, loss_function, learning_rate):
    self.loss_function = loss_function
    self.learning_rate = learning_rate


  def fit(self, X_train, Y_train, X_val, Y_val, batch_size=1, epochs=1):
    train_loss = []
    val_loss = []
    num_batch = X_train.shape[0]//batch_size #Calcula num iteraciones por epoca
    for epoch in range(epochs):
      tloss = 0.0
      vloss = 0.0
      for batch in range(num_batch):
        #Entrenamiento
        b_start = batch*batch_size
        b_end = b_start + batch_size
        tloss = self.step(X_train[b_start:b_end], Y_train[b_start:b_end])

      #Validacion
      Yp = self.prediction(X_val)
      vloss = self.loss_function(Y_val, Yp)

      #Registramos el loss de entrenamiento y validacion
      train_loss.append(tloss.numpy())
      val_loss.append(vloss.numpy())
      print(f"Epoch: {epoch}, train loss: {train_loss[-1]}, val loss: {val_loss[-1]}")

    return{"train_loss":train_loss, "val_loss":val_loss}

#Crear una instancia de nuestro modelo de regresion
model = SimpleLinearregression()

#Confgurar modelo para entrenamiento
mse = MSE()
model.compile(loss_function=mse, learning_rate=0.001)

#Entrenar modelo
loss = model.fit(tiempo, masa, val_tiempo, val_masa, batch_size=1, epochs=10)

train_loss = loss["train_loss"]
val_loss = loss["val_loss"]
epochs = list(range(len(train_loss)))
plot_data_losses(epochs, train_loss, val_loss, "Desempeño del modelo durante el entrenamiento y validacion", "Epochs", "Loss")
