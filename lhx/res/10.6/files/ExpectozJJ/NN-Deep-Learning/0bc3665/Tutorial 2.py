
# coding: utf-8

# # Tutorial 2 

# ## Q1(a): Stochastic Gradient Descent Learning

# The training data is as follows: 
# 
# |  $x=(x_1,x_2,x_3)$  |  $y$  |
# |:-------------------:|:-----:|
# |  (0.09 -0.44 -0.15) | -2.57 |
# |  (0.69 -0.99 -0.76) | -2.97 |
# |  (0.34 0.65 -0.73)  |  0.96 |
# |  (0.15 0.78 -0.58)  |  1.04 |
# | (-0.63 -0.78 -0.56) | -3.21 |
# |  (0.96 0.62 -0.66)  |  1.05 |
# |  (0.63 -0.45 -0.14) | -2.39 |
# |  (0.88 0.64 -0.33)  |  0.66 |

# In[105]:


import tensorflow as tf
import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

import os
if not os.path.isdir('figures'):
	print('creating the figures folder')
	os.makedirs('figures')


# In[4]:


no_iters = 200
lr = 0.01

SEED = 10
np.random.seed(SEED)

# generate training data
X = np.array([[0.09, -0.44, -0.15],
     [0.69, -0.99, -0.76],
     [0.34, 0.65, -0.73],
     [0.15, 0.78, -0.58],
     [-0.63, -0.78, -0.56],
     [0.96, 0.62, -0.66],
     [0.63, -0.45, -0.14],
     [0.88, 0.64, -0.33]])
Y = np.array([-2.57, -2.97, 0.96, 1.04, -3.21, 1.05, -2.39, 0.66])

print(X)
print(Y)
print(lr)

# Model parameters
w = tf.Variable(np.random.rand(3), dtype=tf.float32)
b = tf.Variable(0., dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [3])
d = tf.placeholder(tf.float32)

y = tf.tensordot(x, w, axes=1) + b
loss = tf.square(d - y) # sum of the squares

# optimizer
grad_w = -(d - y)*x
grad_b = -(d - y)
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)

# initialize variables
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# print initial weights and biases
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

# training loop begins
err = []
idx = np.arange(len(X))
for i in range(no_iters):
        
  err_ = []
  np.random.shuffle(idx)
  X, Y = X[idx], Y[idx]
  for p in np.arange(len(X)):
    y_, loss_, w_, b_ = sess.run([y, loss, w_new, b_new], {x: X[p], d: Y[p]})

    if i == 0:
      print('iter: {}'.format(i+1))
      print('p: {}'.format(p+1))
      print('x:{}, d:{}'.format(X[p], Y[p]))
      print('y: {}'.format(y_))
      print('se: {}'.format(loss_))
      print('w: {}, b: {}'.format(w_, b_))

    err_.append(loss_)
  err.append(np.mean(err_))
  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

# print final weights and error
w_, b_ = sess.run([w, b])
print('w: %s, b: %s'%(w_, b_))
print('mse: %g'%err[no_iters-1])

# plot learning curve
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/2.1a_1.png')

# find the predicted values of inputs
pred = []
for p in np.arange(len(X)):
	pred.append(sess.run(y, {x:X[p]}))

print("Predicted values: ",pred)


# ## Q1(b): Batch Gradient Descent for Linear Neuron

# In[5]:


no_iters=500

# generate training data
X = np.array([[0.09, -0.44, -0.15],
     [0.69, -0.99, -0.76],
     [0.34, 0.65, -0.73],
     [0.15, 0.78, -0.58],
     [-0.63, -0.78, -0.56],
     [0.96, 0.62, -0.66],
     [0.63, -0.45, -0.14],
     [0.88, 0.64, -0.33]])
Y = np.array([-2.57, -2.97, 0.96, 1.04, -3.21, 1.05, -2.39, 0.66])
Y = Y.reshape(8,1)

