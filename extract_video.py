import os
import shutil

def extract_videos(source_dir, target_dir, video_extensions=('.wmv', '.mp4', '.avi', '.mkv')):
    """
    提取 source_dir 下所有子文件夹中的视频文件，并将其复制到 target_dir 中。

    :param source_dir: 源文件夹路径
    :param target_dir: 目标文件夹路径
    :param video_extensions: 视频文件扩展名列表
    """
    # 确保目标文件夹存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历源文件夹及其子文件夹
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(video_extensions):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)

                # 如果目标文件已存在，则重命名
                if os.path.exists(target_file):
                    base, ext = os.path.splitext(file)
                    i = 1
                    while True:
                        new_name = f"{base}_{i}{ext}"
                        target_file = os.path.join(target_dir, new_name)
                        if not os.path.exists(target_file):
                            break
                        i += 1

                # 复制文件
                shutil.copy2(source_file, target_file)
                print(f"Copied: {source_file} to {target_file}")

if __name__ == "__main__":
    source_dir = "D:\\9601_N8_DataSet"  # 源文件夹路径
    target_dir = "D:\\extracted_videos"  # 目标文件夹路径
    os.makedirs(target_dir, exist_ok=True)

    extract_videos(source_dir, target_dir)
