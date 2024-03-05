# Averaging Rate Scheduler for Decentralized Learning on Heterogeneous Data
This repository provides the code for "Averaging Rate Scheduler for Decentralized Learning on Heterogeneous Data."

# Abstract
Presently, state-of-the-art decentralized learning algorithms typically require the data distribution to be Independent and Identically Distributed (IID). However, in practical scenarios, the data distribution across the agents can have significant heterogeneity. In this work, we propose averaging rate scheduling as a simple yet effective way to reduce the impact of heterogeneity in decentralized learning. Our experiments illustrate the superiority of the proposed method ($\sim 3\%$ improvement in test accuracy) compared to the conventional approach of employing a constant averaging rate.

# Available Models
* MobileNet-V2
* ResNet
* VGG11
* LeNet-5

# Requirements
* found in env.yml file

# Hyper-parameters
* --world_size   = total number of agents
* --graph        = graph topology (default ring)
* --neighbors    = number of neighbor per agent (default 2)
* --arch         = model to train
* --normtype     = type of normalization layer
* --dataset      = dataset to train
* --batch_size   = batch size for training
* --epochs       = total number of training epochs
* --lr           = learning rate
* --momentum     = momentum coefficient
* --nesterov     = activates nesterov momentum
* --weight_decay = L2 regularization coefficient
* --gamma        = averaging rate for gossip 
* --growth_rate  = the factor by which gamma is multiplied after every epoch (exponential scheduler)
* --alpha        = amount of skew in the data distribution (alpha of Dirichlet distribution); 0.01 = completely non-iid and 10 = more towards iid

# How to run?

test file shows sample commands to run the code
```
sh test.sh
```


