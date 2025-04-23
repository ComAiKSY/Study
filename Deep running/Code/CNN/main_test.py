# TensorFlow 라이브러리 임포트 (딥러닝을 위한 핵심 프레임워크)
import tensorflow as tf

# MNIST 데이터를 불러오기 위한 사용자 정의 클래스
from MNISTData import MNISTData

# AutoEncoder 모델 클래스 임포트
from AutoEncoder import AutoEncoder

# 수치 계산을 위한 NumPy
import numpy as np

# 메인 실행 블록
if __name__ == "__main__":
    print("Hi, I am an AutoEncoder Tester")  # 실행 시작 메시지 출력

    # 학습 관련 하이퍼파라미터 설정 (실제로는 사용 안됨, 참고용)
    batch_size = 32
    num_epochs = 5

    # ------------------------------
    # 📦 1. 데이터 로드
    # ------------------------------
    data_loader = MNISTData()         # MNIST 데이터 처리 객체 생성
    data_loader.load_data()           # MNIST 데이터셋 로드 및 전처리
    x_train = data_loader.x_train     # 학습용 이미지 데이터
    input_output_dim = data_loader.in_out_dim  # 입력/출력 차원 (784)

    # ------------------------------
    # 🧠 2. AutoEncoder 모델 구성
    # ------------------------------
    auto_encoder = AutoEncoder()      # AutoEncoder 객체 생성
    auto_encoder.build_model()        # 인코더 + 디코더 구조 생성 및 컴파일

    # ------------------------------
    # 💾 3. 모델 가중치 로딩
    # ------------------------------
    load_path = "./model/ae_model.weights.h5"  # 저장된 가중치 파일 경로
    print("load model weights from %s" % load_path)
    auto_encoder.load_weights(load_path)       # 저장된 가중치 불러오기

    # ------------------------------
    # 🔍 4. 테스트 데이터 선택
    # ------------------------------
    num_test_items = 56                                           # 테스트할 샘플 수
    test_data = data_loader.x_test[0:num_test_items, :]           # 테스트 입력 데이터
    test_label = data_loader.y_test[0:num_test_items]             # 테스트 라벨
    test_data_x_print = test_data.reshape(num_test_items,         # 시각화를 위한 2D 형태
                                          data_loader.width,
                                          data_loader.height)

    # ------------------------------
    # 🖼️ 5. AutoEncoder를 통한 복원 결과 시각화
    # ------------------------------
    print("const by codes")                                       # 안내 메시지
    reconst_data = auto_encoder.en_decoder.predict(test_data)     # AutoEncoder로 복원 수행
    reconst_data_x_print = reconst_data.reshape(                  # 이미지 형태로 변환
        num_test_items, data_loader.width, data_loader.height)

    # 복원된 이미지에 시그모이드 적용 (0~1 사이로 스케일링)
    recosnt_data_x_print = tf.math.sigmoid(reconst_data_x_print)

    # 원본 이미지와 복원 이미지 나란히 시각화 출력 (MNISTData 클래스 내 함수)
    MNISTData.print_56_pair_images(test_data_x_print,
                                   reconst_data_x_print,
                                   test_label)

    # ------------------------------
    # 🎯 6. 클래스별 평균 latent vector → 복원 이미지
    # ------------------------------
    print("const by code means for each digit")  # 안내 메시지

    avg_codes = np.zeros([10, 32])         # 0~9 숫자별 평균 latent vector 저장용 (32차원)
    avg_add_cnt = np.zeros([10])           # 각 숫자가 몇 번 나왔는지 카운트

    # 각 테스트 이미지에 대해 인코더를 통과시켜 latent vector 추출
    latent_vecs = auto_encoder.encoder.predict(test_data)

    # 숫자별 latent vector 평균 계산
    for i, label in enumerate(test_label):
        avg_codes[label] += latent_vecs[i]      # 해당 숫자에 해당하는 벡터 누적
        avg_add_cnt[label] += 1.0               # 등장 횟수 증가

    # 숫자별 평균 벡터 계산 (나누기)
    for i in range(10):
        if avg_add_cnt[i] > 0.1:                # 등장한 경우에만 나누기 수행
            avg_codes[i] /= avg_add_cnt[i]      # 평균 계산

    # 평균 latent vector를 텐서로 변환
    avg_code_tensor = tf.convert_to_tensor(avg_codes)

    # 디코더를 통해 평균 벡터로 복원 이미지 생성
    reconst_data_by_vecs = auto_encoder.decoder.predict(avg_code_tensor)

    # 시각화를 위한 이미지 형태로 reshape
    reconst_data_x_by_mean_print = reconst_data_by_vecs.reshape(
        10, data_loader.width, data_loader.height)

    # 숫자 라벨 리스트 (0~9)
    label_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 평균 코드로 복원된 10개의 숫자 이미지 시각화 출력
    MNISTData.print_10_images(reconst_data_x_by_mean_print, label_list)
