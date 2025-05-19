import numpy as np
import tensorflow as tf
from MNISTData import MNISTData
from AutoEncoder import AutoEncoder
import os

# 노이즈 추가 함수
def add_noise(x, drop_prob=0.5):
    noise = np.random.binomial(1, 1 - drop_prob, x.shape)
    return x * noise

if __name__ == "__main__":
    print("== Denoising AutoEncoder 테스트 ==")

    # 설정
    model_path = "./model/dae_model.weights.h5"
    noise_prob = 0.5

    # === 데이터 불러오기 ===
    data_loader = MNISTData()
    data_loader.load_data()
    x_test = data_loader.x_test
    y_test = data_loader.y_test

    # === 모델 로드 ===
    auto_encoder = AutoEncoder()
    auto_encoder.build_model()
    auto_encoder.load_weights(model_path)

    # ---------------------------------------
    # [2번] 56개 테스트 데이터로 노이즈 → 복원 → 시각화
    # ---------------------------------------
    print("== [2번] 노이즈 → 복원 이미지 시각화 ==")
    num_samples = 56
    x_vis = x_test[:num_samples]
    y_vis = y_test[:num_samples]

    x_vis_noised = add_noise(x_vis, drop_prob=noise_prob)
    x_vis_noised_img = x_vis_noised.reshape(num_samples, data_loader.width, data_loader.height)

    x_reconstructed = auto_encoder.en_decoder.predict(x_vis_noised)
    x_reconstructed_img = x_reconstructed.reshape(num_samples, data_loader.width, data_loader.height)
    x_reconstructed_img = tf.math.sigmoid(x_reconstructed_img)

    MNISTData.print_56_pair_images(x_vis_noised_img, x_reconstructed_img.numpy(), y_vis)

    # ---------------------------------------
    # [3번] 클래스별 평균 코드 → 복원 → 시각화
    # ---------------------------------------
    print("== [3번] 숫자별 평균 코드로 생성된 이미지 시각화 ==")
    num_for_avg = 1000
    x_avg = x_test[:num_for_avg]
    y_avg = y_test[:num_for_avg]

    latent_vecs = auto_encoder.encoder.predict(x_avg)

    code_dim = latent_vecs.shape[1]
    avg_codes = np.zeros((10, code_dim))
    count_per_class = np.zeros(10)

    for i, label in enumerate(y_avg):
        avg_codes[label] += latent_vecs[i]
        count_per_class[label] += 1

    for i in range(10):
        if count_per_class[i] > 0:
            avg_codes[i] /= count_per_class[i]

    decoded_imgs = auto_encoder.decoder.predict(avg_codes)
    decoded_imgs = decoded_imgs.reshape(10, data_loader.width, data_loader.height)
    decoded_imgs = tf.math.sigmoid(decoded_imgs)

    label_list = [str(i) for i in range(10)]
    MNISTData.print_10_images(decoded_imgs.numpy(), label_list)

    # ---------------------------------------
    # [4번] 평균 ± 표준편차 × 랜덤 → 숫자 5개씩 생성
    # ---------------------------------------
    print("== [4번] 숫자별 평균 코드 + 랜덤으로 생성된 이미지 시각화 ==")

    # 클래스별 표준편차 계산
    std_codes = np.zeros((10, code_dim))
    sum_sq_diff = np.zeros((10, code_dim))

    for i, label in enumerate(y_avg):
        diff = latent_vecs[i] - avg_codes[label]
        sum_sq_diff[label] += diff ** 2

    for i in range(10):
        if count_per_class[i] > 0:
            std_codes[i] = np.sqrt(sum_sq_diff[i] / count_per_class[i])

    # 각 클래스별로 5개 이미지 생성
    all_gen_imgs = []
    all_labels = []

    for digit in range(10):
        for j in range(5):
            rand_vec = np.random.uniform(-1, 1, size=code_dim)
            code_sample = avg_codes[digit] + std_codes[digit] * rand_vec
            img = auto_encoder.decoder.predict(code_sample.reshape(1, -1))
            img = img.reshape(data_loader.width, data_loader.height)
            img = tf.math.sigmoid(img)
            all_gen_imgs.append(img.numpy())
            all_labels.append(f"{digit}_{j+1}")

    all_gen_imgs = np.array(all_gen_imgs)

    # 시각화
    MNISTData.print_50_images(all_gen_imgs, all_labels)

    # ---------------------------------------
    # [5번] 평균 코드의 위치관계 T-SNE 시각화
    # ---------------------------------------
    print("== [5번] 평균 코드 T-SNE 시각화 ==")

    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt

    # T-SNE 적용
    tsne = TSNE(n_components=2, random_state=42, perplexity=5)
    tsne_result = tsne.fit_transform(avg_codes)  # shape: (10, 2)

    # 시각화
    plt.figure(figsize=(8, 6))
    for i in range(10):
        plt.scatter(tsne_result[i, 0], tsne_result[i, 1], label=str(i))
        plt.text(tsne_result[i, 0]+0.3, tsne_result[i, 1], str(i), fontsize=12)

    plt.title("T-SNE of Average Code Vectors by Class")
    plt.xlabel("TSNE-1")
    plt.ylabel("TSNE-2")
    plt.legend()
    plt.grid(True)
    plt.show()

