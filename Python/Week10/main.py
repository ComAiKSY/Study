# 시저 암호화 함수: 주어진 문자열을 알파벳 기준으로 일정 거리만큼 이동시켜 암호화
def caesar_cipher_encrypt(text, shift):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 대문자 알파벳 문자열
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"  # 소문자 알파벳 문자열
    encrypted_text = []  # 암호화된 문자들을 담을 리스트

    for char in text:  # 입력 문자열의 각 문자에 대해
        if char.isupper():  # 대문자인 경우
            index = alphabet_upper.index(char)  # 현재 문자의 인덱스 찾기
            shifted_index = (index + shift) % 26  # 이동 후 인덱스 (알파벳 범위 내 순환)
            encrypted_text.append(alphabet_upper[shifted_index])  # 이동된 대문자 추가
        elif char.islower():  # 소문자인 경우
            index = alphabet_lower.index(char)  # 현재 문자의 인덱스 찾기
            shifted_index = (index + shift) % 26  # 이동 후 인덱스
            encrypted_text.append(alphabet_lower[shifted_index])  # 이동된 소문자 추가
        else:
            encrypted_text.append(char)  # 알파벳이 아닌 문자는 그대로 추가 (예: 공백, 특수문자 등)

    return ''.join(encrypted_text)  # 문자 리스트를 문자열로 합쳐 반환

# 테스트 실행
plain_text = "Hello, World!"  # 암호화할 원본 문자열
shift_value = 3  # 알파벳 이동 거리
encrypted_text = caesar_cipher_encrypt(plain_text, shift_value)
print(f"{encrypted_text}")  # 출력: Khoor, Zruog!
