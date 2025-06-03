import os
from g2pk import G2p

# G2P 변환기 초기화
g2p = G2p()

# 이미지 폴더 경로
image_dir = r"C:\Users\Admin\Desktop\OCRImage"
output_file = "labels_1.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg"):
            name_without_ext = os.path.splitext(filename)[0]  # 예: 109서4180
            # 한글 부분만 영어 발음으로 변환
            romanized = g2p(name_without_ext)
            f.write(f"{romanized}.jpg {name_without_ext}\n")
