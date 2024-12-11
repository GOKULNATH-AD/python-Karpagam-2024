### Basics of Matplotlib

Matplotlib is a Python library used for **data visualization**. It provides tools for creating static, interactive, and animated visualizations. The most commonly used module in Matplotlib is **`pyplot`**, which offers a MATLAB-like interface for creating plots.

---

### Key Features of Matplotlib

1. **Wide Variety of Plots**: Line, bar, scatter, histogram, pie charts, etc.
2. **Customizable**: Allows customization of titles, labels, legends, colors, and styles.
3. **Integration**: Works seamlessly with NumPy, Pandas, and other libraries.
4. **Interactive**: Provides zooming, panning, and interactive graphing capabilities.

---

### Installing Matplotlib

To install Matplotlib, use:

```bash
pip install matplotlib
```

---

### Basic Syntax

```python
import matplotlib.pyplot as plt

# Example: Simple Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

### Common Plot Types in Matplotlib

#### 1. **Line Plot**

Useful for visualizing trends over time or continuous data.

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

#### 2. **Bar Plot**

Used for comparing categories.

```python
categories = ["A", "B", "C"]
values = [10, 15, 7]

plt.bar(categories, values)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

---

#### 3. **Scatter Plot**

Used to display relationships between two sets of data.

```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

#### 4. **Histogram**

Used to display the frequency distribution of data.

```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

plt.hist(data, bins=5, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

---

#### 5. **Pie Chart**

Used to display proportions.

```python
sizes = [15, 30, 45, 10]
labels = ["A", "B", "C", "D"]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
```
