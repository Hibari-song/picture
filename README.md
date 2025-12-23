# picture
绘图工具 - Picture Drawing Tool

一个简单易用的Python绘图工具，支持多种图表类型。

## 功能特点

- 📊 折线图 (Line Chart)
- 📊 柱状图 (Bar Chart)  
- 📊 饼图 (Pie Chart)
- 📊 散点图 (Scatter Plot)
- 支持中文标签
- 高清输出 (300 DPI)

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

### 运行示例

直接运行脚本查看示例：

```bash
python draw.py
```

这将生成四个示例图表：
- `example_line.png` - 正弦函数折线图
- `example_bar.png` - 月度销售柱状图
- `example_pie.png` - 产品份额饼图
- `example_scatter.png` - 相关性散点图

### 在代码中使用

```python
from draw import draw_line_chart, draw_bar_chart, draw_pie_chart, draw_scatter_plot
import numpy as np

# 绘制折线图
x = np.linspace(0, 10, 100)
y = np.cos(x)
draw_line_chart(x, y, title="余弦函数", xlabel="x", ylabel="cos(x)", filename="my_line.png")

# 绘制柱状图
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
draw_bar_chart(categories, values, title="数据对比", filename="my_bar.png")

# 绘制饼图
labels = ['部分1', '部分2', '部分3']
sizes = [30, 45, 25]
draw_pie_chart(labels, sizes, title="比例分布", filename="my_pie.png")

# 绘制散点图
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 5, 4, 6]
draw_scatter_plot(x_data, y_data, title="数据分布", filename="my_scatter.png")
```

## API 文档

### draw_line_chart(x_data, y_data, title, xlabel, ylabel, filename)
绘制折线图

### draw_bar_chart(categories, values, title, xlabel, ylabel, filename)
绘制柱状图

### draw_pie_chart(labels, sizes, title, filename)
绘制饼图

### draw_scatter_plot(x_data, y_data, title, xlabel, ylabel, filename)
绘制散点图

## 依赖

- matplotlib >= 3.5.0
- numpy >= 1.21.0

## 许可

MIT License
