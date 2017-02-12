Title: Kernel Based Methods
Date: 2017-01-21 13:28
Modified: 2017-01-21 13:28
Category: Learning
Tags: Kernel-Trick, Kernel
Slug: kernel-trick
Authors: Rishabh Chakrabarti
Summary: An insight into the Kernel-trick which allow higher dimension access/operability. Source: http://www.eric-kim.net/eric-kim-net/posts/1/kernel_trick.html

# KERNEL?
> Do Read : http://www.eric-kim.net/eric-kim-net/posts/1/kernel_trick.html


> A Kernel Function $K(\vec{v},\vec{w})$ is a function $K:\Re^N \times \Re^N \rightarrow \Re$ that obeys certain mathematical properties.

For an intermediate definition, think of the kernel function as one that computes a **dot product** between $\vec{v}, \vec{w}$.

## Linear SVM, Binary Classification

Suppose that we have a 2-class dataset $D$, and wewish to train a classifier $C$ to predict the class labels of future data points. This is known as `binary classification` problem, and can be cast as `Yes/No` questions such as :

* Medicine :
> Given a patient's vital data, does the patient have a cold?

* Computer Vision :
> Does the image contain a person?

A popular off-the-shelf classifier is the **Support Vector Machine (SVM)**, so we will use this as our classification algorithm.

### *Binary vs. Multiclass Classification*

Binary classifiers are often the focus due to their simpler presentation.

However, many problems inherently have more than 2 possible outcomes.

For instance,

> To train a face verification system that can detect the identity of a photograph from a pool of $N$ people (where $N \gt 2 $).

**This sort of problem is known as a `Multiclass` classification problem.**

Most mathematical definitions are binary classifiers.

There are 2 main approaches to the `Multiclass` problem :

1. Directly add a multiclass extension to a binary classifier.
* **Pros**: Provides a principled way of solving the muticlass problem.
* **Cons** : Multiclass extensions tend to be much more complicated than the original binary formulation. This may lead to significantly longer training and test procedures. Even worse, experimental results may not be that much better than ad-hoc methods like (2).

2. Combine multiple binary classifiers to create a 'mega' multi-multiclass classifier. 2 popular implementations of this idea are the `"One-versus-One" (OVO)` and `"One-versus-All" (OVA)` scheme.

* **Pros** : Simple idea, easy to implement, can be much faster than multiclass extensions. Some people suggest that empirical results tend to be on par with (1).
* **Cons** : Ultimately, it is an ad-hoc method for solving the multiclass problem - there may exist datasets for which OVO?OVA will perform poorly on, but general multiclass classifiers (1) perform well on.

Recall that a Linear SVM finds a hyperplane $\vec{w}$ that best separates the data points in the training set by class label.

> $\vec{w}$ is called the **decision boundary**, and cuts the space into 2 halves : one half for class '0', and the other half for class '1'.

To classify a point $x_i \epsilon X$ (where $X$ is the dataset), we simply see which 'side' of $\vec{w}$ that $x_i$ lies.

**Note**: This description only applies to binary classification problems.

A sample dataset :

![Linear_sample]({filename}/assets/2017-01-22-Kernel-trick-5e30e.png)

Training and evaluating a linear SVM on this dataset yields the following decision boundary.
![SVM_linear]({filename}/assets/2017-01-22-Kernel-trick-ca976.png)

Because the data is easily linearly separable, the SVM is able to find a margin that perfectly separates the training data, which also generalizes very well to the test set. The hyperplane (a line in ) separates the space into two halves: points that live in the brownish region are classified as class '1', whereas points that live in the blueish region are classified as class '0'.

**Unfortunately, in practice we will not always encounter such well-behaved datasets.**

Let's take a look at a dataset that is not linearly separable.

## A Linearly Nonseparable Dataset
![Non_linear_dataset]({filename}/assets/Non_linear_dataset.png)

The above dataset is a synthetically generated dataset.

```cmd
==== Evaluating Random Classifier
== Accuracy: 0.45
             precision    recall  f1-score   support

          0       0.74      0.42      0.53       151
          1       0.23      0.55      0.33        49

avg / total       0.62      0.45      0.48       200

==== Finished Random Classifier (0.000 s)

==== Evaluating SVM (kernel='linear'), 2-fold cross validation
    Parameters to be chosen through cross validation:
        C: [1.0, 10.0, 100.0, 1000.0, 10000.0]
== Best Params: {'kernel': 'linear', 'C': 1.0}
== Best Score: 0.476666666667
== Accuracy: 0.445
             precision    recall  f1-score   support

          0       0.78      0.37      0.50       151
          1       0.26      0.67      0.37        49

avg / total       0.65      0.45      0.47       200

==== Finished Linear SVM (1.290 s)
```

![Linear_Kernel]({filename}/assets/Linear_Kernel.png)


As we can see, the *RandomClassifier* and *Linear SVM* both perform poorly. It's always a bummer when our classifier is as bad as random guessing!

To get a geometric sense of the SVM's failure to cope with this dataset, see the above figure for the decision boundary.

## Dealing with Nonseparable Data

Obviously, we would like to handle linearly nonseparable data - otherwise, SVMs wouldn't be very useful.

> In the SVM example, the primary obstacle is the constraint that the decision boundary be linear in the original feature space (here,$\Re^2$ ).

*However, this is not always the correct decision boundary to find. For instance, in Figure 4, a better decision boundary would be a circular decision boundary that separates the outer cyan ring from the inner red ring.*

> Could we generalize the SVM formulation to explicitly discover decision boundaries with arbitrary shape?

As it turns out, if you get into the nitty-gritty mathematical details of the SVM, the derivations assume that the decision boundary is a separating hyperplane $\vec{w}$.

* I imagine there is a way to recast the SVM *optimization problem* such that a *more-general decision surface* can be found, but I'd bet that the resulting optimization would carry a significant computational burden when compared to the linear SVM formulation.

* So, it appears that we are stuck with an SVM that, for an N-dimensional dataset, finds an (N-1)-dimensional separating hyperplane.

**What if we could play with N...?**

## IDEA !

Separable in a higher dimension

![Higher_Dimension]({filename}/assets/Higher_Dimension.png)
