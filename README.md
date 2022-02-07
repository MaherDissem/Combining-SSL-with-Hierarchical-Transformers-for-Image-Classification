# Combining-SSL-with-Hierarchical-Transformers-for-Image-Classification

Supervised learning can learn large representational spaces, which are crucial for handling difficult learning tasks. However, due to the design of the model, classical image classification approaches struggle to generalize to new problems and new situations when dealing with small datasets.
In fact, supervised learning can lose the location of image features which leads to supervision collapse in very deep architectures.

In [1], it is show how self supervision with strong and sufficient augmentation of unlabeled data can train effectively the first layers of a neural network even better than supervised learning, with no need for a large labeled dataset. Pixel data is diconnected from annotation by getting generic task-agnostic low-level features.

&nbsp;

Transformer models yield impressive results on many NLP and computer vision tasks. However they are infeasible to train on tasks with very long input sequences, for instance on high resolution images: each self-attention layer, at least in its original form, has complexity quadratic in the length of the input.

To alleviate these issues, [2] proposes to change the Transformer architecture to first shorten the internal sequence of activations when going deeper in the layer stack and then expand it back before generation.
This way, Hierarchical transformers improve upon theTransformer baseline given the same amount of computationand can yield the same results as Transformers more efficiently.

&nbsp;

In this research, we propose a model that combines the BYOL's low level features extraction with Hierarchical transformers. We then show that this resulting model achieves competitive results on benchmarks across image classification tasks using well established datasets like STL-10.

&nbsp;

Based on:

[1] S. NAIMI, R. V. LEEUWEN, AND W. MSEDDI, Performance study of combining self supervised learning with visual transformers, Pattern Recognition, (2021), pp. 341–352.

[2] P. NAWROT, S. TWORKOWSKI, M. TYROLSKI, L. KAISER, Y. WU, C. SZEGEDY, AND H. MICHALEWSKI, Hierarchical transformers are more efficient language models, CoRR, abs/2110.13711 (2021)
