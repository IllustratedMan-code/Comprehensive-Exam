---
theme: default
layout: intro
hideInToc: true
drawings:
  persist: false
transition: slide-left
mdc: true
---

<div class="absolute top-30">

<h1> Qualifying Exam </h1>

David Lewis

</div>

<img class="absolute right-10 bottom-30" src=/paper-title.png  width=60% />

---

```yaml
layout: center
routeAlias: toc
hideInToc: true
```

# Introduction

<Toc maxDepth=1 />

---

```yaml
routeAlias: vocab
layout: two-cols
```

### Bioinformatics

- <Link title="Transcription Factor" to=TF />
- <Link title="ChIP-seq (TF Binding)" to=ChIP-seq />
- <Link title="ATAC-seq (Chromatin Accessibility)" to=ATAC-seq />
- <Link title="Hi-C (3D Chromatin Conformation)" to=Hi-C />
- <Link title="Topologically Associated Domains (TADs)" to=TAD />

::right::

### Machine Learning

- <Link to=convolutional-layer title="Convolutional Layer" />
- <Link to=transformer-encoder title="Transformer Encoder" />

<!--
A Choose Your Own Adventure style of introduction. If everyone knows the topics listed here, we can move on.
-->

---

```yaml
layout: center
```

# Purpose?

<div v-click v-motion :initial="{ y: -50 }" :enter="{ y: 0 }">

$$
\text{Hi-C} \approx model(\text{DNA, CTCF ChIP-seq, ATAC-seq})
$$

</div>

<!--
Everything in the paper boils down to predicting 3D chromatin conformation from DNA sequence, CTCF binding and chromatin accessibility.
-->

---

# Rationale

<v-clicks>
- Hi-C is expensive when compared to CTCF ChIP + ATAC-seq
- In silico experiments
- No other multi-modal models

</v-clicks>

<!--
In silico experiments manipulate the presence of cis-regulatory elements (DNA)
-->

---

# Why CTCF?

<v-clicks>

- Often found at the boundaries of TADs
- Forms a complex with cohesin to insulate regions of chromatin

</v-clicks>

<SlidevVideo v-click autoplay controls>
<source src=/pages/CTCF.webm />
</SlidevVideo>

---

```yaml
layout: intro
```

# Results

---

```yaml
src: pages/figures.md
```

---

```yaml
layout: intro
```

# Discussion

---

## Critiques

- CTCF only performs this function in mammals
- Insulation is not a perfect metric
- Does not capture distant interactions well
- No "meta methods" about ML model architecture

---

## Future Work?

- CTCF ChIP-seq model from sequence data
- ATAC model from sequence data
- A "sequence-only" model provides more oppourtunity for insilico modification.

---

## Agree or Disagree?

<v-clicks>

Agree!

</v-clicks>

---

```yaml
src: supplement.md
```