# Model parameters
w = tf.Variable(np.random.rand(3,1), dtype=tf.float32)
b = tf.Variable([0.], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [None, 3])
d = tf.placeholder(tf.float32, [None, 1])

y = tf.matmul(x,w) + b
loss = tf.reduce_sum(tf.square(d - y)) # sum of the squares

# optimizer
grad_w = -tf.matmul(tf.transpose(x), d - y)
grad_b = -tf.reduce_sum(d - y)
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)


# training loop
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init) # intialize values

# print initial weights
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

err = []
for i in range(no_iters):
  sess.run([loss, w_new, b_new], {x: X, d: Y})
  err.append(sess.run(loss, {x: X, d: Y}))

  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

  if (i < 2):
  	y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
  	print('iter: {}'.format(i+1))
  	print('y: {}'.format(y_))
  	print('loss: {}'.format(loss_))
  	print('w: {}, b: {}'.format(w_, b_))


# evaluate final weights and training error
y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
print("w: %s b: %s"%(w_, b_))
print("y: %s, mse: %g"%(y_, loss_))


# plot learning curves
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/Tutorial2_1b.png')


pred = sess.run(y, {x: X})


# ## Q2
# 
# Design a perceptron to approximate the function $y$: $$y=0.5+x_1+3x_2^2$$
# 
# for inputs $0\le x_1,x_2\le 1$
# 
# The results below show that Stochastic Gradient Descent Learning has better performance than Gradient Descent Learning as the mean squared error is lower. 

# ### Using Gradient Descent Learning

# In[43]:


no_iters=200

# generate training data
X = np.zeros((121,2))
Y = np.zeros((121,1))

n = 0
for i in np.arange(0,1.01,0.1):
    for j in np.arange(0,1.01,0.1):
        X[n]=[i,j]
        Y[n,0]=0.5+i+3*j*j
        n+=1

# Model parameters
w = tf.Variable(np.random.rand(2,1), dtype=tf.float32)
b = tf.Variable([0.], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [None, 2])
d = tf.placeholder(tf.float32, [None, 1])

u = tf.matmul(x,w) + b
y = 4*tf.sigmoid(u)
loss = tf.reduce_sum(tf.square(d - y)) # sum of the squares

# optimizer
grad_w, grad_b = tf.gradients(loss, [w, b])
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)


# training loop
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init) # intialize values

# print initial weights
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

err = []
for i in range(no_iters):
  sess.run([loss, w_new, b_new], {x: X, d: Y})
  err.append(sess.run(loss, {x: X, d: Y}))

  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

  if (i < 2):
  	y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
  	print('iter: {}'.format(i+1))
  	#print('y: {}'.format(y_))
  	print('loss: {}'.format(loss_))
  	print('w: {}, b: {}'.format(w_, b_))


# evaluate final weights and training error
y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
print("w: %s b: %s mse: %g"%(w_, b_,loss_))
#print("y: %s, mse: %g"%(y_, loss_))


# plot learning curves
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/Tutorial2_2a.png')


pred = sess.run(y, {x: X})

fig = plt.figure(2)
ax = fig.gca(projection = '3d')
ax.scatter(X[:,0], X[:,1], Y, 'ro', label='targets')
ax.scatter(X[:,0], X[:,1], pred, 'b^', label='predicted')
X1 = np.arange(0, 1, 0.1)
X2 = np.arange(0, 1, 0.1)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
plt.title('Targets and Predictions')
plt.legend()
plt.savefig('./figures/Tutorial2_2a(2).png')

plt.show()


# ### Using Stochastic Gradient Descent Learning

# In[46]:


no_iters = 200
lr = 0.01

# generate training data
X = np.zeros((121,2))
Y = np.zeros(121)

n = 0
for i in np.arange(0,1.01,0.1):
    for j in np.arange(0,1.01,0.1):
        X[n]=[i,j]
        Y[n]=0.5+i+3*j*j
        n+=1

# Model parameters
w = tf.Variable(np.random.rand(2), dtype=tf.float32)
b = tf.Variable([0.], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [2])
d = tf.placeholder(tf.float32)

