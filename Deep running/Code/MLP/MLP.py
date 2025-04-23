# TensorFlow 라이브러리 import (딥러닝 프레임워크)
import tensorflow as tf

# =====================================================
# 🧠 MLP 클래스 (다층 퍼셉트론)
# - 은닉층 구조와 출력 노드 수를 유연하게 지정 가능
# - 이진 분류 문제 또는 간단한 논리 연산 학습에 사용
# =====================================================
class MLP:
    # --------------------------------------------
    # 🔧 클래스 초기화
    # - hidden_layer_conf: 은닉층 노드 수 리스트 (예: [4, 5])
    # - num_output_nodes: 출력층 노드 수 (예: 1 = 이진 분류)
    # --------------------------------------------
    def __init__(self, hidden_layer_conf, num_output_nodes):
        self.hidden_layer_conf = hidden_layer_conf          # 은닉층 구성 정보 저장
        self.num_output_nodes = num_output_nodes            # 출력 노드 수
        self.logic_op_model = None                          # 모델 구조 저장 변수 (Keras 모델)

    # --------------------------------------------
    # 🧱 모델 구성 함수
    # - 입력층 → 은닉층(들) → 출력층 구조 정의
    # --------------------------------------------
    def build_model(self):
        # ✅ 입력층: 특성 2개를 받는 벡터 입력 (예: [x1, x2])
        input_layer = tf.keras.Input(shape=[2, ])

        # 은닉층 구성 준비 (입력부터 시작)
        hidden_layers = input_layer

        # ✅ 은닉층 구성: hidden_layer_conf에 따라 반복 생성
        if self.hidden_layer_conf is not None:
            for num_hidden_nodes in self.hidden_layer_conf:
                hidden_layers = tf.keras.layers.Dense(
                    units=num_hidden_nodes,                     # 해당 층의 노드 수
                    activation=tf.keras.activations.sigmoid,    # sigmoid 활성화 함수 사용
                    use_bias=True                               # bias 항 포함
                )(hidden_layers)  # 이전 층의 출력 → 현재 층의 입력

        # ✅ 출력층 구성
        output = tf.keras.layers.Dense(
            units=self.num_output_nodes,                  # 출력 노드 수 (예: 1)
            activation=tf.keras.activations.sigmoid,      # sigmoid 사용 (이진 확률 출력)
            use_bias=True
        )(hidden_layers)

        # ✅ 모델 정의: 입력 → 출력 구조로 연결
        self.logic_op_model = tf.keras.Model(inputs=input_layer, outputs=output)

        # ✅ 옵티마이저: SGD (확률적 경사 하강법), 학습률 0.1
        sgd = tf.keras.optimizers.SGD(learning_rate=0.1)

        # ✅ 손실 함수: MSE (Mean Squared Error, 평균제곱오차)
        self.logic_op_model.compile(optimizer=sgd, loss="mse")

    # --------------------------------------------
    # 🏋️ 모델 학습 함수
    # - 입력 x, 정답 y를 주고 반복적으로 학습 진행
    # --------------------------------------------
    def fit(self, x, y, batch_size, epochs):
        self.logic_op_model.fit(
            x=x,                      # 학습 데이터 입력
            y=y,                      # 정답 라벨
            batch_size=batch_size,    # 한 번에 학습할 데이터 수
            epochs=epochs             # 전체 학습 반복 횟수
        )

    # --------------------------------------------
    # 🔍 예측 함수
    # - 입력 데이터를 기반으로 예측 결과 출력 (확률 또는 레이블)
    # --------------------------------------------
    def predict(self, x, batch_size):
        prediction = self.logic_op_model.predict(x=x, batch_size=batch_size)
        return prediction  # 예측 결과 반환 (sigmoid 확률값)
