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
```

## Model Architecture

- 2Mb DNA sequence is one-hot encoded
- DNA and feature signals (ATAC, CTCF ChIP) are preprocessed separately then combined
- Transformer encoder processes combined signal into latent representation of 3D chromatin relationships
- Conv2D/Decoder transforms latent representation into recognizable Hi-C-like representation

::caption::

A schematic of C. Origami Architecture

---

```yaml
routeAlias: data-formats
transition: slide-left
layout: image-right
image: /figures/figure1-b.webp
```

## Data Formats and Selection

- **Inputs:** <span v-mark.orange.box> 2Mb </span> regions of DNA, CTCF ChIP-seq, and ATAC-seq
- **Outputs:** matrix of interactions between <span v-mark.green.box> 8Kb </span> regions within the input (equivalent to Hi-C)
- A validation chromosome and
  a test chromosome are randomly selected from the rest of the chromosomes
- <span v-mark.blue.box> Hi-C </span> data is used for validation/testing
- Training is done with the <span v-mark.red.box> <Link to=IMR90 title="IMR-90" /> </span> cell line

::caption::
C. Origami integrates DNA sequence, CTCF ChIP-sea and ATAC-seq signals as input features
to predict Hi-C interaction matrix in 2-Mb windows.

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
```

## Input Data Types Matter

- C. Origami (DNA + CTCF + ATAC) performs the best
- Lower validation loss = better performance on the validation chromosome

::caption::

Validation loss of models trained from different combinations of input features. Lower validation loss indicates better model performance.

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
```

## It Works!

- Less <span v-mark.box.orange> "noisy" </span> than experimental
- Insulation scores are highly similar
- Insulation is inversly correlated with CTCF and ATAC-seq signal (mostly)

<div class="absolute left-10% max-w-40% text-sm bottom-10% opacity-70%">

**b**,**c**, Experimental (**b**) and C.Origami-predicted (**c**) Hi-C
matrices of IMR-90 on training (chr2), validation (chr10) and test
(chr15) chromosomes. **d**, Input CTCF-binding and chromatin
accessibility profiles. **e**, Insulation scores calculated from
experimental (solid line) and C.Origami-predicted (dotted line) Hi-C
matrices. Pearson correlation coefficients between prediction and
target insulation scores are presented.

</div>

---

```yaml
layout: image-left
transition: slide-up
image: /figures/figure2-f-h.webp
```

## Insulation is highly correlated

- Chromosome 10 is Validation
- Chromosome 15 is Test
- $\rho$ is Spearman, r is Pearson (all other correlations are pearson)
- C. Origami has higher correlation than competing (sequence only) models
- Direct (non-insulation) correlation decreases as distance increases

::caption::
f, Insulation score correlation between predicted and experimental Hi-C matrices across all windows in both validation and test chromosomes with Pearson ($r$) and Spearman ($\rho$) correlation coefficients. g, Chromosome-wide distance-stratified interaction correlation (Pearson) between prediction and experimental data. h, Comparison of model performance across Akita, DeepC, Orca and C.Origami using genome-wide insulation score correlation between prediction and experimental data from IMR-90 cells. Error bars in the violin plots indicate minimum, mean and maximum values. μ, average insulation correlation.

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

<div class="absolute right-10% max-w-40% text-sm bottom-10% opacity-70%">

a,b, Experimental (a) and C.Origami-predicted (b) Hi-C matrices from IMR-90 (left) and GM12878 (middle), and their differences (right). Arrowheads highlight differential chromatin interactions between the two cell types. c, CTCF-binding and ATAC–seq profiles. d, Insulation scores calculated from experimental Hi-C matrices (solid line) and C.Origami-predicted Hi-C matrices (dotted line).

</div>

---

```yaml
layout: image-right
transition: slide-up
image: /figures/figure3-e-h.webp
```

## Correlation to Experimental Data

- Insulation scores are highly correlated
- Matrix correlation is considerably lower
- Matrix correlation falls as distance increases
- Performs better than sequence-only models in all cases

<div class="absolute left-5% max-w-40% text-sm bottom-0% opacity-70%">

e, Pearson correlation between insulation scores calculated from predicted and experimental Hi-C matrices across cell types. f–h, Genome-wide evaluation of sequence-based models and C.Origami using de novo prediction results from GM12878 cells. Presented metrics include insulation score correlation (f), observed versus expected matrix correlation (g) and distance-stratified correlation (h). Error bars in violin plots of f and g indicate minimum, mean and maximum values within each group. Corr, correlation; obs/exp, observed/expected.

</div>

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

::caption::

**a,** Chromosomal translocation t(7;9) in CUTLL1 cells. **b**, Experimental Hi-C data mapped to a custom reference chromosome with t(7;9) translocation

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

::caption::
Legend goes here
