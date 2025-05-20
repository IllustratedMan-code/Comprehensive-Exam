import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a toy Hi-C matrix (just a gradient for illustration)
size = 100
matrix = np.random.rand(size, size) * 0.3
for i in range(size):
    for j in range(size):
        matrix[i, j] += np.exp(-((i - j) ** 2) / (2 * 20**2))  # diagonal gradient

# Parameters
locus = 50
radius = 15  # number of bins
l_edge = max(locus - radius, 0)
r_edge = min(locus + radius, size)

# Plotting
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(matrix, cmap='Reds', origin='upper')

# Left mask (top-left)
left_rect = patches.Rectangle((l_edge, l_edge), locus - l_edge, locus - l_edge,
                              linewidth=2, edgecolor='black', facecolor='none', label='Left')
ax.add_patch(left_rect)

# Right mask (bottom-right)
right_rect = patches.Rectangle((locus, locus), r_edge - locus, r_edge - locus,
                               linewidth=2, edgecolor='blue', facecolor='none', label='Right')
ax.add_patch(right_rect)

# Center mask (off-diagonal rectangle)
center_rect = patches.Rectangle((locus, l_edge), r_edge - locus, locus - l_edge,
                                linewidth=2, edgecolor='green', facecolor='none', label='Center')
ax.add_patch(center_rect)

# Add labels
ax.text(l_edge + 2, l_edge + 2, 'Left', color='black', fontsize=10)
ax.text(locus + 2, locus + 2, 'Right', color='blue', fontsize=10)
ax.text(locus + 2, l_edge + 2, 'Center', color='green', fontsize=10)

ax.set_title('Insulation Score Regions')
plt.tight_layout()
plt.show()
