import requests
import os
import time
from tqdm import tqdm

def download_gif(url, save_path):
    """下载单张GIF图片"""
    try:
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 发送请求
        response = requests.get(url, headers=headers, stream=True, timeout=10)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 保存图片
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return True
        else:
            print(f"下载失败，状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"下载出错: {str(e)}")
        return False

def main():
    # 创建保存图片的目录
    save_dir = "xyq_gifs"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 基础URL
    base_url = "https://cbg-xyq.res.netease.com/images/big/{}.gif"
    
    # 记录成功和失败的数量
    success_count = 0
    fail_count = 0
    
    # 生成所有可能的编号并下载
    print("开始下载图片...")
    for x in tqdm(range(0, 4), desc="总体进度"):
        for y in range(1, 7):
            # 生成编号
            number = f"27{x}0{y}"
            # 构建完整URL
            url = base_url.format(number)
            # 构建保存路径
            save_path = os.path.join(save_dir, f"{number}.gif")
            
            # 下载图片
            if download_gif(url, save_path):
                success_count += 1
            else:
                fail_count += 1
            
            # 适当延迟，避免请求过于频繁
            time.sleep(1)
    
    print(f"下载完成！成功: {success_count} 张, 失败: {fail_count} 张")
    print(f"图片已保存到 {os.path.abspath(save_dir)} 目录")

if __name__ == "__main__":
    main()
