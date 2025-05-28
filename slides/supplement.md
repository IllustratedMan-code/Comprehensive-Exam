---
layout: section
title: Supplement
hideInToc: false
---

# Supplement

---

```yaml
src: /pages/supplemental-figures.md
```

---

```yaml
routeAlias: ChIP-seq
image: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Chromatin_immunoprecipitation_sequencing.svg/800px-Chromatin_immunoprecipitation_sequencing.svg.png
layout: image-right
backgroundSize: auto 100%
```

## ChIP-seq

- Chromatin Immunoprecipitation Sequencing
- Used to determine which DNA binds to a particular protein of interest

<goBack />

---

```yaml
routeAlias: Hi-C
image: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/HiCschematic.png/1024px-HiCschematic.png
layout: image-left
backgroundSize: 95% auto
```

## Hi-C

- Used to determine 3D chromatin relationships
- Can identify <Link title="TADs" to=TAD />

::caption::
Prakrutiuday, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

<goBack />

---

```yaml
routeAlias: ATAC-seq
image: https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Tn5_Transposase_in_ATAC-seq.webp/1024px-Tn5_Transposase_in_ATAC-seq.webp.png
layout: image-right
```

## ATAC-seq

An assay for measuring accessible chromatin, in other words, chromatin that allows normal transcription factors to bind.

::caption::
By Sun, Y., Miao, N. & Sun, T. - Sun, Y., Miao, N. & Sun, T. Detect accessible chromatin using ATAC-sequencing, from principle to applications. Hereditas 156, 29 (2019). https://doi.org/10.1186/s41065-019-0105-9, CC BY 4.0, https://commons.wikimedia.org/w/index.php?curid=163464776

<goBack />

---

```yaml
routeAlias: TF
```

## Transcription Factor

Any protein that binds to DNA and alters transcriptional activity.

<goBack />

---

```yaml
routeAlias: IMR90
```

## IMR-90 cells

A cell line derived from 16-week old human female fibroblasts in the lung.

<goBack from=data-formats />

---

```yaml
routeAlias: convolutional-layer
image: https://upload.wikimedia.org/wikipedia/commons/1/19/2D_Convolution_Animation.gif
layout: image-right
backgroundSize: 95% auto
```

## Convolutional Layer

For each input value, a convolutional layer will apply a kernel matrix to the value and it's "surroundings", resulting in a single output value. Multiple kernel matrices can be learned by the layer, each attempting to identify a feature relationship. The area of a kernel matrix is known as a "receptive field".

<goBack />

---

```yaml
routeAlias: transformer-encoder
image: transformer.webp
layout: image-left
backgroundSize: 95% auto
```

## Transformer Encoder

Takes input vectors as input and "transforms" it into an embedding space where each vector represents a point in a high dimensional space. These points can then be compared to see relationships.

<goBack />

---

```yaml
routeAlias: TAD
image: https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Structural_organization_of_chromatin.png/1024px-Structural_organization_of_chromatin.png
layout: image-right
backgroundSize: 95% auto
```

## Topologically Associated Domains

Regions of chromatin that are isulated from each other. In other words,
chromatin within a TAD may interact with itself, but not with chromatin in other TADs.
<goBack />

---

```yaml
routeAlias: CUTLL1
hideInToc: true
```

# CUTLL1 Cells

CUTLL1 is human T-cell lymphoma cell line with a t(7;9) rearrangement, aberrant NOTCH1 activation and high sensitivity to gamma-secretase inhibitors.

<goBack from=figure4-a-b />

---

```yaml
routeAlias: GM12878
```

## GM12878 Cells

Epstein-Barr transfected lymphoblastoid human cell line.

<goBack from=figure3-a-d />

---

```yaml
routeAlias: GRAM
```

## GRAM score

$$
\text{GRAM}_m (r) = \sum_k \text{ReLU} (\alpha^r_k) \cdot \text{ReLU} (A^m_k)
$$

$$
a^r_k = \frac{1}{Z} \sum_i \sum_j \frac{ \partial r}{\partial A^m_{k_{i, j}}}
$$

- Z is the number of pixels or activations in a layer
- m is activation layer ID
- k is channel
- r is the full output space
- Operates on convolutional 2D layers
- Does not appear to be implemented in the source code

---
