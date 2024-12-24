# BlockTensor3D
The scripts here are almost the same as [another repository](https://github.com/brucelyu/efrg3D) where entanglement filtering is incorporated.
Please see the description there for more details.

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
