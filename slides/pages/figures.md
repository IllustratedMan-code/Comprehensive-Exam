---
transition: slide-up
layout: section
hideInToc: true
---

# Figure 1

---

```yaml
transition: slide-up
layout: image
image: /figures/figure1.webp
backgroundSize: 80% 90%
```

---

```yaml
transition: slide-up
layout: image-left
image: /figures/figure1-a.webp
backgroundSize: auto 90%
```

## Model Architecture

- 2Mb DNA sequence is one-hot encoded
- DNA and feature signals (ATAC, CTCF ChIP) are preprocessed separately then combined
- Transformer encoder processes combined signal into latent representation of 3D chromatin relationships
- Conv2D/Decoder transforms latent representation into recognizable Hi-C-like representation

---

```yaml
routeAlias: data-formats
transition: slide-left
layout: image-right
image: /figures/figure1-b.webp
backgroundSize: auto 90%
```

## Data Formats and Selection

- **Inputs:** <span v-mark.orange.box> 2Mb </span> regions of DNA, CTCF ChIP-seq, and ATAC-seq
- **Outputs:** matrix of interactions between <span v-mark.green.box> 8Kb </span> regions within the input (equivalent to Hi-C)
- A validation chromosome and
  a test chromosome are randomly selected from the rest of the chromosomes
- <span v-mark.blue.box> Hi-C </span> data is used for validation/testing
- Training is done with the <span v-mark.red.box> <Link to=IMR90 title="IMR-90" /> </span> cell line

---

```yaml
transition: slide-up
layout: section
hideInToc: true
```

# Figure 2

---

```yaml
layout: image
transition: slide-up
image: /figures/figure2.webp
backgroundSize: auto 95%
```

---

```yaml
layout: image-right
transition: slide-up
image: /figures/figure2-a.webp
backgroundSize: 90% 90%
```

## Cropped Image Wrong

## Input Data Types Matter

- C. Origami (DNA + CTCF + ATAC) performs the best
- Lower validation loss = better performance on the validation chromosome

---

```yaml
layout: default
transition: slide-up
image: /figures/insulation.png
backgroundSize: 80% auto
```

## Insulation Score

<div v-click="['+1', '+1']"  v-motion :initial="{ y: 100 }"  :enter="{ y: 0 }" :leave="{y: 100}" >

$$
\text{Insulation} = \frac{
	\text{max} \left ( \frac{1}{n} \sum_n \text{Left Intensity}, \frac{1}{n} \sum_n \text{right Intensity}  \right ) + \text{pseudocount}}{
	\frac{1}{n} \sum_n (\text{ Center Intensity}) + \text{pseudocount}
	}
$$

</div>

<div v-after v-motion :initial="{ y: -50 }"  :enter="{ y: -70 }" class="relative" >
$$
\text{Insulation} = \frac{
\text{max} \left ( \text{ Average Left Intensity}, \: \text{Average Right Intensity} \right ) + \text{pseudocount}}{
\text{ Average Center Intensity} + \text{pseudocount}
}
$$

</div>

<div v-click v-motion :initial="{x: 0, y: 0}" :enter="{x: 0, y: -50}" :click-4="{x: -300, y: -50}" >

<img src=/figures/insulation.png width=30% class="absolute left-50% -translate-x-1/2" />

</div>

<div v-click v-motion :initial="{x: 300, y:0}" :enter="{x: 300, y: -50}">

$
\text{Bin Radius} = 50 = 8kb \cdot 50 = 400kb = \frac{1}{5} \text{ of contact matrix}
$

```python
def chr_score(matrix, res = 10000, radius = 500000, pseudocount_coeff = 30):
	pseudocount = matrix.mean() * pseudocount_coeff
	pixel_radius = int(radius / res)
	scores = []
	for loc_i, loc in enumerate(range(len(matrix))):
		scores.append(
			point_score(loc, pixel_radius, matrix, pseudocount))
    return scores
```

</div>

<!--
A quick aside about insulation scores. They are calculated by sliding three "boxes" along the diagonal. Each point (represented by the red dot) is calculated by dividing the left or right box with the largest intensity (red) divided by the center box. Low values represent a lack of difference between left or right and center boxes.
-->

