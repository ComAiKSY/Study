# TensorFlow와 NumPy 라이브러리 임포트
import tensorflow as tf   # 딥러닝 모델 생성, 학습, 평가를 위한 라이브러리
import numpy as np        # 수학 연산 및 배열 처리 라이브러리

# ============================================
# 🧠 ImageClassifier_MLP 클래스
# - MLP(Multi-Layer Perceptron) 구조로 이미지 분류
# - 입력 이미지를 flatten 후 은닉층 2개를 거쳐 softmax로 클래스 분류
# ============================================
class ImageClassifier_MLP:
    # ------------------------------------------
    # 🔧 초기화 함수
    # - 입력 이미지 크기(x, y)와 라벨 수(num_labels)를 받음
    # ------------------------------------------
    def __init__(self, img_shape_x, img_shape_y, num_labels):
        self.img_shape_x = img_shape_x       # 이미지 가로 크기
        self.img_shape_y = img_shape_y       # 이미지 세로 크기
        self.num_labels = num_labels         # 분류할 클래스 수
        self.classifier = None               # MLP 모델 (추후 build_MLP_model에서 생성됨)

    # ------------------------------------------
    # 🏋️ 모델 학습 함수
    # ------------------------------------------
    def fit(self, train_imgs, train_labels, num_epochs):
        # 입력 이미지와 라벨을 주어진 에폭 수만큼 학습
        self.classifier.fit(train_imgs, train_labels, epochs=num_epochs)

    # ------------------------------------------
    # 🔍 예측 함수
    # ------------------------------------------
    def predict(self, test_imgs):
        # 테스트 이미지에 대한 softmax 분류 결과 (확률 벡터) 반환
        prediction = self.classifier.predict(test_imgs)
        return prediction

    # ------------------------------------------
    # 🧱 MLP 모델 구성 함수
    # - Flatten → Dense(128) → Dense(128) → Dense(num_labels)
    # ------------------------------------------
    def build_MLP_model(self):
        # ✅ 입력층: 이미지 크기에 맞는 텐서 (예: 28x28)
        input_layer = tf.keras.layers.Input(shape=[self.img_shape_x, self.img_shape_y])

        # ✅ 평탄화 (Flatten): 2D → 1D (예: 28x28 → 784)
        flatten_layer = tf.keras.layers.Flatten()(input_layer)

        # ✅ 은닉층 활성화 함수 (ReLU)
        ac_func_relu = tf.keras.activations.relu

        # ✅ 첫 번째 은닉층 (128 노드, ReLU)
        hidden_layer_1 = tf.keras.layers.Dense(units=128, activation=ac_func_relu)(flatten_layer)

        # ✅ 두 번째 은닉층 (128 노드, ReLU)
        hidden_layer_2 = tf.keras.layers.Dense(units=128, activation=ac_func_relu)(hidden_layer_1)

        # ✅ 출력층 활성화 함수 (Softmax → 다중 클래스 분류)
        ac_func_softmax = tf.keras.activations.softmax

        # ✅ 출력층: 클래스 수 만큼 노드 (softmax로 확률값 출력)
        output_layer = tf.keras.layers.Dense(units=self.num_labels, activation=ac_func_softmax)(hidden_layer_2)

        # ✅ 전체 모델 구성 (입력 → 은닉층들 → 출력층)
        classifier_model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

        # ✅ 옵티마이저 설정: Adam (학습률 0.001)
        opt_alg = tf.keras.optimizers.Adam(learning_rate=0.001)

        # ✅ 손실 함수: categorical crossentropy (softmax일 때)
        loss_cross_e = tf.keras.losses.CategoricalCrossentropy(from_logits=False)

        # ✅ 모델 컴파일: 손실 함수, 옵티마이저, 정확도 지표 설정
        classifier_model.compile(optimizer=opt_alg, loss=loss_cross_e, metrics=['accuracy'])

        # ✅ 모델을 클래스 내부에 저장
        self.classifier = classifier_model

    # ------------------------------------------
    # 🔁 라벨을 One-hot 벡터로 변환하는 정적 메서드
    # 예: [2, 0, 1] → [[0,0,1], [1,0,0], [0,1,0]]
    # ------------------------------------------
    @staticmethod
    def to_onehotvec_label(index_labels, dim):
        # index_labels: 정수 라벨 리스트 (예: [0, 1, 2, 3, ...])
        # dim: 전체 클래스 수 (예: 10)

        num_labels = len(index_labels)  # 샘플 수
        # 모두 0으로 초기화된 배열 생성 (샘플 수 x 클래스 수)
        onehotvec_labels = np.zeros((num_labels, dim))

        # 정답 인덱스 위치에만 1.0 설정
        for i, idx in enumerate(index_labels):
            onehotvec_labels[i][idx] = 1.0

        # NumPy 배열을 TensorFlow 텐서로 변환
        onehotvec_labels_tf = tf.convert_to_tensor(onehotvec_labels)

        return onehotvec_labels_tf  # 변환된 One-hot 텐서 반환
