Title: Neural Network
Date: 2017-04-15 19:46
Modified: 2017-04-15 19:46
Category: Learning
Tags: Neural Networks, Neurons, Perceptrons
Slug: neural_theory
Authors: Rishabh Chakrabarti
Summary: Basics of Neural Networks and theory.
Status : draft
# Biology !

The theory Artificial of Neural networks (ANN) is based on the human neural network. Closely modelled after the biological system of neurons. Let's dive into the fundamental theory behind why nature chose this path and what's in it for us w.r.t. construction of a general purpose computer and creation of a sophisticated system using the current digital computer model, i.e. Turing machine.

## Let's dive into the biology

The elementary unit is a [**NEURON**](https://en.wikipedia.org/wiki/Neuron).

![Neuron](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Complete_neuron_cell_diagram_en.svg/819px-Complete_neuron_cell_diagram_en.svg.png)

The main funda is that neurons make connections and they make a lot of them. Going into numbers and stats,

* The *average human brain* contains : $10^{10}$ to $10^{11}$ neurons.
* Each neuron making $100$ to $1000$ connections
* i.e. Total number of connections are : $10^{14}$ to $10^{15}$ !!

If every neuron connected to every neuron, this number would explode!

### Neurotic facts :

1. The neurons are **mechanically highly sensitive** (as observed in a *funny bone* or *knee-jerk* reflex ) and hence the brain is protected and enclosed in a hard skull and suspended in a fluid (**hydraulic suspension system**).

2. Neurons are **metabolically very active** and the nervous system consumes 25% of the energy produced. This is due to the electrochemistry of neurons. This high metabolism provides two facts :
    * This metabolically active tissue is *most sensitive to poisons* and *temporary lack of fuel*. Thus, there is a **blood-brain barrier** in place. This is an elaborate metabolic mechanism to regulate brain chemistry and insulate it from the less-poison-sensitive rest of the body.
    * This high metabolic rate also forces nature to make the whole network the most optimized as possible.

3. The **most peculiar** fact is : Neurons don't divide after a time roughly coinciding with birth. When a neuron dies, it is not replaced. From the viewpoint of ANN, it is cheating to invent new neurons if the system needs to be biologically plausible. The neurons present in the beginning are all you can use. It is all right to reuse old ones but not to generate new ones.

Thus, we have established the fact that neurons are biologically expensive and have a huge overhead.

> *Neurons must earn their keep*

There is a **strong biological** pressure to keep minimum number of neurons.

> **CONJECTURE**: *It might be necessary to have 10 billion or more neurons to attain the level of intelligence we currently have.*

For those interested in building i.e. practically constructing the whole neural network, fewer artificial neurons than the above conjecture are adequate to simulate higher mental function.

But here, something important needs to be looked at. The **sheer size!** and comparison parameter between the real and artificial network.

### Synapses and Activation

The most common synapses in the structure that we are trying to model are **chemical synapses**. Chemical synapses use *chemical transmitters* called **neurotransmitters**. It is important to realize the great variety of neurotransmitters and synaptic specializations in the real nervous system.

Synapses are likely to be specialized in ways that directly affect their computational function.

Therefore, the esoteric details of synaptic function may be directly relevant to the neural network modeler in a way that many of the other details of neurophysiology are not.

The vast majority of models assume that a synapse has strength, like a resistor, that remains stable until it is changed by a well-defined learning rule.

> In real, the synapses are way too complex.

### Membrane Potential

The Membrane Potential is between 50 to 90 mV and depends on the cell type.

If a cell has a 70 Angstrom thickness and a -70 mV membrane potential, it would result in an electrical field across the membrane of the order of 100,000 V per cm. Such a high electrical field corresponds to extreme electrical stress on the membrane and the structures in it.

Neuron's have a **Na-K pump** operating constantly to maintain the membrane potential. This causes a huge metabolic overhead.

When the membrane potential becomes more negative, the cell is referred to as *hyperpolarized* and when the membrane potential becomes less negative, it is referred to as *depolarized*.

### Action Potential
