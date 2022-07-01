How run
---
You need have `python3` and all dependencies (list below) installed.
```python
python3 main.py
```

Dependencies
---
```sh
pip install PyQt5 scipy matplotlib
```

Function description
---
- function - mathematical function (ex.: x^2+3, is evaluate by python eval function)
- Left/Right range - Function range (Left <= x <= Right)
- Step - How accurate plot should be (Less = more accurate)
- X-axis - Draw line on x = 0
- Y-axis - Draw line on y = 0
- Find minimum - Mark the minimum of function
- Find maximum - Mark the maximum of function
- Find root - Mark the root of function
- M. Carlo - Monte Carlo method (integral, draw circles)
- N - How many circles? (More circles = more accurace)
- Rec. method - Rectangle method (integral, draw rectangles)
- Width - Rectangle width (More width = less accurate)
- Vertical - Mirror plot vertically
- Horizontal - Mirror plot horizontally
- Clear - Clear plot
- Draw - Draw another plot
- Info - All info about function (min, max, etc.)

Examples
---
#### GUI

![alt text](https://github.com/wojciechmadry/PyFunctionPlotter/blob/main/examples/gui.png)

#### 1.
- 1/x (0.01 to 10)
- np.sqrt(9-x) (0.01 to 10)
- np.abs(-2*x) (-2 to 2)

![alt text](https://github.com/wojciechmadry/PyFunctionPlotter/blob/main/examples/example1.png)

#### 2
- np.sin(x^2) (-5 to 5)
- -np.cos(x + 2)^3 (-5 to 5)

![alt text](https://github.com/wojciechmadry/PyFunctionPlotter/blob/main/examples/example2.png)

#### 3.
- np.abs(x) + np.sqrt(4-x^2) (-2 to 2)
- np.abs(x) - np.sqrt(4-x^2) (-2 to 2)

![alt text](https://github.com/wojciechmadry/PyFunctionPlotter/blob/main/examples/example3.png)

