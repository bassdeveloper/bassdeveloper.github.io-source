Title: NLP using Neural Networks
Date: 2017-01-24 12:50
Modified: 2017-01-24 12:50
Category: Learning
Tags: Neural Networks, Speech recognition
Slug: neural
Authors: Rishabh Chakrabarti
Summary: Dive into Neural Networks to build End-to-End Systems
Status:draft

# Wanna Chat Honey?

> Sources :
> 1. How to make an amazing TensorFlow Chatbot: https://www.youtube.com/watch?v=SJDEOWLHYVo

Chatbots are becoming increasingly popular since a chat platform is the next most used screen after your homescreen.

Statistics show that most apps only used once.

Now applications don't need to fight for space on one end. They can simply utilize the space on the second space, i.e. Chat App.

Most simple type of neural networks are : **Feed Forward**.


# TensorFlow

## Tensors

The central unit of data in TensorFlow is the **tensor**.

> A tensor consists of a set of primitive values shaped into an array of any number of dimensions.

A tensor's rank is its number of dimensions.

```python
3 # a rank 0 tensor; this is a scalar with shape []
[1. ,2., 3.] # a rank 1 tensor; this is a vector with shape [3]
[[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]
[[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]
```

### TensorFlow Core:

#### Importing TensorFlow

The canonical import statement for TensorFlow programs is as follows:

```py
import tensorflow as tf
```
#### The Computational Graph

TensorFlow Core programs as consisiting of 2 discrete sections:

1. Building the computational graph.
2. Running the computational graph.

> A **computational graph** is a series of TensorFlow operations arranged into a graph of nodes.

Each node takes zero or more tensors as inputs and produces a tensor as an output. One type of node is a **constant**.

Like all TensorFlow constants, it takes no inputs, and it outputs a value it stores internally. We can create two floating point Tensors `node1` and `node2` as follows:

```py
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)

'''>> Output : Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)'''
```

Notice that printing the nodes does not output the values `3.0` and `4.0`. Instead, they are nodes that, when evaluated, would produce 3.0 and 4.0 respectively.

**To evaluate the nodes, we must run the computational graph within a `session`.**

> A session encapsulates the control and state of the TensorFlow

```py
sess = tf.Session()
print(sess.run([node1, node2]))

'''>> Output:  [3.0, 4.0]'''
```

We can build more complicated computations by combining `Tensor` nodes with operations (Operations are also nodes).

```py
node3 = tf.add(node1, node2)
print("node3: ", node3)
'''>> Output: node3:  Tensor("Add_2:0", shape=(), dtype=float32)'''

print("sess.run(node3): ",sess.run(node3))

'''sess.run(node3):  7.0'''
```

TensorFlow provides a utility called `TensorBoard` that can display a picture of the computational graph.

As it stands, this graph is not especially interesting because it always produces a constant result. A graph can be parametrized to accept external inputs, known as **placeholders**.

> A **placeholder** is a promise to provide a value later.

```py
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
```
The preceding three lines are a bit like a function or a lambda in which we define two input parameters (a and b) and then an operation on them.

We can evaluate this graph with multiple inputs by using the `feed_dict` parameter to specify Tensors that provide concrete values to these placeholders:

```py
print(sess.run(adder_node, {a: 3, b:4.5}))

'''
>> Output: 7.5
'''
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))

'''
>> Output: [ 3.  7.]
'''
```
Make it more complex:

```py
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b:4.5}))
'''
Output : 22.5
'''
```

Now,in machine learning, we  would typically want a model that can take arbitrary inputs.

To make the model trainable, we need to be able to modify the graph to get new outputs with the same input.

> `Variables` allow us to add trainable parameters to a graph.

```py
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
```
Constants are initialized when you call `tf.constant`, and their value can never change. By contrast, variables are not initialized when you call `tf.Variable`. To initialize all the variables in a TensorFlow program, you must explicitly call a special operation as follows:

```py
init = tf.global_variables_initializer()
sess.run(init)
```

It is important to realize `init` is a handle to the TensorFlow sub-graph that intializes all the global variables. Until we call `sess.run`, the variables are uninitialized.

Since `x` is a placeholder, we can evaluate `linear_model`
for several values of `x` simultaneously as follows:

```py
print(sess.run(linear_model,{x:[1,2,3,4]}))
'''Output: [ 0.          0.30000001  0.60000002  0.90000004]'''
```

So We've created a model, but we don't know how good it is yet. To evaluate the model on training data, we need a `y` placeholder to provide the desired values, and we need to write a loss function.

> A loss function measures how far apart the current model is from the provided data.


We'll use a standard loss model for linear regression, which sums the squares of the deltas between the current model and the provided data.

`linear_model - y` creates a vector where each element is the corresponding example's error delta.

We call tf.square to square that error. Then, we sum all the squared errors to create a single scalar that abstracts the error of all examples using `tf.reduce_sum` :

```py
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))
'''Output : 23.66'''
```

We could improve this manually by reassigning the values of W and b to the perfect values of -1 and 1.

A variable is initialized to the value provided to `tf.Variable` but can be changed using operations like `tf.assign`. For example, W=-1 and b=1 are the optimal parameters for our model. We can change W and b accordingly:
