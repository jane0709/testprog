"""运行后显示一个静态爱心，没有动画。hhhhh"""

import math

import matplotlib.pyplot as plt


def draw_heart():
    # 爱心的参数方程。
    angles = [2 * math.pi * i / 1000 for i in range(1001)]
    x = [16 * math.sin(t) ** 3 for t in angles]
    y = [
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
        for t in angles
    ]

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="#fff5f7")
    ax.set_facecolor("#fff5f7")
    ax.fill(x, y, color="#ff416c", edgecolor="#d92550", linewidth=2)
    ax.set_aspect("equal")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 16)
    ax.axis("off")
    fig.tight_layout()
    plt.show()

    print("爱心绘制完成！") 

if __name__ == "__main__":
    draw_heart()