u = tf.tensordot(x, w, axes=1) + b
y = 4*tf.sigmoid(u)
loss = tf.square(d - y) # sum of the squares

# optimizer
grad_w, grad_b = tf.gradients(loss, [w, b])
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)

# initialize variables
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# print initial weights and biases
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

# training loop begins
err = []
idx = np.arange(len(X))
for i in range(no_iters):
        
  err_ = []
  np.random.shuffle(idx)
  X, Y = X[idx], Y[idx]
  for p in np.arange(len(X)):
    y_, loss_, w_, b_ = sess.run([y, loss, w_new, b_new], {x: X[p], d: Y[p]})

    err_.append(loss_)
  err.append(np.mean(err_))
  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

# print final weights and error
w_, b_ = sess.run([w, b])
print('w: %s, b: %s'%(w_, b_))
print('mse: %g'%err[no_iters-1])

# plot learning curve
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/Tutorial2_2b.png')

# find the predicted values of inputs
pred = []
for p in np.arange(len(X)):
	pred.append(sess.run(y, {x:X[p]}))

fig = plt.figure(3)
ax = fig.gca(projection = '3d')
ax.scatter(X[:,0], X[:,1], Y, 'ro', label='targets')
ax.scatter(X[:,0], X[:,1], pred, 'b^', label='predicted')
X1 = np.arange(0, 1, 0.1)
X2 = np.arange(0, 1, 0.1)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
plt.title('Targets and Predictions')
plt.legend()
plt.savefig('./figures/Tutorial2_2b(2).png')

plt.show()


# ## Q3 
# 
# Train a linear neuron to learn the following function $\phi$ 
# 
# $$\phi(x,y)=1.5+ 3.3x-2.5y+0.2xy$$
# 
# for $0\le x,y,\le 1$

# (a) Sample 25 data points randomly from the input space for training

# In[163]:


X = np.random.rand(25, 3)
Y = np.random.rand(25,1)

i=0
for i in np.arange(25):
    X[i,2]=X[i,0]*X[i,1]
    Y[i]=1.5+3.3*X[i,0]-2.5*X[i,1]+0.2*X[i,0]*X[i,1]

print(X)
print(Y)


# (b) Use a gradient descent algorithm to train a linear neuron

# In[164]:


no_iters=200
lr=0.01

# Model parameters
w = tf.Variable(np.random.rand(3,1), dtype=tf.float32)
b = tf.Variable([0.], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [None, 3])
d = tf.placeholder(tf.float32, [None, 1])

y = tf.matmul(x,w) + b
loss = tf.reduce_mean(tf.square(d - y)) # sum of the squares

# optimizer
grad_w = -tf.matmul(tf.transpose(x), d - y)
grad_b = -tf.reduce_sum(d - y)
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)


# training loop
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init) # intialize values

# print initial weights
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

err = []
for i in range(no_iters):
  sess.run([loss, w_new, b_new], {x: X, d: Y})
  err.append(sess.run(loss, {x: X, d: Y}))

  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

  if (i < 2):
  	y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
  	print('iter: {}'.format(i+1))
  	print('y: {}'.format(y_))
  	print('loss: {}'.format(loss_))
  	print('w: {}, b: {}'.format(w_, b_))


# evaluate final weights and training error
y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
print("w: %s b: %s"%(w_, b_))
print("y: %s, mse: %g"%(y_, loss_))

w__ = w_

# plot learning curves
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/Tutorial2_3b.png')


pred = sess.run(y, {x: X})


# (c) Compute the training error and plot the function approximated by the linear neuron

# In[109]:


fig = plt.figure(2)
ax = fig.gca(projection = '3d')
ax.scatter(X[:,0], X[:,1], Y[:,0], color='blue', marker='x', label='targets')
ax.scatter(X[:,0], X[:,1], y_[:,0], color='red', marker='.', label='predicted')
X1 = np.arange(0, 1, 0.1)
X2 = np.arange(0, 1, 0.1)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
plt.title('Targets and Predictions')
plt.legend()
plt.savefig('./figures/Tutorial2_3b(2).png')

