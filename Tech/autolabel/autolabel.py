import os

dict_map = {
    'gyeongnam': '경남', 'busan': '부산', 'jeo': '저', 'meo': '머', 'seo': '서', 'beo': '버',
    'geo': '거', 'neo': '너', 'deo': '더', 'bu': '부', 'do': '도', 'no': '노', 'go': '고', 'ro': '로', 'bo': '보', 'jo': '조',
    'gu': '구', 'na': '나', 'ma': '마', 'ba': '바', 'sa': '사', 'ah': '아', 'ja': '자', 'cha': '차', 'ka': '카',
    'ta': '타', 'pa': '파', 'ha': '하', 'la': '라', 'ra': '라', 'me': '머', 'mu': '무', 'su': '수',
    'ho': '호', 'ru': '루', 'mo': '모', 'ke': '커', 'ne': '네', 'je': '제', 'yu': '유',
    'se': '서', 'mi': '미', 'ju': '주', 'de': '데', 'oe': '외', 'wa': '와', 'wi': '위', 'ri': '리', 'ye': '예',
    'yi': '이', 'u': '우', 'eo': '어', 'heo': '허', 'du': '두', 'leo': '러', 'lu': '루', 'so': '소', 'da': '다',
    'lo': '로', 'nu': '누', 'o': '오', 'ga': '가'
}

# 역맵핑 (한글 → 영어)
reverse_map = {}
for k, v in dict_map.items():
    if v not in reverse_map or len(k) > len(reverse_map[v]):
        reverse_map[v] = k

def convert_korean_to_romanized(name):
    for korean, roman in sorted(reverse_map.items(), key=lambda x: -len(x[0])):
        name = name.replace(korean, roman)
    return name

def rename_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if not os.path.isfile(old_path):
            continue
        name, ext = os.path.splitext(filename)
        new_name = convert_korean_to_romanized(name) + ext
        new_path = os.path.join(folder_path, new_name)
        if old_path != new_path:
            print(f"Renaming: {filename} -> {new_name}")
            os.rename(old_path, new_path)

# 사용 예시
folder = "C:/Users/Admin/Desktop/OCRImage"  # 실제 이미지 폴더 경로로 변경
rename_files_in_folder(folder)
