# TensorFlow는 딥러닝을 위한 대표적인 라이브러리
import tensorflow as tf

# matplotlib는 이미지 등 시각화를 위한 라이브러리
import matplotlib.pyplot as plt

# 우리가 만든 MLP 기반 이미지 분류기 클래스 가져오기
from ImageClassifier_MLP import ImageClassifier_MLP

# ===============================================
# 🎬 전체 실행 함수 정의: 데이터 로딩 → 모델 학습 → 예측 시각화까지 전과정 수행
# ===============================================
def run_classifier():
    # ---------------------------------------------
    # 1. Fashion MNIST 데이터셋 불러오기
    # - tf.keras에서 제공하는 28x28 흑백 의류 이미지 분류 데이터셋
    # ---------------------------------------------
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    # 라벨 인덱스에 대응되는 실제 클래스 이름 (총 10개)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    # 데이터셋의 구조 및 라벨 정보 출력 (디버깅용)
    print("Train data Shape")
    print(train_images.shape)   # (60000, 28, 28)
    print("Train data labels")
    print(train_labels)         # 예: [9, 0, 0, 3, 0, ...]
    print("Test data shape")
    print(test_images.shape)    # (10000, 28, 28)
    print("Test data labels")
    print(test_labels)

    # ---------------------------------------------
    # 1-1. 첫 번째 이미지 출력해보기 (샘플 확인)
    # ---------------------------------------------
    plt.figure()
    plt.imshow(train_images[0])     # 2D 이미지 출력
    plt.colorbar()                  # 픽셀 강도 값 범례
    plt.grid(False)
    plt.show()

    # ---------------------------------------------
    # 2. 이미지 정규화: 픽셀값 [0~255] → [0.0~1.0]
    # - 학습 안정성 및 속도 향상을 위해 필수 전처리
    # ---------------------------------------------
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # ---------------------------------------------
    # 2-1. 여러 이미지 확인: 훈련용 이미지 25장 시각화
    # ---------------------------------------------
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([]); plt.yticks([]); plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)  # 흑백으로 표시
        plt.xlabel(class_names[train_labels[i]])         # 정답 클래스 이름 표시
    plt.show()

    ##### classifier train and predict - begin

    # ---------------------------------------------
    # 3. MLP 분류기 인스턴스 생성
    # - 입력 이미지 크기와 클래스 수 지정
    # ---------------------------------------------
    my_classifier = ImageClassifier_MLP(img_shape_x=28, img_shape_y=28, num_labels=10)

    # ---------------------------------------------
    # 4. 라벨을 One-hot 인코딩 형식으로 변환
    # - [3] → [0,0,0,1,0,0,0,0,0,0]
    # - softmax + categorical crossentropy 조합에 필수
    # ---------------------------------------------
    train_labels_onehot = my_classifier.to_onehotvec_label(train_labels, dim=10)
    test_labels_onehot = my_classifier.to_onehotvec_label(test_labels, dim=10)

    # ---------------------------------------------
    # 5. MLP 모델 구성 및 컴파일
    # - Flatten → Dense → Dense → Softmax
    # ---------------------------------------------
    my_classifier.build_MLP_model()

    # ---------------------------------------------
    # 6. 학습 수행
    # - 입력 이미지 + One-hot 라벨로 학습 진행
    # ---------------------------------------------
    my_classifier.fit(
        train_imgs=train_images,
        train_labels=train_labels_onehot,
        num_epochs=10
    )

    # ---------------------------------------------
    # 7. 예측 수행
    # - 테스트 이미지에 대해 softmax 확률 예측
    # ---------------------------------------------
    predicted_logits = my_classifier.predict(test_imgs=test_images)

    # 확률 중 가장 큰 인덱스를 선택 → 최종 예측 클래스
    predicted_labels = tf.math.argmax(input=predicted_logits, axis=1)

    # ---------------------------------------------
    # 8. 예측 결과 시각화 (테스트 이미지 25개)
    # ---------------------------------------------
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([]); plt.yticks([]); plt.grid(False)
        plt.imshow(test_images[i], cmap=plt.cm.binary)  # 흑백 이미지 출력
        plt.xlabel(class_names[predicted_labels[i]])     # 예측된 클래스 이름 출력
    plt.show()

    ##### classifier train and predict - end

# ---------------------------------------------
# 🏁 스크립트 직접 실행 시 run_classifier() 함수 실행
# ---------------------------------------------
if __name__ == "__main__":
    run_classifier()