plt.show()

fig = plt.figure(3)
ax = fig.gca(projection = '3d')
X1 = np.arange(0, 1, 0.1)
X2 = np.arange(0, 1, 0.1)
X1,X2 = np.meshgrid(X1,X2)
Z = b_ + w_[0]*X1+w_[1]*X2+w_[2]*X1*X2
regression_plane = ax.plot_surface(X1, X2, Z)
ax.xaxis.set_major_locator(ticker.IndexLocator(base = 0.2, offset=0.0))
ax.yaxis.set_major_locator(ticker.IndexLocator(base = 0.2, offset=0.0))
ax.set_title('Function learned by linear neuron')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.savefig('./figures/Tutorial2_3b(3).png')

plt.show()


# (d) Repeat (b) and (c) for a perceptron and compare the results with those of the linear neuron 

# In[150]:


X = np.random.rand(25, 2)
Y = np.random.rand(25,1)

i=0
for i in np.arange(25):
    Y[i]=1.5+3.3*X[i,0]-2.5*X[i,1]+0.2*X[i,0]*X[i,1]

no_iters=1000
lr=0.05

# Model parameters
w = tf.Variable(np.random.rand(2,1), dtype=tf.float32)
b = tf.Variable([0.], dtype=tf.float32)

# Model input and output
x = tf.placeholder(tf.float32, [None, 2])
d = tf.placeholder(tf.float32, [None, 1])

u = tf.matmul(x,w) + b
y = 6*tf.sigmoid(u)-1
loss = tf.reduce_mean(tf.square(d - y)) # sum of the squares

# optimizer
grad_w, grad_b = tf.gradients(loss, [w, b])
w_new = w.assign(w - lr*grad_w)
b_new = b.assign(b - lr*grad_b)


# training loop
init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init) # intialize values

# print initial weights
w_, b_ = sess.run([w, b])
print('w: {}, b: {}'.format(w_, b_))

err = []
for i in range(no_iters):
  sess.run([loss, w_new, b_new], {x: X, d: Y})
  err.append(sess.run(loss, {x: X, d: Y}))

  if i%10 == 0:
          print('iter: %d, mse: %g'%(i, err[i]))

# evaluate final weights and training error
y_, loss_, w_, b_ = sess.run([y, loss, w, b], {x: X, d: Y})
print("w: %s b: %s"%(w_, b_))
print("y: %s, mse: %g"%(y_, loss_))


# plot learning curves
plt.figure(1)
plt.plot(range(no_iters), err)
plt.xlabel('epochs')
plt.ylabel('mean square error')
plt.savefig('./figures/Tutorial2_3b.png')


pred = sess.run(y, {x: X})


# In[161]:


fig = plt.figure(2)
ax = fig.gca(projection = '3d')
ax.scatter(X[:,0], X[:,1], Y[:,0], color='blue', marker='x', label='targets')
ax.scatter(X[:,0], X[:,1], y_[:,0], color='red', marker='.', label='predicted')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$y$')
plt.title('Targets and Predictions')
plt.legend()
plt.savefig('./figures/Tutorial2_3b(4).png')

plt.show()

fig = plt.figure(3)
ax = fig.gca(projection = '3d')
X1 = np.arange(0, 1, 0.05)
X2 = np.arange(0, 1, 0.05)
X1,X2 = np.meshgrid(X1,X2)
Z = b_ + w_[0]*X1+w_[1]*X2
Z = 6/(1+np.exp(-Z))-1.0
regression_plane = ax.plot_surface(X1, X2, Z)
ax.xaxis.set_major_locator(ticker.IndexLocator(base = 0.2, offset=0.0))
ax.yaxis.set_major_locator(ticker.IndexLocator(base = 0.2, offset=0.0))
ax.set_title('Function learned by perceptron')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.savefig('./figures/Tutorial2_3b(3).png')

plt.show()

