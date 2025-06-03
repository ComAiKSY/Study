import os

# 이미지가 저장된 디렉토리 경로
image_dir = r"C:\Users\Admin\Desktop\OCRImage"
# 출력할 txt 파일 이름
output_file = "labels.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg"):
            name_without_ext = os.path.splitext(filename)[0]
            f.write(f"{filename} {name_without_ext}\n")
