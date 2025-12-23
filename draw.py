#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
绘图工具 - Picture Drawing Tool
支持多种图表类型的绘制
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 设置中文字体支持
# 尝试使用可用的中文字体，如果没有则降级到默认字体
available_fonts = [f.name for f in fm.fontManager.ttflist]
chinese_fonts = ['SimHei', 'Microsoft YaHei', 'STHeiti', 'WenQuanYi Micro Hei']
selected_font = None
for font in chinese_fonts:
    if font in available_fonts:
        selected_font = font
        break

if selected_font:
    rcParams['font.sans-serif'] = [selected_font, 'DejaVu Sans']
else:
    rcParams['font.sans-serif'] = ['DejaVu Sans']
rcParams['axes.unicode_minus'] = False


def draw_line_chart(x_data, y_data, title="折线图", xlabel="X轴", ylabel="Y轴", filename="line_chart.png"):
    """
    绘制折线图
    
    参数:
        x_data: X轴数据
        y_data: Y轴数据
        title: 图表标题
        xlabel: X轴标签
        ylabel: Y轴标签
        filename: 保存的文件名
    """
    fig = plt.figure(figsize=(10, 6))
    try:
        plt.plot(x_data, y_data, marker='o', linewidth=2)
        plt.title(title, fontsize=16)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"折线图已保存到: {filename}")
    finally:
        plt.close(fig)


def draw_bar_chart(categories, values, title="柱状图", xlabel="类别", ylabel="数值", filename="bar_chart.png"):
    """
    绘制柱状图
    
    参数:
        categories: 类别列表
        values: 数值列表
        title: 图表标题
        xlabel: X轴标签
        ylabel: Y轴标签
        filename: 保存的文件名
    """
    fig = plt.figure(figsize=(10, 6))
    try:
        plt.bar(categories, values, color='skyblue', edgecolor='navy', alpha=0.7)
        plt.title(title, fontsize=16)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"柱状图已保存到: {filename}")
    finally:
        plt.close(fig)


def draw_pie_chart(labels, sizes, title="饼图", filename="pie_chart.png"):
    """
    绘制饼图
    
    参数:
        labels: 标签列表
        sizes: 大小列表
        title: 图表标题
        filename: 保存的文件名
    """
    fig = plt.figure(figsize=(10, 8))
    try:
        colors = plt.cm.Set3(range(len(labels)))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(title, fontsize=16)
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"饼图已保存到: {filename}")
    finally:
        plt.close(fig)


def draw_scatter_plot(x_data, y_data, title="散点图", xlabel="X轴", ylabel="Y轴", filename="scatter_plot.png"):
    """
    绘制散点图
    
    参数:
        x_data: X轴数据
        y_data: Y轴数据
        title: 图表标题
        xlabel: X轴标签
        ylabel: Y轴标签
        filename: 保存的文件名
    """
    fig = plt.figure(figsize=(10, 6))
    try:
        plt.scatter(x_data, y_data, c='coral', s=100, alpha=0.6, edgecolors='black')
        plt.title(title, fontsize=16)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"散点图已保存到: {filename}")
    finally:
        plt.close(fig)


if __name__ == "__main__":
    print("绘图工具演示")
    print("=" * 50)
    
    # 示例1: 折线图
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    draw_line_chart(x, y, title="正弦函数图", xlabel="x", ylabel="sin(x)", filename="example_line.png")
    
    # 示例2: 柱状图
    categories = ['一月', '二月', '三月', '四月', '五月']
    values = [23, 45, 56, 78, 32]
    draw_bar_chart(categories, values, title="月度销售数据", xlabel="月份", ylabel="销售额", filename="example_bar.png")
    
    # 示例3: 饼图
    labels = ['产品A', '产品B', '产品C', '产品D']
    sizes = [30, 25, 20, 25]
    draw_pie_chart(labels, sizes, title="产品市场份额", filename="example_pie.png")
    
    # 示例4: 散点图
    x_scatter = np.random.randn(100)
    y_scatter = 2 * x_scatter + np.random.randn(100)
    draw_scatter_plot(x_scatter, y_scatter, title="相关性分析", xlabel="变量X", ylabel="变量Y", filename="example_scatter.png")
    
    print("\n所有示例图表已生成完成！")
