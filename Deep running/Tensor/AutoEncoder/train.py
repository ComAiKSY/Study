from MNISTData import MNISTData
from AutoEncoder import AutoEncoder
import numpy as np
import os

# 노이즈 추가 함수
def add_noise(x, drop_prob=0.5):
    noise = np.random.binomial(1, 1 - drop_prob, x.shape)
    return x * noise

if __name__ == "__main__":
    print("== Denoising AutoEncoder 학습 시작 ==")
    
    # 학습 설정
    batch_size = 32
    num_epochs = 10  # 자유롭게 변경 가능
    noise_prob = 0.5
    model_dir = "./model"
    os.makedirs(model_dir, exist_ok=True)
    save_path = os.path.join(model_dir, "dae_model.weights.h5")

    # 데이터 불러오기
    data_loader = MNISTData()
    data_loader.load_data()
    x_train = data_loader.x_train

    # 노이즈 추가
    x_train_noised = add_noise(x_train, drop_prob=noise_prob)

    # 모델 구성 및 학습
    auto_encoder = AutoEncoder()
    auto_encoder.build_model()
    auto_encoder.fit(x=x_train_noised, y=x_train, batch_size=batch_size, epochs=num_epochs)

    # 가중치 저장
    auto_encoder.save_weights(save_path)
    print("모델 가중치 저장 완료:", save_path)
