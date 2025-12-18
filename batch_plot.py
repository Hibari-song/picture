# -*- coding: utf-8 -*-
"""
批量绘图程序
用于绘制data3.30env.xlsx中15个工况的数据图
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import numpy as np
import os

# 设置字体
plt.rcParams['font.family'] = ['Times New Roman', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'stix'

# 自定义字体
times_font = FontProperties(family='Times New Roman')
simsun_font = FontProperties(family='SimSun')

# 颜色设置（参考图片中的颜色）
COLORS = {
    'STC': '#FF0000',      # 红色
    'PSTC': '#00FF00',     # 绿色  
    'ASTC4': '#0000FF'     # 蓝色
}

# 线型设置
LINE_STYLES = {
    'STC': '-',
    'PSTC': '-',
    'ASTC4': '-'
}

# 数据组定义
DATA_GROUPS = {
    'Y': ['STC_Y', 'PSTC_Y', 'ASTC4_Y'],
    'Rotation_3': ['STC_Rotation_3', 'PSTC_Rotation_3', 'ASTC4_Rotation_3'],
    'Rotation_1': ['STC_Rotation_1', 'PSTC_Rotation_1', 'ASTC4_Rotation_1'],
    'wing1': ['STC_wing1', 'PSTC_wing1', 'ASTC4_wing1'],
    'wing2': ['STC_wing2', 'PSTC_wing2', 'ASTC4_wing2'],
    'wing3': ['STC_wing3', 'PSTC_wing3', 'ASTC4_wing3']
}

# Y轴标签（中文）
Y_LABELS = {
    'Y': 'Y方向位移',
    'Rotation_3': '旋转角3',
    'Rotation_1': '旋转角1', 
    'wing1': '舵翼1',
    'wing2': '舵翼2',
    'wing3': '舵翼3'
}

def create_figure():
    """创建图形，参考image.png的尺寸"""
    # 设置图形尺寸（约和参考图像相似）
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    return fig, ax

def setup_axes(ax, x_max=200, x_interval=20):
    """设置坐标轴样式"""
    # 设置X轴范围和刻度
    ax.set_xlim(0, x_max)
    ax.set_xticks(np.arange(0, x_max + 1, x_interval))
    
    # 设置刻度朝内
    ax.tick_params(axis='both', direction='in', length=5, width=1)
    
    # 设置边框样式
    for spine in ax.spines.values():
        spine.set_linewidth(1)
    
    # 设置X轴标签
    ax.set_xlabel('Time (s)', fontproperties=times_font, fontsize=12)
    
    # 设置刻度字体为Times New Roman
    for label in ax.get_xticklabels():
        label.set_fontproperties(times_font)
        label.set_fontsize(10)
    for label in ax.get_yticklabels():
        label.set_fontproperties(times_font)
        label.set_fontsize(10)

def plot_data_group(df, group_name, columns, ax, colors, linestyles):
    """绘制一组数据"""
    time = df['Time']
    
    for col in columns:
        # 提取方法名称（STC, PSTC, ASTC4）
        method = col.split('_')[0]
        color = colors.get(method, '#000000')
        linestyle = linestyles.get(method, '-')
        
        ax.plot(time, df[col], color=color, linestyle=linestyle, 
                linewidth=1, label=method, alpha=0.8)

def add_legend(ax):
    """添加图例"""
    legend = ax.legend(loc='upper right', frameon=True, fontsize=10,
                      prop=times_font)
    legend.get_frame().set_linewidth(1)
    legend.get_frame().set_edgecolor('black')

def save_figure(fig, output_path, dpi_main=300, dpi_thumb=72):
    """保存图形（矢量图和缩略图）"""
    # 保存PDF矢量图
    pdf_path = output_path.replace('.png', '.pdf')
    fig.savefig(pdf_path, format='pdf', bbox_inches='tight', dpi=dpi_main)
    
    # 保存SVG矢量图
    svg_path = output_path.replace('.png', '.svg')
    fig.savefig(svg_path, format='svg', bbox_inches='tight')
    
    # 保存PNG高分辨率
    fig.savefig(output_path, format='png', bbox_inches='tight', dpi=dpi_main)
    
    # 保存缩略图
    thumb_path = output_path.replace('.png', '_thumb.png')
    fig.savefig(thumb_path, format='png', bbox_inches='tight', dpi=dpi_thumb)
    
    return pdf_path, svg_path, output_path, thumb_path

def process_sheet(excel_file, sheet_name, output_dir):
    """处理单个工况"""
    print(f"正在处理工况 {sheet_name}...")
    
    # 读取数据
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    
    # 过滤时间范围 0-200s
    df = df[df['Time'] <= 200]
    
    # 为每个数据组创建图表
    for group_name, columns in DATA_GROUPS.items():
        # 检查列是否存在
        available_cols = [col for col in columns if col in df.columns]
        if not available_cols:
            print(f"  跳过 {group_name}：无可用数据列")
            continue
            
        # 创建图形
        fig, ax = create_figure()
        
        # 绘制数据
        plot_data_group(df, group_name, available_cols, ax, COLORS, LINE_STYLES)
        
        # 设置坐标轴
        setup_axes(ax)
        
        # 添加Y轴标签
        y_label = Y_LABELS.get(group_name, group_name)
        ax.set_ylabel(y_label, fontproperties=simsun_font, fontsize=12)
        
        # 添加标题
        title = f'工况{sheet_name} - {y_label}'
        ax.set_title(title, fontproperties=simsun_font, fontsize=14)
        
        # 添加图例
        add_legend(ax)
        
        # 保存图形
        output_name = f'case{sheet_name}_{group_name}.png'
        output_path = os.path.join(output_dir, output_name)
        save_figure(fig, output_path)
        
        print(f"  已保存: {group_name}")
        
        plt.close(fig)

def main():
    """主函数"""
    # 文件路径
    excel_file = r'F:\无模型自适应舵\绘图\data3.30env.xlsx'
    output_dir = r'F:\无模型自适应舵\绘图\output'
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有工况（sheet名称）
    xl = pd.ExcelFile(excel_file)
    sheet_names = xl.sheet_names
    
    print(f"共发现 {len(sheet_names)} 个工况")
    print("-" * 50)
    
    # 先处理第一个工况作为示例
    process_sheet(excel_file, sheet_names[0], output_dir)
    
    print("-" * 50)
    print("第一个工况处理完成！请检查output文件夹中的图形。")

if __name__ == '__main__':
    main()