---

```yaml
layout: image-right
image: /figures/figure2-b-e.webp
transition: slide-up
backgroundSize: auto 95%
```

## It Works!

- Less <span v-mark.box.orange> "noisy" </span> than experimental
- Insulation scores are highly similar
- Insulation is inversly correlated with CTCF and ATAC-seq signal (mostly)

---

```yaml
layout: image-left
transition: slide-up
image: /figures/figure2-f-h.webp
backgroundSize: auto 95%
```

## Insulation is highly correlated

- Chromosome 10 is Validation
- Chromosome 15 is Test
- $\rho$ is Spearman, r is Pearson (all other correlations are pearson)
- C. Origami has higher correlation than competing (sequence only) models
- Direct (non-insulation) correlation decreases as distance increases

---

```yaml
layout: section
hideInToc: true
```

# Figure 3

---

```yaml
layout: image
transition: slide-up
image: /figures/figure3.webp
backgroundSize: auto 95%
```

---

```yaml
layout: image-left
transition: slide-up
image: /figures/figure3-a-d.webp
backgroundSize: auto 95%
routeAlias: figure3-a-d
```

## Works On Other Cell Types

- Correctly identifies looping differences in the GM12878 cell line
- Insulation scores are highly correlated

---

```yaml
layout: image-right
transition: slide-up
image: /figures/figure3-e-h.webp
backgroundSize: auto 95%
```

## Correlation to Experimental Data

- Insulation scores are highly correlated
- Matrix correlation is considerably lower
- Matrix correlation falls as distance increases
- Performs better than sequence-only models in all cases

---

```yaml
layout: section
hideInToc: true
```

# Figure 4

---

```yaml
transition: slide-up
layout: image
image: /figures/figure4.webp
backgroundSize: auto 95%
```

---

```yaml
transition: slide-up
layout: image-left
image: /figures/figure4-a-b.webp
backgroundSize: 95% auto
routeAlias: figure4-a-b
```

## Translocation in <Link to=CUTLL1 title="CUTLL1" /> Cells

- Opportunity to test in silico modifications
- Hi-C is performed on the CUTLL1 Cells (which have a real translocation)

<!--
Note the TAD difference from non-translocated cells indicated by the arrows
-->

---

```yaml
transition: slide-up
layout: image-right
image: /figures/figure4-c-f.webp
backgroundSize: 95% auto
```

## Synthetic Genome With Identical Translocation

- ATAC, CTCF ChIP and DNA are cut and "glued" back together to simulate translocation
- Same "Stripe" or "neo TAD" identified in in silico

---

```yaml
layout: image-left
image: /figures/figure4-g-i.webp
backgroundSize: 95% auto
```

## In Silico Deletion

- Deletion of 500-bp region alters chromatin looping
- Change is most visible in the virtual 4C signal

---

```yaml
transition: slide-up
layout: section
hideInToc: true
```

# Figure 5

---

```yaml
layout: image
image: /figures/figure5.webp
backgroundSize: auto 95%
```

---

```yaml
layout: image-left
image: /figures/figure5-abd.webp
backgroundSize: 95% auto
```

## Impact Score

- Metric calculated by in silico deletion of 1Kb regions across a 2Mb window
- Resulting model prediction is compared to non-deleted 2Mb window
- Difference maps are aggregated via mean absolute difference

---

```yaml
layout: image-right
image: /figures/figure5-c.webp
backgroundSize: auto 95%
```

## All Scores are Correlated with ATAC and CTCF signal

---

```yaml
layout: image-left
image: /figures/figure5-e-g.webp
backgroundSize: 95% auto
```

## Characterization of Identified Cis-Regulatory Elements

- Groups are clustered by presence and absence of ATAC and CTCF signal
- Each row of **e** represents a 5Kb region centered by an "important" 1Kb region

---

```yaml
layout: section
hideInToc: true
```

# Figure 6

---

```yaml
layout: image
image: /figures/figure6.webp
backgroundSize: auto 95%
```

---

