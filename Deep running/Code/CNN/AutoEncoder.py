# TensorFlow 임포트 (딥러닝 프레임워크의 핵심 라이브러리)
import tensorflow as tf

# Intel MKL 관련 충돌 방지를 위한 환경 설정 (윈도우에서 오류 방지용)
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# ========================================================
# 🧠 AutoEncoder 클래스 정의
# - 입력 데이터를 압축(Encode)했다가 다시 복원(Decode)하는 신경망 구조
# - 특징 학습, 노이즈 제거, 차원 축소 등 다양한 용도로 사용됨
# ========================================================
class AutoEncoder:
    def __init__(self):
        # 모델 구성 요소 초기화 (나중에 build_model()에서 채워짐)
        self.encoder = None          # 입력 → 잠재벡터로 변환하는 모델
        self.decoder = None          # 잠재벡터 → 복원된 출력으로 변환하는 모델
        self.en_decoder = None       # encoder + decoder 전체 AutoEncoder

        # 자주 쓰는 활성화 함수 저장
        self.relu = tf.keras.activations.relu   # 은닉층에 많이 사용됨 (양수만 활성화)
        self.tanh = tf.keras.activations.tanh   # 잠재공간에 많이 사용됨 ([-1, 1] 범위)

        # 입력 이미지 크기 (MNIST 기준 28x28 = 784차원 벡터)
        self.input_output_dim = 784

        # 은닉층 노드 수 설정 (자유롭게 바꿀 수 있음)
        self.encoder_hidden_layers = [200, 200]  # 인코더 히든레이어 구성
        self.decoder_hidden_layers = [200, 200]  # 디코더 히든레이어 구성

        # 잠재공간(latent space) 차원 수 → 이걸 압축된 벡터로 사용
        self.code_dim = 32

    # ===================================================
    # 📦 모델 구성 함수: 인코더 + 디코더 + 전체 오토인코더 정의
    # ===================================================
    def build_model(self):
        # -----------------------------
        # 1. 인코더 구성 (입력 → 잠재공간 벡터)
        # -----------------------------
        encoder_input = tf.keras.layers.Input(shape=(self.input_output_dim,), dtype=tf.float32)

        # 히든 레이어 순차적으로 연결
        encoder_h_layer = encoder_input
        for dim in self.encoder_hidden_layers:
            encoder_h_layer = tf.keras.layers.Dense(
                units=dim,              # 각 레이어의 노드 수
                activation=self.relu,   # 활성화 함수: ReLU (비선형성 부여)
                use_bias=True
            )(encoder_h_layer)

        # 잠재벡터(code) 출력층: 압축 표현
        code = tf.keras.layers.Dense(
            units=self.code_dim,
            activation=self.tanh,       # tanh: -1 ~ 1 범위로 출력 제한
            use_bias=True
        )(encoder_h_layer)

        # 인코더 모델 생성
        self.encoder = tf.keras.models.Model(inputs=encoder_input, outputs=code)

        # -----------------------------
        # 2. 디코더 구성 (잠재벡터 → 복원된 출력)
        # -----------------------------
        decoder_input = tf.keras.layers.Input(shape=(self.code_dim,), dtype=tf.float32)

        # 히든 레이어 구성
        decoder_h_layer = decoder_input
        for dim in self.decoder_hidden_layers:
            decoder_h_layer = tf.keras.layers.Dense(
                units=dim,
                activation=self.relu,
                use_bias=True
            )(decoder_h_layer)

        # 출력층: 원래 입력과 같은 차원으로 복원 (비활성화함수 없음 → 연속값 그대로 출력)
        decoder_output = tf.keras.layers.Dense(
            units=self.input_output_dim,
            activation=None,           # 회귀 문제이므로 출력값에 활성화 함수 없음
            use_bias=True
        )(decoder_h_layer)

        # 디코더 모델 생성
        self.decoder = tf.keras.models.Model(inputs=decoder_input, outputs=decoder_output)

        # -----------------------------
        # 3. 전체 AutoEncoder 연결 (Encoder → Decoder)
        # -----------------------------
        vae_output = self.decoder(code)  # 인코더의 출력(code)을 디코더에 바로 넣음
        self.en_decoder = tf.keras.models.Model(inputs=encoder_input, outputs=vae_output)

        # -----------------------------
        # 4. 학습 설정 (컴파일 단계)
        # -----------------------------
        optimizer_alg = tf.keras.optimizers.Adam(learning_rate=0.001)  # 학습 알고리즘 설정 (Adam)

        # 손실 함수: 평균 제곱 오차 (입력과 출력 간의 거리 계산)
        mse = tf.keras.losses.mse

        # 전체 모델 컴파일 (학습 준비 완료)
        self.en_decoder.compile(optimizer=optimizer_alg, loss=mse)

    # ===================================================
    # 🧪 모델 학습 함수
    # - 입력과 출력이 동일한 데이터를 이용해 AutoEncoder 학습
    # ===================================================
    def fit(self, x, y, batch_size, epochs):
        # x: 입력 이미지 (벡터화된 MNIST 등)
        # y: 출력 이미지 (오토인코더 특성상 입력과 동일함)
        self.en_decoder.fit(x=x, y=y, batch_size=batch_size, epochs=epochs)

    # ===================================================
    # 💾 가중치 저장 함수
    # - 학습된 모델의 가중치를 파일로 저장함
    # ===================================================
    def save_weights(self, save_path):
        self.en_decoder.save_weights(save_path)

    # ===================================================
    # 📂 가중치 불러오기 함수
    # - 저장된 모델 가중치를 로드하여 기존 모델에 적용
    # ===================================================
    def load_weights(self, load_path):
        self.en_decoder.load_weights(load_path)
