Title: Kernel Based Methods
Date: 2017-01-21 13:28
Modified: 2017-01-21 13:28
Category: Learning
Tags: Kernel-Trick, Kernel
Slug: kernel-trick
Authors: Rishabh Chakrabarti
Summary: An insight into the Kernel-trick which allow higher dimension access/operability.

# KERNEL?

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

**Note**: This description only applies to binary classification problems -
