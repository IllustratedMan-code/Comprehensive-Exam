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

<h1 style="font-size: 3rem;"> Comprehensive Exam </h1>

David Lewis

</div>

<img class="absolute right-10 bottom-30" src=/paper-title.png  width=70% />

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

<h1 class="absolute top-10" > Key Terms </h1>

<br>
<br>
<br>

### Bioinformatics

- <Link title="Transcription Factor" to=TF />
- <Link title="ChIP-seq (TF Binding)" to=ChIP-seq />
- <Link title="ATAC-seq (Chromatin Accessibility)" to=ATAC-seq />
- <Link title="Hi-C (3D Chromatin Conformation)" to=Hi-C />
- <Link title="Topologically Associated Domains (TADs)" to=TAD />

::right::

<br>
<br>
<br>

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

# Purpose

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
- No other multi-modal models at time of writing

</v-clicks>

<!--
In silico experiments manipulate the presence of cis-regulatory elements (DNA)
-->

---

```yaml
hideInToc: true
```

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

<v-clicks>

- CTCF only performs this function in mammals
- Insulation is not a perfect metric
- Does not capture distant interactions well
- No "meta methods" about ML model architecture
- No experimental validation for in silico deletions

</v-clicks>

---

## Future Work?

- CTCF ChIP-seq model from sequence data
- ATAC model from sequence data
- A "sequence-only" model provides more opportunity for in silico modification.

---

## Overall Consensus

<h1 v-click=1 class="absolute bottom-60 left-100"> Approved! </h1>
<Fireworks v-click=1 />

---

```yaml
src: supplement.md
```
