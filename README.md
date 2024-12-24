# BlockTensor3D
The scripts here are almost the same as [another repository](https://github.com/brucelyu/efrg3D) where entanglement filtering is incorporated.
Please see the description there for more details.
The codes here can reproduce the results shown in the Figure 2 of this arXiv preprint: [Essential difference between 2D and 3D from the perspective of real-space renormalization group](https://arxiv.org/abs/2311.05891).


## Short guide for running the script
Let's perform the calculation at bond dimension $\chi=4$.

1. For determining $T_c$
```python
python bisectTc.py --scheme hotrg3d --chi 4 --rgn 18 --itern 9 --Tlow 4.0 --Thi 5.0
```
Run it two times to estimate the $T_c$ with a high precision value, which is about 4.56081 at this small bond dimension.

2. For generate RG flow at estimated $T_c$
```python
python flow2FixTen.py --scheme hotrg3d --chi 4 --rgn 12
```
From the information printed in the terminal, we see that the RG errors are about 20% near the critical fixed-point tensor.
The fixed-point tensor is pretty fixed at this small bond dimension.
But it is exception.
In general, the tensor isn't fixed near the critical region for bond dimension $\chi>4$.
You can check this claim by changing the bond dimension.

3. For linearization of RG equation and extracting scaling dimensions
```python
python textbookRG.py --scheme hotrg3d --chi 4 --rgstart 4 --rgend 9
```
At this very small bond dimension, the estimated values are crude, but stable with respect to the RG step.
However, at larger bond dimensions, the estimated values drift with the RG step.
You can check this by changing the bond dimension to any larger values, $\chi=6$ for example.


## How to reproduce the results in the preprint?
In general, the tensor isn't fixed near the critical region.
We need to fix a convention of choosing the RG step for linearizing the RG map.
We choose the RG step $n$ where the tensor is the most fixed, or the norm of the two tensors of the adjacent RG steps is smallest.
For example, at $\chi=6$, after running the script `flow2FixTen.py`, the output figure `tenDiff.png` shows that at the RG step $n=4$, the difference $||A^{(n+1)} - A^{(n)}||$ is smallest.
Hence, we choose the estimated scaling dimensions at $n=4$.
In the Figure 2 of the arXiv preprint, the chosen RG step is summarized in the following table:
| $\chi$    | 4 | 6 | 7 | 8 | 10 | 12 | 14 | 15 | 18 | 20 |
|-----------|---|---|---|---|----|----|----|----|----|----|
| RG step n | 8 | 4 | 5 | 5 | 5  | 6  | 7  | 8  | 9  | 8  |
