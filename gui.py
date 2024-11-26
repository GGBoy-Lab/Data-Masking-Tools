import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def crop_video(input_file, output_file, x1, y1, x2, y2):
    # FFmpeg 可执行文件的完整路径
    ffmpeg_path = r'C:\Users\Administrator\anaconda3\envs\opencv\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win64-v4.2.2.exe'

    # 构建 FFmpeg 命令
    command = [
        ffmpeg_path,
        '-i', input_file,  # 输入文件
        '-vf', f'crop={x2 - x1}:{y2 - y1}:{x1}:{y1}',  # 裁剪参数
        '-c:v', 'libx264',  # 使用 H.264 编码器
        '-crf', '18',  # 设置 CRF 值
        '-preset', 'slow',  # 设置编码速度/质量权衡
        '-b:v', '5000k',  # 设置视频比特率
        '-c:a', 'copy',  # 复制音频流
        output_file  # 输出文件
    ]

    # 执行命令
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing FFmpeg: {e}")
    except FileNotFoundError as e:
        print(f"FFmpeg not found: {e}")

def batch_crop_videos(input_folder, output_folder, x1, y1, x2, y2):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.wmv', '.mp4', '.avi', '.mkv')):  # 支持的视频格式
            input_file = os.path.join(input_folder, filename)
            # 生成输出文件路径，统一为 .mp4 格式
            output_filename = os.path.splitext(filename)[0] + '.mp4'
            output_file = os.path.join(output_folder, output_filename)
            print(f"Cropping {input_file} to {output_file}")
            crop_video(input_file, output_file, x1, y1, x2, y2)

def main():
    # 创建 Tkinter 窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 选择输入文件夹
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    if not input_folder:
        print("No input folder selected. Exiting.")
        return

    # 选择输出文件夹
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        print("No output folder selected. Exiting.")
        return

    # 设置裁剪区域坐标
    x1 = 250  # 左上角 X 坐标
    y1 = 137  # 左上角 Y 坐标
    x2 = 1030  # 右下角 X 坐标
    y2 = 820  # 右下角 Y 坐标

    batch_crop_videos(input_folder, output_folder, x1, y1, x2, y2)

if __name__ == "__main__":
    main()
