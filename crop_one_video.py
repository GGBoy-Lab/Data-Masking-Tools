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

def main():
    # 创建 Tkinter 窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 选择输入文件
    input_file = filedialog.askopenfilename(title="Select Input Video File", filetypes=[("Video Files", "*.wmv *.mp4 *.avi *.mkv")])
    if not input_file:
        print("No input file selected. Exiting.")
        return

    # 获取输入文件的目录和文件名
    input_dir = os.path.dirname(input_file)
    input_filename = os.path.basename(input_file)
    input_base, input_ext = os.path.splitext(input_filename)

    # 默认输出文件名与输入文件名相同，但扩展名为 .mp4
    default_output_filename = f"{input_base}.mp4"
    default_output_path = os.path.join(input_dir, default_output_filename)

    # 选择输出文件
    output_file = filedialog.asksaveasfilename(
        title="Select Output Video File",
        initialfile=default_output_filename,
        defaultextension=".mp4",
        filetypes=[("MP4 Files", "*.mp4")]
    )
    if not output_file:
        print("No output file selected. Please select an output file to proceed.")
        return

    # 设置裁剪区域坐标
    x1 = 250  # 左上角 X 坐标
    y1 = 137  # 左上角 Y 坐标
    x2 = 1030  # 右下角 X 坐标
    y2 = 820  # 右下角 Y 坐标

    print(f"Cropping {input_file} to {output_file}")
    crop_video(input_file, output_file, x1, y1, x2, y2)

if __name__ == "__main__":
    main()
