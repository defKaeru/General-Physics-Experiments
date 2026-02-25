import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os

plt.rcParams['font.sans-serif'] = ['SimHei'] # 选择你系统上存在的中文黑体，例如 'SimHei'（黑体）或 'KaiTi'（楷体）
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
# plt.rcParams['text.usetex'] = True

def plot_histogram_with_normal_fit(csv_file_path):
    """
    读取单列CSV数据，绘制柱形图并叠加正态分布拟合曲线。

    参数:
    csv_file_path (str): CSV文件的路径。
    """
    # 1. 检查文件是否存在
    if not os.path.exists(csv_file_path):
        print(f"1错误：文件 '{csv_file_path}' 不存在。")
        return

    # 2. 导入CSV数据
    try:
        df = pd.read_csv(csv_file_path, header=None) # 假设CSV没有标题行
        if df.shape[1] > 1:
            print(f"2警告：CSV文件 '{csv_file_path}' 包含多列数据，将只使用第一列。")
        data = df.iloc[:, 0].dropna() # 获取第一列数据并删除NaN值
        if data.empty:
            print(f"3错误：CSV文件 '{csv_file_path}' 的第一列没有有效数据。")
            return
    except Exception as e:
        print(f"4读取CSV文件时发生错误：{e}")
        return

    # 3. 计算正态分布参数（均值和标准差）
    mu, std = norm.fit(data)
    muStd = 4  # 固定均值为4

    # 4. 绘制柱形图
    plt.figure(figsize=(10, 6)) # 设置图表大小
    n, bins, patches = plt.hist(data, bins=11, density=True, width = 0.04, alpha=0.6, color='g', label='数据柱状图')

    # 5. 绘制正态分布拟合曲线
    xmin, xmax = 3.70, 4.30
    x = np.linspace(xmin, xmax, 100)
    q = norm.pdf(x, mu, std)
    plt.plot(x, q, 'r', linewidth=2, label=r'拟合正态分布 (mu=%.2f, sigma=%.2f)' % (mu, std))
    p = norm.pdf(x, muStd, std)
    plt.plot(x, p, 'k', linewidth=2, label=r'理论正态分布 (mu=%.2f, sigma=%.2f)' % (muStd, std))

    # 6. 添加图表标题和标签
    plt.title('数据柱形图与正态分布拟合曲线')
    plt.xlabel('时间')
    plt.ylabel('概率密度')
    plt.legend() # 显示图例
    plt.grid(True, linestyle='--', alpha=0.7) # 添加网格线
    plt.show()

# --- 使用示例 ---
if __name__ == "__main__":
    # 创建一个虚拟的CSV文件用于测试
    # test_data = np.random.normal(loc=4.05, scale=0.1, size=200) # 生成1000个均值为50，标准差为10的正态分布数据
    # test_df = pd.DataFrame(test_data)
    # test_csv_filename = 'data.csv'
    # test_df.to_csv(test_csv_filename, index=False, header=False) # 保存为没有索引和标题的CSV文件

    # print(f"已创建测试文件：{test_csv_filename}")
    # print("正在生成图表...")
    
    csv_filename = 'data.csv'  # 请确保这个文件存在且只有一列数据

    # 调用函数处理并绘图
    plot_histogram_with_normal_fit(csv_filename)

    # 你可以将 'single_column_data.csv' 替换为你自己的CSV文件路径
    # 例如：
    # plot_histogram_with_normal_fit('your_data.csv')