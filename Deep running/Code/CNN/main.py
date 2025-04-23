# ================================
# 📦 학습 스크립트 (AutoEncoder 학습용)
# ================================

# MNIST 데이터셋을 로딩하고 전처리하는 사용자 정의 클래스 임포트
from MNISTData import MNISTData

# AutoEncoder 모델 클래스 임포트
from AutoEncoder import AutoEncoder

# Python의 메인 실행부
# 👉 이 코드는 파일을 직접 실행할 때만 아래 블록이 실행됨
if __name__ == "__main__":
    # 실행 안내 메시지
    print("Hi, I am an Auto Encoder Trainer.")

    # --------------------------------------
    # 🛠️ 학습 설정: 하이퍼파라미터 정의
    # --------------------------------------
    batch_size = 32    # 학습 시 한 번에 처리할 데이터 수
    num_epochs = 5     # 전체 학습 반복 횟수

    # --------------------------------------
    # 📥 데이터셋 로드
    # --------------------------------------
    data_loader = MNISTData()        # MNIST 데이터를 불러올 객체 생성
    data_loader.load_data()          # 내부적으로 x_train, x_test 등 준비됨

    # 학습에 사용할 데이터 변수로 추출
    x_train = data_loader.x_train              # 28x28 → 784로 벡터화된 이미지 데이터
    input_output_dim = data_loader.in_out_dim  # 입력/출력 차원 수 (784)

    # --------------------------------------
    # 🧠 AutoEncoder 모델 구성
    # --------------------------------------
    auto_encoder = AutoEncoder()        # AutoEncoder 클래스 객체 생성
    auto_encoder.build_model()          # 인코더 + 디코더 구조 설계 및 컴파일

    # --------------------------------------
    # 🔁 모델 학습
    # --------------------------------------
    # 오토인코더는 입력 = 출력 구조로 학습됨 (복원 학습)
    auto_encoder.fit(
        x=x_train,                     # 입력 데이터
        y=x_train,                     # 출력 데이터 (입력과 동일)
        batch_size=batch_size,
        epochs=num_epochs
    )

    # --------------------------------------
    # 💾 학습된 모델 가중치 저장
    # --------------------------------------
    save_path = "./model/ae_model.weights.h5"   # 저장 파일 경로 지정
    auto_encoder.save_weights(save_path)        # 모델 가중치 저장

    # 저장 완료 메시지 출력
    print("load model weights from %s" % save_path)
