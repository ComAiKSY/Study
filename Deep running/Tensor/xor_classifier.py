import tensorflow as tf
from MLP import MLP

def xor_classifier_example():
    # XOR 입력 데이터 정의
    input_data = tf.constant([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
    input_data = tf.cast(input_data, tf.float32)

    # XOR 정답 레이블 정의
    xor_labels = tf.constant([[0.0], [1.0], [1.0], [0.0]])  # 2D 형태로 변환
    xor_labels = tf.cast(xor_labels, tf.float32)

    # 학습 파라미터 설정
    batch_size = 1
    epochs = 1500

    # MLP 모델 생성 및 학습
    mlp_classifier = MLP(hidden_layer_conf=[4], num_output_nodes=1)  # 은닉층 노드 4개
    mlp_classifier.build_model()
    mlp_classifier.fit(x=input_data, y=xor_labels, batch_size=batch_size, epochs=epochs)

    # XOR 예측 수행
    prediction = mlp_classifier.predict(x=input_data, batch_size=batch_size)

    # 결과 출력
    print("====== MLP XOR Classifier Result =====")
    for i in range(len(input_data)):
        x1, x2 = input_data[i].numpy()
        y_pred = prediction[i][0]
        predicted_label = 1 if y_pred > 0.5 else 0
        print(f"{int(x1)} XOR {int(x2)} => {y_pred:.2f} => {predicted_label}")

# Entry point
if __name__ == '__main__':
    xor_classifier_example()
