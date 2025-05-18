---
theme: default
#background: https://cover.sli.dev
layout: cover
hideInToc: true
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Qualifying Exam

David Lewis

---

```yaml
layout: center
routeAlias: toc
```

<Toc maxDepth=1 />

---

```yaml
routeAlias: vocab
```

## Vocab Check

- <Link title="Transcription Factor" to=TF />
- <Link title="ChIP-seq (TF Binding)" to=ChIP-seq />
- <Link title="ATAC-seq (Chromatin Accessibility)" to=ATAC-seq />
- <Link title="HI-C (3D Chromatin Conformation)" to=HI-C />

---

```yaml
layout: center
```

# What is the purpose?

<div v-click v-motion :initial="{ y: -50 }" :enter="{ y: 0 }">

$$
\text{HI-C} \approx model(\text{DNA, CTCF ChIP-seq, ATAC-seq})
$$

</div>

<!--
Everything in the paper boils down to predicting 3D chromatin conformation from DNA sequence, CTCF binding and chromatin accessibility.
-->

---

## Why do this?

<v-clicks>

- HI-C is expensive when compared to CTCF ChIP + ATAC-seq
- In silico experiments

</v-clicks>

<!--
In silico experiments manipulate the presence of cis-regulatory elements (DNA)
-->

---

```yaml
src: supplement.md
```
