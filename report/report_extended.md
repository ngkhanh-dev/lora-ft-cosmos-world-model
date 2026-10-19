# Đánh giá mở rộng Base vs LoRA — Cosmos-Predict2

### Bảng 1 · Điểm từng video

| video | PSNR (dB) · Base | PSNR (dB) · LoRA | PSNR (dB) · Δ | SSIM · Base | SSIM · LoRA | SSIM · Δ | LPIPS · Base | LPIPS · LoRA | LPIPS · Δ | Latent L2 · Base | Latent L2 · LoRA | Latent L2 · Δ | I3D-L2 · Base | I3D-L2 · LoRA | I3D-L2 · Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | 14.0300 | 14.2364 | 0.2064 | 0.5516 | 0.5557 | 0.0041 | 0.3157 | 0.3023 | -0.0134 | 0.6198 | 0.6107 | -0.0092 | 33.3216 | 31.8741 | -1.4475 |
| 19 | 10.7198 | 10.6203 | -0.0995 | 0.3935 | 0.3943 | 0.0008 | 0.4208 | 0.4193 | -0.0014 | 0.8177 | 0.8218 | 0.0042 | 43.4392 | 42.2576 | -1.1816 |
| 60 | 11.3118 | 11.2961 | -0.0157 | 0.4184 | 0.4229 | 0.0045 | 0.4621 | 0.4529 | -0.0092 | 0.7893 | 0.7887 | -0.0006 | 40.6029 | 42.4969 | 1.8941 |
| 62 | 11.9911 | 11.9409 | -0.0502 | 0.4248 | 0.4253 | 0.0005 | 0.3695 | 0.3688 | -0.0007 | 0.7482 | 0.7518 | 0.0036 | 37.3943 | 38.1979 | 0.8036 |
| 64 | 12.8645 | 12.7201 | -0.1443 | 0.4604 | 0.4595 | -0.0009 | 0.3516 | 0.3553 | 0.0037 | 0.7178 | 0.7265 | 0.0086 | 39.2450 | 42.6775 | 3.4324 |
| 65 | 11.5081 | 11.6689 | 0.1608 | 0.4617 | 0.4637 | 0.0020 | 0.4341 | 0.4326 | -0.0016 | 0.8035 | 0.7936 | -0.0099 | 41.6958 | 42.6841 | 0.9883 |
| 98 | 11.2634 | 11.2991 | 0.0356 | 0.3742 | 0.3719 | -0.0023 | 0.3953 | 0.4064 | 0.0112 | 0.7654 | 0.7635 | -0.0019 | 40.7626 | 39.3517 | -1.4110 |
| 100 | 12.9284 | 12.8383 | -0.0901 | 0.4627 | 0.4655 | 0.0028 | 0.3569 | 0.3541 | -0.0027 | 0.6772 | 0.6801 | 0.0029 | 40.6656 | 38.0051 | -2.6605 |
| Trung bình | 12.0772 | 12.0775 | 0.0004 | 0.4434 | 0.4448 | 0.0014 | 0.3882 | 0.3865 | -0.0018 | 0.7424 | 0.7421 | -0.0003 | 39.6409 | 39.6931 | 0.0522 |

#### 📝 Đánh giá Bảng 1 — điểm từng video (ô xanh = bên tốt hơn trong cặp)
- **PSNR (dB)**: video khó nhất (theo Base) là `19` (10.720), dễ nhất là `9` (14.030). LoRA tốt hơn Base ở **3/8** video; cải thiện nhiều nhất ở `9` (+0.2064), tệ đi nhiều nhất ở `64` (-0.1443).
- **SSIM**: video khó nhất (theo Base) là `98` (0.3742), dễ nhất là `9` (0.5516). LoRA tốt hơn Base ở **6/8** video; cải thiện nhiều nhất ở `60` (+0.004465), tệ đi nhiều nhất ở `98` (-0.002302).
- **LPIPS**: video khó nhất (theo Base) là `60` (0.4621), dễ nhất là `9` (0.3157). LoRA tốt hơn Base ở **6/8** video; cải thiện nhiều nhất ở `9` (+0.01339), tệ đi nhiều nhất ở `98` (-0.01118).
- **Latent L2**: video khó nhất (theo Base) là `19` (0.8177), dễ nhất là `9` (0.6198). LoRA tốt hơn Base ở **4/8** video; cải thiện nhiều nhất ở `65` (+0.00994), tệ đi nhiều nhất ở `64` (-0.008645).
- **I3D-L2**: video khó nhất (theo Base) là `19` (43.439), dễ nhất là `9` (33.322). LoRA tốt hơn Base ở **4/8** video; cải thiện nhiều nhất ở `100` (+2.661), tệ đi nhiều nhất ở `64` (-3.432).
- **Nhận xét chung**: độ phân tán *giữa các video* lớn gấp **27–3026 lần** chênh lệch trung bình do LoRA gây ra ở mọi metric → điểm số chủ yếu do *độ khó của từng video* quyết định, chứ không phải do Base hay LoRA.

### Bảng 2 · Thống kê tổng hợp

| Metric | Run | Mean | Std | Median | Min | Max | Δ% so với Base |
|---|---|---|---|---|---|---|---|
| PSNR (dB) | Base | 12.0772 | 1.1071 | 11.7496 | 10.7198 | 14.0300 | – |
| PSNR (dB) | LoRA | 12.0775 | 1.1451 | 11.8049 | 10.6203 | 14.2364 | 0.0030 |
| SSIM | Base | 0.4434 | 0.0547 | 0.4426 | 0.3742 | 0.5516 | – |
| SSIM | LoRA | 0.4448 | 0.0561 | 0.4424 | 0.3719 | 0.5557 | 0.3238 |
| LPIPS | Base | 0.3882 | 0.0487 | 0.3824 | 0.3157 | 0.4621 | – |
| LPIPS | LoRA | 0.3865 | 0.0499 | 0.3876 | 0.3023 | 0.4529 | -0.4573 |
| Latent L2 | Base | 0.7424 | 0.0677 | 0.7568 | 0.6198 | 0.8177 | – |
| Latent L2 | LoRA | 0.7421 | 0.0688 | 0.7577 | 0.6107 | 0.8218 | -0.0382 |
| I3D-L2 | Base | 39.6409 | 3.0943 | 40.6342 | 33.3216 | 43.4392 | – |
| I3D-L2 | LoRA | 39.6931 | 3.7536 | 40.8046 | 31.8741 | 42.6841 | 0.1318 |

#### 📝 Đánh giá Bảng 2 — thống kê tổng hợp
- **PSNR (dB)**: Base 12.077 → LoRA 12.078 (Δ +0.0003658; LoRA tốt hơn 0.00% theo giá trị trung bình). Std giữa các video: 1.107 (Base) / 1.145 (LoRA) — LoRA phân tán hơn một chút.
- **SSIM**: Base 0.4434 → LoRA 0.4448 (Δ +0.001436; LoRA tốt hơn 0.32% theo giá trị trung bình). Std giữa các video: 0.05473 (Base) / 0.0561 (LoRA) — LoRA phân tán hơn một chút.
- **LPIPS**: Base 0.3882 → LoRA 0.3865 (Δ -0.001775; LoRA tốt hơn 0.46% theo giá trị trung bình). Std giữa các video: 0.04872 (Base) / 0.04992 (LoRA) — LoRA phân tán hơn một chút.
- **Latent L2**: Base 0.7424 → LoRA 0.7421 (Δ -0.0002839; LoRA tốt hơn 0.04% theo giá trị trung bình). Std giữa các video: 0.06765 (Base) / 0.06876 (LoRA) — LoRA phân tán hơn một chút.
- **I3D-L2**: Base 39.641 → LoRA 39.693 (Δ +0.05223; LoRA kém hơn 0.13% theo giá trị trung bình). Std giữa các video: 3.094 (Base) / 3.754 (LoRA) — LoRA phân tán hơn một chút.
- **Tóm lại**: xét riêng giá trị trung bình, LoRA nhỉnh hơn ở **4/5** metric. Trung bình chỉ là bước đầu — Bảng 3 mới cho biết khác biệt đó có vượt khỏi nhiễu giữa các video hay không.

### Bảng 3 · Kiểm định ghép cặp

| Metric | Base | LoRA | Δ (LoRA−Base) | CI95 thấp | CI95 cao | Δ % | LoRA thắng | p Wilcoxon | p t-test | d_z (>0: LoRA tốt) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSNR (dB) | 12.0772 | 12.0775 | 0.0004 | -0.0760 | 0.0827 | 0.0030 | 3/8 | 0.9453 | 0.9937 | 0.0029 | không có khác biệt rõ rệt |
| SSIM | 0.4434 | 0.4448 | 0.0014 | -0.0001 | 0.0029 | 0.3238 | 6/8 | 0.1953 | 0.1290 | 0.6083 | không có khác biệt rõ rệt |
| LPIPS | 0.3882 | 0.3865 | -0.0018 | -0.0065 | 0.0031 | -0.4573 | 6/8 | 0.4609 | 0.5224 | 0.2381 | không có khác biệt rõ rệt |
| Latent L2 | 0.7424 | 0.7421 | -0.0003 | -0.0046 | 0.0038 | -0.0382 | 4/8 | 1.0000 | 0.9058 | 0.0434 | không có khác biệt rõ rệt |
| I3D-L2 | 39.6409 | 39.6931 | 0.0522 | -1.2477 | 1.4238 | 0.1318 | 4/8 | 0.9453 | 0.9447 | -0.0254 | không có khác biệt rõ rệt |

#### 📝 Đánh giá Bảng 3 — Base vs LoRA có khác nhau thật không?
- **PSNR (dB)** → *không có khác biệt rõ rệt*. Δ = +0.0003658 (CI95 [-0.076, +0.0827], chứa 0), p Wilcoxon = 0.945, d_z = +0.00, LoRA thắng 3/8 video.
- **SSIM** → *không có khác biệt rõ rệt*. Δ = +0.001436 (CI95 [-0.0001307, +0.002925], chứa 0), p Wilcoxon = 0.195, d_z = +0.61, LoRA thắng 6/8 video.
- **LPIPS** → *không có khác biệt rõ rệt*. Δ = -0.001775 (CI95 [-0.006474, +0.003057], chứa 0), p Wilcoxon = 0.461, d_z = +0.24, LoRA thắng 6/8 video.
- **Latent L2** → *không có khác biệt rõ rệt*. Δ = -0.0002839 (CI95 [-0.004557, +0.003799], chứa 0), p Wilcoxon = 1.000, d_z = +0.04, LoRA thắng 4/8 video.
- **I3D-L2** → *không có khác biệt rõ rệt*. Δ = +0.05223 (CI95 [-1.248, +1.424], chứa 0), p Wilcoxon = 0.945, d_z = -0.03, LoRA thắng 4/8 video.
- **Tổng kết**: 0/5 metric có khác biệt đạt ý nghĩa thống kê (CI95 không chứa 0 và p Wilcoxon < 0.05); 0 metric trong đó nghiêng hẳn về LoRA.
- **Công suất kiểm định (n = 8 video)**: nửa độ rộng khoảng tin cậy t 95% của Δ là PSNR (dB) ±0.105, SSIM ±0.00197, LPIPS ±0.00624, Latent L2 ±0.00547, I3D-L2 ±1.72. Chênh lệch nhỏ hơn mức này không thể tách khỏi nhiễu giữa các video với 8 mẫu — nên 'không khác biệt rõ rệt' nghĩa là *chưa đủ bằng chứng*, không phải *chắc chắn bằng nhau*.

### Bảng 4 · FVD — backbone: I3D (Kinetics-400, torchscript StyleGAN-V)

| So sánh | FVD | CI95 thấp | CI95 cao | Số clip/tập | Chiều đặc trưng |
|---|---|---|---|---|---|
| Base ↔ GT | 731.7877 | 750.8368 | 1050.4326 | 160 | 400 |
| LoRA ↔ GT | 743.2240 | 754.6321 | 1072.6607 | 160 | 400 |
| Base ↔ LoRA (tham chiếu) | 291.2377 | 272.4966 | 471.7785 | 160 | 400 |

#### 📝 Đánh giá Bảng 4 — FVD (backbone: I3D (Kinetics-400, torchscript StyleGAN-V))
- **FVD(Base, GT) = 731.79**, **FVD(LoRA, GT) = 743.22** (thấp hơn = phân phối video sinh ra gần video thật hơn). Chênh lệch LoRA − Base = +11.44 (bootstrap theo video: CI95 [-54.84, +78.34]; LoRA có FVD thấp hơn Base trong 37% số lần resample) → **khoảng tin cậy chứa 0 → chưa đủ bằng chứng LoRA khác Base về FVD**.
- Khoảng cách Base↔LoRA = 291.24, bằng **0.39×** khoảng cách trung bình tới GT. Hai model sinh ra phân phối video gần nhau hơn nhiều so với GT → LoRA chưa dịch chuyển phân phối đầu ra đáng kể.
- **Lưu ý độ tin cậy**: chỉ có 8 video × 20 clip chồng lấp = 160 mẫu/tập nhưng đặc trưng 400 chiều → ma trận hiệp phương sai thiếu hạng, FVD bị chệch lên và *không so sánh được trực tiếp với con số FVD trong các bài báo*; chỉ nên dùng để so sánh tương đối Base vs LoRA trong cùng thiết lập này.

### Bảng 5 · Theo thời gian

| Metric | Đoạn | Base | LoRA | Cải thiện của LoRA |
|---|---|---|---|---|
| PSNR (dB) | Đầu 1/3 | 12.8519 | 12.8213 | -0.0306 |
| PSNR (dB) | Giữa 1/3 | 11.8751 | 11.9245 | 0.0494 |
| PSNR (dB) | Cuối 1/3 | 11.4854 | 11.4671 | -0.0183 |
| PSNR (dB) | Drift (cuối − đầu) | -1.3665 | -1.3542 | 0.0123 |
| SSIM* | Đầu 1/3 | 0.4199 | 0.4209 | 0.0010 |
| SSIM* | Giữa 1/3 | 0.4022 | 0.4037 | 0.0015 |
| SSIM* | Cuối 1/3 | 0.3920 | 0.3921 | 0.0001 |
| SSIM* | Drift (cuối − đầu) | -0.0280 | -0.0289 | -0.0009 |
| LPIPS | Đầu 1/3 | 0.3452 | 0.3429 | 0.0023 |
| LPIPS | Giữa 1/3 | 0.3959 | 0.3917 | 0.0043 |
| LPIPS | Cuối 1/3 | 0.4248 | 0.4261 | -0.0013 |
| LPIPS | Drift (cuối − đầu) | 0.0796 | 0.0832 | -0.0036 |
| Latent L2 | Đầu 1/3 | 0.6639 | 0.6621 | 0.0017 |
| Latent L2 | Giữa 1/3 | 0.7548 | 0.7525 | 0.0023 |
| Latent L2 | Cuối 1/3 | 0.8010 | 0.8041 | -0.0031 |
| Latent L2 | Drift (cuối − đầu) | 0.1371 | 0.1420 | -0.0048 |

#### 📝 Đánh giá Bảng 5 — sai số tăng dần theo thời gian (SSIM* = SSIM tính lại theo frame, chỉ dùng cho phân tích theo thời gian)
- **PSNR (dB)**: từ đoạn đầu đến đoạn cuối, Base xấu đi 1.366 và LoRA 1.354 (drift Base -1.366 / LoRA -1.354). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.0494) và nhỏ nhất/bất lợi nhất ở **Đầu 1/3** (-0.0306) (dương = LoRA tốt hơn).
- **SSIM***: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.02796 và LoRA 0.02885 (drift Base -0.02796 / LoRA -0.02885). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00152) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (+9.09e-05) (dương = LoRA tốt hơn).
- **LPIPS**: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.07957 và LoRA 0.08315 (drift Base +0.07957 / LoRA +0.08315). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00426) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (-0.00131) (dương = LoRA tốt hơn).
- **Latent L2**: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.1371 và LoRA 0.142 (drift Base +0.1371 / LoRA +0.142). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00232) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (-0.00309) (dương = LoRA tốt hơn).
- **Ý nghĩa**: nếu drift của LoRA nhỏ hơn Base thì LoRA giúp giữ chất lượng tốt hơn khi video dài ra (ít tích luỹ sai số); nếu hai drift gần như bằng nhau thì LoRA không cải thiện độ ổn định theo thời gian. Sai số tăng mạnh về cuối clip là đặc trưng của sinh video autoregressive/diffusion khi chỉ được điều kiện bằng 1 frame đầu.

### Bảng 6 · Thắng/thua theo video × metric

| video | PSNR (dB) | SSIM | LPIPS | Latent L2 | I3D-L2 | LoRA thắng | Base thắng |
|---|---|---|---|---|---|---|---|
| 9 | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | 5 | 0 |
| 19 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | LoRA ✓ | 3 | 2 |
| 60 | Base ✓ | LoRA ✓ | LoRA ✓ | ≈ | Base ✓ | 2 | 2 |
| 62 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | Base ✓ | 2 | 3 |
| 64 | Base ✓ | Base ✓ | Base ✓ | Base ✓ | Base ✓ | 0 | 5 |
| 65 | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | 4 | 1 |
| 98 | LoRA ✓ | Base ✓ | Base ✓ | LoRA ✓ | LoRA ✓ | 3 | 2 |
| 100 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | LoRA ✓ | 3 | 2 |
| LoRA - Base - hoà | 3 - 5 - 0 | 6 - 2 - 0 | 6 - 2 - 0 | 3 - 4 - 1 | 4 - 4 - 0 | 22 | 17 |

#### 📝 Đánh giá Bảng 6 — mức độ nhất quán giữa các metric
- Tổng cộng LoRA thắng **22** ô, Base thắng **17** ô trên 8×5 = 40 ô (còn lại là hoà trong ±0.1%).
- Video mà LoRA không thua ở metric nào: `9`. Video mà LoRA không thắng ở metric nào: `64`.
- **6/8** video cho kết quả *lẫn lộn* (có metric LoRA thắng, có metric Base thắng). Số video lẫn lộn lớn cho thấy các metric không đồng thuận — LoRA không cải thiện một cách nhất quán, và kết luận phụ thuộc vào metric được chọn.

### Bảng 7 · Tương quan Spearman giữa các metric

| index | PSNR (dB) | SSIM | LPIPS | Latent L2 | I3D-L2 |
|---|---|---|---|---|---|
| PSNR (dB) | 1.00 | 0.85 | 0.80 | 0.91 | 0.66 |
| SSIM | 0.85 | 1.00 | 0.57 | 0.63 | 0.42 |
| LPIPS | 0.80 | 0.57 | 1.00 | 0.88 | 0.65 |
| Latent L2 | 0.91 | 0.63 | 0.88 | 1.00 | 0.74 |
| I3D-L2 | 0.66 | 0.42 | 0.65 | 0.74 | 1.00 |

#### 📝 Đánh giá Bảng 7 — độ đồng thuận giữa các metric
- Cặp đồng thuận nhất: **PSNR (dB) – Latent L2** (ρ = +0.91); cặp ít đồng thuận nhất: **SSIM – I3D-L2** (ρ = +0.42). ρ dương nghĩa là video nào 'dễ' theo metric này cũng 'dễ' theo metric kia.
- Tương quan trung bình giữa các cặp: +0.71. Các metric xếp hạng video khá giống nhau → độ khó của video là yếu tố chung chi phối mọi metric.
- Lưu ý: chỉ 16 mẫu và 8 video lặp lại ở 2 model nên các mẫu không hoàn toàn độc lập; xem đây là mô tả, không phải kiểm định.

### Bảng 8 · Độ khác biệt giữa video Base và video LoRA

| video | PSNR(Base,LoRA) dB | MAE(Base,LoRA) /255 | Latent RMSE(Base,LoRA) |
|---|---|---|---|
| 9 | 19.2489 | 10.8927 | 0.3271 |
| 19 | 19.8464 | 10.2985 | 0.2781 |
| 60 | 20.0293 | 10.8914 | 0.2868 |
| 62 | 23.1917 | 7.3961 | 0.2045 |
| 64 | 24.5957 | 6.5691 | 0.1973 |
| 65 | 16.9155 | 17.2515 | 0.4066 |
| 98 | 16.7088 | 19.2506 | 0.4260 |
| 100 | 20.1951 | 10.8193 | 0.3008 |
| Trung bình | 20.0914 | 11.6712 | 0.3034 |

#### 📝 Đánh giá Bảng 8 — LoRA đã thay đổi đầu ra bao nhiêu?
- PSNR giữa video Base và video LoRA (cùng frame đầu, cùng prompt) trung bình **20.1 dB**, MAE trung bình 11.7/255. Để so sánh, PSNR của mỗi model so với ground-truth chỉ khoảng **12.1 dB**.
- Hai video Base/LoRA giống nhau *hơn nhiều* so với việc mỗi video giống GT → LoRA chỉ chỉnh nhẹ đầu ra; khoảng cách tới GT chủ yếu do giới hạn của cả mô hình (chuyển động robot, chi tiết vật thể, lệch thời gian/tốc độ khung hình), nên metric khó nhúc nhích.
- Trong không gian latent: khoảng cách Base↔LoRA = 0.303, so với khoảng cách tới GT ≈ 0.742.
- Video mà LoRA làm đầu ra thay đổi nhiều nhất là `98` (PSNR Base↔LoRA = 16.7 dB).

### Hình · Mức khác biệt Base ↔ LoRA

![fig_base_vs_lora_difference.png](fig_base_vs_lora_difference.png)

### Hình 1 · Từng video, Base vs LoRA

![fig1_per_video_dumbbell.png](fig1_per_video_dumbbell.png)

#### 📝 Đánh giá Hình 1
- **PSNR (dB)**: giá trị giữa các video trải trong khoảng 3.31 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.1 (trung bình tuyệt đối) = 3.0% độ trải đó.
- **SSIM**: giá trị giữa các video trải trong khoảng 0.1775 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00224 (trung bình tuyệt đối) = 1.3% độ trải đó.
- **LPIPS**: giá trị giữa các video trải trong khoảng 0.1465 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00548 (trung bình tuyệt đối) = 3.7% độ trải đó.
- **Latent L2**: giá trị giữa các video trải trong khoảng 0.1978 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00511 (trung bình tuyệt đối) = 2.6% độ trải đó.
- **I3D-L2**: giá trị giữa các video trải trong khoảng 10.12 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 1.73 (trung bình tuyệt đối) = 17.1% độ trải đó.
- **Cách đọc**: hai chấm gần nhau (đoạn nối ngắn) = LoRA gần như không đổi so với Base ở video đó. Thứ tự các video (video nào cao/thấp) gần như giống hệt giữa hai model → *nội dung video* quyết định điểm, không phải model.

### Hình 2 · Cải thiện của LoRA theo video

![fig2_improvement_per_video.png](fig2_improvement_per_video.png)

#### 📝 Đánh giá Hình 2
- **PSNR (dB)**: 3 cột xanh / 5 cột đỏ; trung bình +0.000366. Video LoRA giúp nhiều nhất `9` (+0.206), thiệt nhất `64` (-0.144). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **SSIM**: 6 cột xanh / 2 cột đỏ; trung bình +0.00144. Video LoRA giúp nhiều nhất `60` (+0.00447), thiệt nhất `98` (-0.0023). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **LPIPS**: 6 cột xanh / 2 cột đỏ; trung bình +0.00178. Video LoRA giúp nhiều nhất `9` (+0.0134), thiệt nhất `98` (-0.0112). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **Latent L2**: 4 cột xanh / 4 cột đỏ; trung bình +0.000284. Video LoRA giúp nhiều nhất `65` (+0.00994), thiệt nhất `64` (-0.00865). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **I3D-L2**: 4 cột xanh / 4 cột đỏ; trung bình -0.0522. Video LoRA giúp nhiều nhất `100` (+2.66), thiệt nhất `64` (-3.43). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **Cách đọc**: cột xanh và đỏ xen kẽ với biên độ gần như ngang nhau nghĩa là LoRA chỉ tạo *nhiễu* quanh 0 chứ không tạo cải thiện hệ thống.

### Hình 3 · Forest plot hiệu ứng

![fig3_forest_effect_sizes.png](fig3_forest_effect_sizes.png)

#### 📝 Đánh giá Hình 3
- Hiệu ứng chuẩn hoá lớn nhất là **SSIM** (d_z = +0.61; quy ước ~0.2 nhỏ, 0.5 vừa, 0.8 lớn). Mức thay đổi so với Base chỉ trong khoảng 0.00% – 0.46%.
- Các metric có CI95 (của Δ) chứa 0: PSNR (dB), SSIM, LPIPS, Latent L2, I3D-L2. Tất cả điểm xám đi qua đường 0 → LoRA chưa tạo ra khác biệt có thể đo được.
- Lưu ý: d_z từ 8 mẫu rất không ổn định (CI rộng) — hãy đọc xu hướng chung giữa các metric hơn là con số tuyệt đối.

### Hình 4 · Đường cong theo thời gian

![fig4_time_curves.png](fig4_time_curves.png)

#### 📝 Đánh giá Hình 4
- **PSNR (dB)**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 50% số mốc thời gian, |LoRA−Base| lớn nhất là 0.157. Cả hai đều xấu đi theo thời gian (từ 14.5 ở đầu đến 11.4 ở cuối với Base).
- **SSIM***: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 70% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00534. Cả hai đều xấu đi theo thời gian (từ 0.447 ở đầu đến 0.39 ở cuối với Base).
- **LPIPS**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 73% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00881. Cả hai đều xấu đi theo thời gian (từ 0.271 ở đầu đến 0.428 ở cuối với Base).
- **Latent L2**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 52% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00708. Cả hai đều xấu đi theo thời gian (từ 0.627 ở đầu đến 0.809 ở cuối với Base).
- **Cách đọc**: hàng dưới là chênh lệch LoRA − Base; nếu dải đen (±1.96 SEM) luôn chứa đường đỏ y = 0 thì không có thời điểm nào LoRA khác Base một cách đáng tin. Phần lớn sai số tích luỹ theo thời gian là của *cả hai* model, tức giới hạn của mô hình nền chứ không phải do LoRA.

### Hình 5 · Heatmap % cải thiện

![fig5_improvement_heatmap.png](fig5_improvement_heatmap.png)

#### 📝 Đánh giá Hình 5
- Ô có thay đổi lớn nhất: video `64` ở **I3D-L2** (-8.75%). Toàn bảng chỉ dao động trong ±8.75%.
- Hàng 'Trung bình' (dưới đường đen): PSNR (dB) -0.02%, SSIM +0.30%, LPIPS +0.50%, Latent L2 +0.05%, I3D-L2 -0.11%.
- **Cách đọc**: nếu một *hàng* (video) xanh đồng loạt thì LoRA giúp nhất quán video đó; nếu một *cột* (metric) xanh đồng loạt thì LoRA cải thiện metric đó. Mảng màu loang lổ xanh/đỏ xen kẽ = tác động không nhất quán.

### Hình 6 · Scatter Base vs LoRA

![fig6_base_vs_lora_scatter.png](fig6_base_vs_lora_scatter.png)

#### 📝 Đánh giá Hình 6
- **PSNR (dB)**: tương quan Base–LoRA r = 0.994; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **SSIM**: tương quan Base–LoRA r = 0.999; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **LPIPS**: tương quan Base–LoRA r = 0.989; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **Latent L2**: tương quan Base–LoRA r = 0.996; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **I3D-L2**: tương quan Base–LoRA r = 0.837; các điểm lệch khỏi đường chéo đáng kể → LoRA đổi thứ hạng một số video.
- **Cách đọc**: khoảng cách dọc từ điểm tới đường chéo = mức thay đổi do LoRA. Điểm xanh phía tốt, đỏ phía xấu; điểm càng xa đường chéo càng chịu tác động nhiều.

### Hình 7 · FVD

![fig7_fvd.png](fig7_fvd.png)

#### 📝 Đánh giá Hình 7
- Cột Base↔GT = 731.8, LoRA↔GT = 743.2; thanh sai số là CI95 bootstrap theo video — hai thanh chồng lấn mạnh.
- Histogram bên phải là phân phối của FVD(LoRA) − FVD(Base): CI95 = [-54.8, +78.3] → chứa 0 → chưa đủ bằng chứng LoRA khác Base về FVD.
- Cột tím (Base↔LoRA) = 291.2 cho biết hai model sinh ra phân phối khác nhau bao nhiêu; nếu nhỏ hơn nhiều hai cột còn lại thì LoRA chưa dịch chuyển đầu ra nhiều.
- FVD ở đây dựa trên rất ít video nên chỉ mang tính so sánh tương đối (xem lưu ý ở Bảng 4).

### Hình 8 · Tương quan metric

![fig8_metric_correlation.png](fig8_metric_correlation.png)

#### 📝 Đánh giá Hình 8
- Tương quan Spearman ngoài đường chéo nằm trong khoảng [+0.42, +0.91], trung bình +0.71.
- Ô xanh đậm = hai metric xếp hạng các (video, model) giống nhau; ô đỏ/nhạt = hai metric bất đồng, tức chúng đang bắt các khía cạnh chất lượng khác nhau. Vì vậy kết luận về LoRA nên dựa trên *nhiều* metric cùng lúc (Bảng 3, 6 và Hình 3) thay vì chỉ PSNR/SSIM.

### Hình 9 · So sánh trực quan 8 video

![fig9_qualitative_all8.png](fig9_qualitative_all8.png)

### Hình 10a · Diễn tiến theo thời gian (video 1-4)

![fig10a_strips_videos_1-4.png](fig10a_strips_videos_1-4.png)

### Hình 10b · Diễn tiến theo thời gian (video 5-8)

![fig10b_strips_videos_5-8.png](fig10b_strips_videos_5-8.png)

#### 📝 Đánh giá Hình 9–10
- Cột thứ 4 là hiệu tuyệt đối |LoRA − Base| khuếch đại ×5: vùng sáng là nơi LoRA thực sự vẽ khác Base. Trung bình chênh lệch pixel Base↔LoRA chỉ 11.7/255 (Bảng 8).
- ΔPSNR theo video dao động từ -0.14 dB (video `64`) đến +0.21 dB (video `9`).
- Quan sát bằng mắt nên tập trung vào: (1) cánh tay/bàn tay robot có đi đúng quỹ đạo như GT không, (2) vật thể bị gắp có giữ đúng hình dạng/màu không, (3) hậu cảnh có bị 'trôi' dần về cuối clip không. Ở các hàng của Hình 10, so sánh cột frame 92 (cuối clip) giữa GT, Base và LoRA — đây là chỗ sai khác tích luỹ rõ nhất.
- Lưu ý: GT gốc là 20 fps còn video sinh ra là 16 fps nhưng code gốc (và các metric ở đây) căn theo *chỉ số frame*, nên cùng một chỉ số frame có thể tương ứng hai thời điểm hơi khác nhau; điều này làm giảm PSNR/SSIM tuyệt đối của cả Base lẫn LoRA như nhau.

### Bảng 9 · Tổng hợp mọi metric

| Metric | Base | LoRA | Δ % | LoRA thắng | Kết luận |
|---|---|---|---|---|---|
| PSNR (dB) | 12.0772 | 12.0775 | 0.0030 | 3/8 | không có khác biệt rõ rệt |
| SSIM | 0.4434 | 0.4448 | 0.3238 | 6/8 | không có khác biệt rõ rệt |
| LPIPS | 0.3882 | 0.3865 | -0.4573 | 6/8 | không có khác biệt rõ rệt |
| Latent L2 | 0.7424 | 0.7421 | -0.0382 | 4/8 | không có khác biệt rõ rệt |
| I3D-L2 | 39.6409 | 39.6931 | 0.1318 | 4/8 | không có khác biệt rõ rệt |
| FVD | 731.7877 | 743.2240 | 1.5628 | 37% bootstrap | không có khác biệt rõ rệt |

#### 🏁 Kết luận

**Chưa đo được khác biệt đáng tin cậy** giữa LoRA và Base ở thiết lập này.

- Trong 6 metric: **0** nghiêng hẳn về LoRA (có ý nghĩa), **0** nghiêng hẳn về Base, **6** không có khác biệt rõ rệt, còn lại ở mức xu hướng chưa chắc chắn.
- Thang đo của sai số: PSNR trung bình chỉ ~12.1 dB và SSIM ~0.44 cho cả hai model, nghĩa là cả Base lẫn LoRA đều còn *rất xa* video thật; phần chênh lệch giữa hai model (+0.000 dB) nhỏ hơn nhiều so với độ lệch giữa các video.
- **Giới hạn của thí nghiệm** (cần nêu khi báo cáo): (1) chỉ 8 video held-out → nửa độ rộng CI cỡ PSNR (dB) ±0.105, SSIM ±0.00197, LPIPS ±0.00624; (2) LoRA mới huấn luyện 300 iteration trên 24 video nên khó kỳ vọng thay đổi lớn; (3) PSNR/SSIM so khớp từng pixel rất khắt khe với bài toán sinh video (chỉ cần lệch vài frame chuyển động là điểm tụt mạnh) và GT 20 fps bị căn theo chỉ số frame với video 16 fps; (4) FVD/Latent L2 dùng backbone ngoài (xem nhãn backbone ở Bảng 4) nên chỉ so sánh tương đối; (5) một seed sinh mỗi video.
- **Hướng làm tiếp nếu muốn chênh lệch rõ hơn**: huấn luyện lâu hơn/nhiều video hơn, tăng số video đánh giá (≥ 30), nhiều seed mỗi video, và dùng metric bám sát thao tác robot (vị trí tay/vật thể) bên cạnh metric ảnh.

### Bảng 3 · Kiểm định ghép cặp

| Metric | Base | LoRA | Δ (LoRA−Base) | CI95 thấp | CI95 cao | Δ % | LoRA thắng | p Wilcoxon | p t-test | d_z (>0: LoRA tốt) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSNR (dB) | 12.0772 | 12.0775 | 0.0004 | -0.0760 | 0.0827 | 0.0030 | 3/8 | 0.9453 | 0.9937 | 0.0029 | không có khác biệt rõ rệt |
| SSIM | 0.4434 | 0.4448 | 0.0014 | -0.0001 | 0.0029 | 0.3238 | 6/8 | 0.1953 | 0.1290 | 0.6083 | không có khác biệt rõ rệt |
| LPIPS | 0.3882 | 0.3865 | -0.0018 | -0.0065 | 0.0031 | -0.4573 | 6/8 | 0.4609 | 0.5224 | 0.2381 | không có khác biệt rõ rệt |
| Latent L2 | 0.7424 | 0.7421 | -0.0003 | -0.0046 | 0.0038 | -0.0382 | 4/8 | 1.0000 | 0.9058 | 0.0434 | không có khác biệt rõ rệt |
| I3D-L2 | 39.6409 | 39.6931 | 0.0522 | -1.2477 | 1.4238 | 0.1318 | 4/8 | 0.9453 | 0.9447 | -0.0254 | không có khác biệt rõ rệt |

#### 📝 Đánh giá Bảng 3 — Base vs LoRA có khác nhau thật không?
- **PSNR (dB)** → *không có khác biệt rõ rệt*. Δ = +0.0003658 (CI95 [-0.076, +0.0827], chứa 0), p Wilcoxon = 0.945, d_z = +0.00, LoRA thắng 3/8 video.
- **SSIM** → *không có khác biệt rõ rệt*. Δ = +0.001436 (CI95 [-0.0001307, +0.002925], chứa 0), p Wilcoxon = 0.195, d_z = +0.61, LoRA thắng 6/8 video.
- **LPIPS** → *không có khác biệt rõ rệt*. Δ = -0.001775 (CI95 [-0.006474, +0.003057], chứa 0), p Wilcoxon = 0.461, d_z = +0.24, LoRA thắng 6/8 video.
- **Latent L2** → *không có khác biệt rõ rệt*. Δ = -0.0002839 (CI95 [-0.004557, +0.003799], chứa 0), p Wilcoxon = 1.000, d_z = +0.04, LoRA thắng 4/8 video.
- **I3D-L2** → *không có khác biệt rõ rệt*. Δ = +0.05223 (CI95 [-1.248, +1.424], chứa 0), p Wilcoxon = 0.945, d_z = -0.03, LoRA thắng 4/8 video.
- **Tổng kết**: 0/5 metric có khác biệt đạt ý nghĩa thống kê (CI95 không chứa 0 và p Wilcoxon < 0.05); 0 metric trong đó nghiêng hẳn về LoRA.
- **Công suất kiểm định (n = 8 video)**: nửa độ rộng khoảng tin cậy t 95% của Δ là PSNR (dB) ±0.105, SSIM ±0.00197, LPIPS ±0.00624, Latent L2 ±0.00547, I3D-L2 ±1.72. Chênh lệch nhỏ hơn mức này không thể tách khỏi nhiễu giữa các video với 8 mẫu — nên 'không khác biệt rõ rệt' nghĩa là *chưa đủ bằng chứng*, không phải *chắc chắn bằng nhau*.

### Bảng 3 · Kiểm định ghép cặp

| Metric | Base | LoRA | Δ (LoRA−Base) | CI95 thấp | CI95 cao | Δ % | LoRA thắng | p Wilcoxon | p t-test | d_z (>0: LoRA tốt) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSNR (dB) | 12.0772 | 12.0775 | 0.0004 | -0.0760 | 0.0827 | 0.0030 | 3/8 | 0.9453 | 0.9937 | 0.0029 | không có khác biệt rõ rệt |
| SSIM | 0.4434 | 0.4448 | 0.0014 | -0.0001 | 0.0029 | 0.3238 | 6/8 | 0.1953 | 0.1290 | 0.6083 | không có khác biệt rõ rệt |
| LPIPS | 0.3882 | 0.3865 | -0.0018 | -0.0065 | 0.0031 | -0.4573 | 6/8 | 0.4609 | 0.5224 | 0.2381 | không có khác biệt rõ rệt |
| Latent L2 | 0.7424 | 0.7421 | -0.0003 | -0.0046 | 0.0038 | -0.0382 | 4/8 | 1.0000 | 0.9058 | 0.0434 | không có khác biệt rõ rệt |
| I3D-L2 | 39.6409 | 39.6931 | 0.0522 | -1.2477 | 1.4238 | 0.1318 | 4/8 | 0.9453 | 0.9447 | -0.0254 | không có khác biệt rõ rệt |

#### 📝 Đánh giá Bảng 3 — Base vs LoRA có khác nhau thật không?
- **PSNR (dB)** → *không có khác biệt rõ rệt*. Δ = +0.0003658 (CI95 [-0.076, +0.0827], chứa 0), p Wilcoxon = 0.945, d_z = +0.00, LoRA thắng 3/8 video.
- **SSIM** → *không có khác biệt rõ rệt*. Δ = +0.001436 (CI95 [-0.0001307, +0.002925], chứa 0), p Wilcoxon = 0.195, d_z = +0.61, LoRA thắng 6/8 video.
- **LPIPS** → *không có khác biệt rõ rệt*. Δ = -0.001775 (CI95 [-0.006474, +0.003057], chứa 0), p Wilcoxon = 0.461, d_z = +0.24, LoRA thắng 6/8 video.
- **Latent L2** → *không có khác biệt rõ rệt*. Δ = -0.0002839 (CI95 [-0.004557, +0.003799], chứa 0), p Wilcoxon = 1.000, d_z = +0.04, LoRA thắng 4/8 video.
- **I3D-L2** → *không có khác biệt rõ rệt*. Δ = +0.05223 (CI95 [-1.248, +1.424], chứa 0), p Wilcoxon = 0.945, d_z = -0.03, LoRA thắng 4/8 video.
- **Tổng kết**: 0/5 metric có khác biệt đạt ý nghĩa thống kê (CI95 không chứa 0 và p Wilcoxon < 0.05); 0 metric trong đó nghiêng hẳn về LoRA.
- **Công suất kiểm định (n = 8 video)**: nửa độ rộng khoảng tin cậy t 95% của Δ là PSNR (dB) ±0.105, SSIM ±0.00197, LPIPS ±0.00624, Latent L2 ±0.00547, I3D-L2 ±1.72. Chênh lệch nhỏ hơn mức này không thể tách khỏi nhiễu giữa các video với 8 mẫu — nên 'không khác biệt rõ rệt' nghĩa là *chưa đủ bằng chứng*, không phải *chắc chắn bằng nhau*.

### Bảng 4 · FVD — backbone: I3D (Kinetics-400, torchscript StyleGAN-V)

| So sánh | FVD | CI95 thấp | CI95 cao | Số clip/tập | Chiều đặc trưng |
|---|---|---|---|---|---|
| Base ↔ GT | 731.7877 | 750.8368 | 1050.4326 | 160 | 400 |
| LoRA ↔ GT | 743.2240 | 754.6321 | 1072.6607 | 160 | 400 |
| Base ↔ LoRA (tham chiếu) | 291.2377 | 272.4966 | 471.7785 | 160 | 400 |

#### 📝 Đánh giá Bảng 4 — FVD (backbone: I3D (Kinetics-400, torchscript StyleGAN-V))
- **FVD(Base, GT) = 731.79**, **FVD(LoRA, GT) = 743.22** (thấp hơn = phân phối video sinh ra gần video thật hơn). Chênh lệch LoRA − Base = +11.44 (bootstrap theo video: CI95 [-54.84, +78.34]; LoRA có FVD thấp hơn Base trong 37% số lần resample) → **khoảng tin cậy chứa 0 → chưa đủ bằng chứng LoRA khác Base về FVD**.
- Khoảng cách Base↔LoRA = 291.24, bằng **0.39×** khoảng cách trung bình tới GT. Hai model sinh ra phân phối video gần nhau hơn nhiều so với GT → LoRA chưa dịch chuyển phân phối đầu ra đáng kể.
- **Lưu ý độ tin cậy**: chỉ có 8 video × 20 clip chồng lấp = 160 mẫu/tập nhưng đặc trưng 400 chiều → ma trận hiệp phương sai thiếu hạng, FVD bị chệch lên và *không so sánh được trực tiếp với con số FVD trong các bài báo*; chỉ nên dùng để so sánh tương đối Base vs LoRA trong cùng thiết lập này.

### Bảng 5 · Theo thời gian

| Metric | Đoạn | Base | LoRA | Cải thiện của LoRA |
|---|---|---|---|---|
| PSNR (dB) | Đầu 1/3 | 12.8519 | 12.8213 | -0.0306 |
| PSNR (dB) | Giữa 1/3 | 11.8751 | 11.9245 | 0.0494 |
| PSNR (dB) | Cuối 1/3 | 11.4854 | 11.4671 | -0.0183 |
| PSNR (dB) | Drift (cuối − đầu) | -1.3665 | -1.3542 | 0.0123 |
| SSIM* | Đầu 1/3 | 0.4199 | 0.4209 | 0.0010 |
| SSIM* | Giữa 1/3 | 0.4022 | 0.4037 | 0.0015 |
| SSIM* | Cuối 1/3 | 0.3920 | 0.3921 | 0.0001 |
| SSIM* | Drift (cuối − đầu) | -0.0280 | -0.0289 | -0.0009 |
| LPIPS | Đầu 1/3 | 0.3452 | 0.3429 | 0.0023 |
| LPIPS | Giữa 1/3 | 0.3959 | 0.3917 | 0.0043 |
| LPIPS | Cuối 1/3 | 0.4248 | 0.4261 | -0.0013 |
| LPIPS | Drift (cuối − đầu) | 0.0796 | 0.0832 | -0.0036 |
| Latent L2 | Đầu 1/3 | 0.6639 | 0.6621 | 0.0017 |
| Latent L2 | Giữa 1/3 | 0.7548 | 0.7525 | 0.0023 |
| Latent L2 | Cuối 1/3 | 0.8010 | 0.8041 | -0.0031 |
| Latent L2 | Drift (cuối − đầu) | 0.1371 | 0.1420 | -0.0048 |

#### 📝 Đánh giá Bảng 5 — sai số tăng dần theo thời gian (SSIM* = SSIM tính lại theo frame, chỉ dùng cho phân tích theo thời gian)
- **PSNR (dB)**: từ đoạn đầu đến đoạn cuối, Base xấu đi 1.366 và LoRA 1.354 (drift Base -1.366 / LoRA -1.354). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.0494) và nhỏ nhất/bất lợi nhất ở **Đầu 1/3** (-0.0306) (dương = LoRA tốt hơn).
- **SSIM***: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.02796 và LoRA 0.02885 (drift Base -0.02796 / LoRA -0.02885). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00152) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (+9.09e-05) (dương = LoRA tốt hơn).
- **LPIPS**: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.07957 và LoRA 0.08315 (drift Base +0.07957 / LoRA +0.08315). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00426) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (-0.00131) (dương = LoRA tốt hơn).
- **Latent L2**: từ đoạn đầu đến đoạn cuối, Base xấu đi 0.1371 và LoRA 0.142 (drift Base +0.1371 / LoRA +0.142). Chênh lệch có lợi cho LoRA lớn nhất ở **Giữa 1/3** (+0.00232) và nhỏ nhất/bất lợi nhất ở **Cuối 1/3** (-0.00309) (dương = LoRA tốt hơn).
- **Ý nghĩa**: nếu drift của LoRA nhỏ hơn Base thì LoRA giúp giữ chất lượng tốt hơn khi video dài ra (ít tích luỹ sai số); nếu hai drift gần như bằng nhau thì LoRA không cải thiện độ ổn định theo thời gian. Sai số tăng mạnh về cuối clip là đặc trưng của sinh video autoregressive/diffusion khi chỉ được điều kiện bằng 1 frame đầu.

### Bảng 6 · Thắng/thua theo video × metric

| video | PSNR (dB) | SSIM | LPIPS | Latent L2 | I3D-L2 | LoRA thắng | Base thắng |
|---|---|---|---|---|---|---|---|
| 9 | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | 5 | 0 |
| 19 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | LoRA ✓ | 3 | 2 |
| 60 | Base ✓ | LoRA ✓ | LoRA ✓ | ≈ | Base ✓ | 2 | 2 |
| 62 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | Base ✓ | 2 | 3 |
| 64 | Base ✓ | Base ✓ | Base ✓ | Base ✓ | Base ✓ | 0 | 5 |
| 65 | LoRA ✓ | LoRA ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | 4 | 1 |
| 98 | LoRA ✓ | Base ✓ | Base ✓ | LoRA ✓ | LoRA ✓ | 3 | 2 |
| 100 | Base ✓ | LoRA ✓ | LoRA ✓ | Base ✓ | LoRA ✓ | 3 | 2 |
| LoRA - Base - hoà | 3 - 5 - 0 | 6 - 2 - 0 | 6 - 2 - 0 | 3 - 4 - 1 | 4 - 4 - 0 | 22 | 17 |

#### 📝 Đánh giá Bảng 6 — mức độ nhất quán giữa các metric
- Tổng cộng LoRA thắng **22** ô, Base thắng **17** ô trên 8×5 = 40 ô (còn lại là hoà trong ±0.1%).
- Video mà LoRA không thua ở metric nào: `9`. Video mà LoRA không thắng ở metric nào: `64`.
- **6/8** video cho kết quả *lẫn lộn* (có metric LoRA thắng, có metric Base thắng). Số video lẫn lộn lớn cho thấy các metric không đồng thuận — LoRA không cải thiện một cách nhất quán, và kết luận phụ thuộc vào metric được chọn.

### Bảng 7 · Tương quan Spearman giữa các metric

| index | PSNR (dB) | SSIM | LPIPS | Latent L2 | I3D-L2 |
|---|---|---|---|---|---|
| PSNR (dB) | 1.00 | 0.85 | 0.80 | 0.91 | 0.66 |
| SSIM | 0.85 | 1.00 | 0.57 | 0.63 | 0.42 |
| LPIPS | 0.80 | 0.57 | 1.00 | 0.88 | 0.65 |
| Latent L2 | 0.91 | 0.63 | 0.88 | 1.00 | 0.74 |
| I3D-L2 | 0.66 | 0.42 | 0.65 | 0.74 | 1.00 |

#### 📝 Đánh giá Bảng 7 — độ đồng thuận giữa các metric
- Cặp đồng thuận nhất: **PSNR (dB) – Latent L2** (ρ = +0.91); cặp ít đồng thuận nhất: **SSIM – I3D-L2** (ρ = +0.42). ρ dương nghĩa là video nào 'dễ' theo metric này cũng 'dễ' theo metric kia.
- Tương quan trung bình giữa các cặp: +0.71. Các metric xếp hạng video khá giống nhau → độ khó của video là yếu tố chung chi phối mọi metric.
- Lưu ý: chỉ 16 mẫu và 8 video lặp lại ở 2 model nên các mẫu không hoàn toàn độc lập; xem đây là mô tả, không phải kiểm định.

### Bảng 8 · Độ khác biệt giữa video Base và video LoRA

| video | PSNR(Base,LoRA) dB | MAE(Base,LoRA) /255 | Latent RMSE(Base,LoRA) |
|---|---|---|---|
| 9 | 19.2489 | 10.8927 | 0.3271 |
| 19 | 19.8464 | 10.2985 | 0.2781 |
| 60 | 20.0293 | 10.8914 | 0.2868 |
| 62 | 23.1917 | 7.3961 | 0.2045 |
| 64 | 24.5957 | 6.5691 | 0.1973 |
| 65 | 16.9155 | 17.2515 | 0.4066 |
| 98 | 16.7088 | 19.2506 | 0.4260 |
| 100 | 20.1951 | 10.8193 | 0.3008 |
| Trung bình | 20.0914 | 11.6712 | 0.3034 |

#### 📝 Đánh giá Bảng 8 — LoRA đã thay đổi đầu ra bao nhiêu?
- PSNR giữa video Base và video LoRA (cùng frame đầu, cùng prompt) trung bình **20.1 dB**, MAE trung bình 11.7/255. Để so sánh, PSNR của mỗi model so với ground-truth chỉ khoảng **12.1 dB**.
- Hai video Base/LoRA giống nhau *hơn nhiều* so với việc mỗi video giống GT → LoRA chỉ chỉnh nhẹ đầu ra; khoảng cách tới GT chủ yếu do giới hạn của cả mô hình (chuyển động robot, chi tiết vật thể, lệch thời gian/tốc độ khung hình), nên metric khó nhúc nhích.
- Trong không gian latent: khoảng cách Base↔LoRA = 0.303, so với khoảng cách tới GT ≈ 0.742.
- Video mà LoRA làm đầu ra thay đổi nhiều nhất là `98` (PSNR Base↔LoRA = 16.7 dB).

### Hình · Mức khác biệt Base ↔ LoRA

![fig_base_vs_lora_difference.png](fig_base_vs_lora_difference.png)

### Bảng 7 · Tương quan Spearman giữa các metric

| index | PSNR (dB) | SSIM | LPIPS | Latent L2 | I3D-L2 |
|---|---|---|---|---|---|
| PSNR (dB) | 1.00 | 0.85 | 0.80 | 0.91 | 0.66 |
| SSIM | 0.85 | 1.00 | 0.57 | 0.63 | 0.42 |
| LPIPS | 0.80 | 0.57 | 1.00 | 0.88 | 0.65 |
| Latent L2 | 0.91 | 0.63 | 0.88 | 1.00 | 0.74 |
| I3D-L2 | 0.66 | 0.42 | 0.65 | 0.74 | 1.00 |

#### 📝 Đánh giá Bảng 7 — độ đồng thuận giữa các metric
- Cặp đồng thuận nhất: **PSNR (dB) – Latent L2** (ρ = +0.91); cặp ít đồng thuận nhất: **SSIM – I3D-L2** (ρ = +0.42). ρ dương nghĩa là video nào 'dễ' theo metric này cũng 'dễ' theo metric kia.
- Tương quan trung bình giữa các cặp: +0.71. Các metric xếp hạng video khá giống nhau → độ khó của video là yếu tố chung chi phối mọi metric.
- Lưu ý: chỉ 16 mẫu và 8 video lặp lại ở 2 model nên các mẫu không hoàn toàn độc lập; xem đây là mô tả, không phải kiểm định.

### Bảng 8 · Độ khác biệt giữa video Base và video LoRA

| video | PSNR(Base,LoRA) dB | MAE(Base,LoRA) /255 | Latent RMSE(Base,LoRA) |
|---|---|---|---|
| 9 | 19.2489 | 10.8927 | 0.3271 |
| 19 | 19.8464 | 10.2985 | 0.2781 |
| 60 | 20.0293 | 10.8914 | 0.2868 |
| 62 | 23.1917 | 7.3961 | 0.2045 |
| 64 | 24.5957 | 6.5691 | 0.1973 |
| 65 | 16.9155 | 17.2515 | 0.4066 |
| 98 | 16.7088 | 19.2506 | 0.4260 |
| 100 | 20.1951 | 10.8193 | 0.3008 |
| Trung bình | 20.0914 | 11.6712 | 0.3034 |

#### 📝 Đánh giá Bảng 8 — LoRA đã thay đổi đầu ra bao nhiêu?
- PSNR giữa video Base và video LoRA (cùng frame đầu, cùng prompt) trung bình **20.1 dB**, MAE trung bình 11.7/255. Để so sánh, PSNR của mỗi model so với ground-truth chỉ khoảng **12.1 dB**.
- Hai video Base/LoRA giống nhau *hơn nhiều* so với việc mỗi video giống GT → LoRA chỉ chỉnh nhẹ đầu ra; khoảng cách tới GT chủ yếu do giới hạn của cả mô hình (chuyển động robot, chi tiết vật thể, lệch thời gian/tốc độ khung hình), nên metric khó nhúc nhích.
- Trong không gian latent: khoảng cách Base↔LoRA = 0.303, so với khoảng cách tới GT ≈ 0.742.
- Video mà LoRA làm đầu ra thay đổi nhiều nhất là `98` (PSNR Base↔LoRA = 16.7 dB).

### Hình · Mức khác biệt Base ↔ LoRA

![fig_base_vs_lora_difference.png](fig_base_vs_lora_difference.png)

### Hình 1 · Từng video, Base vs LoRA

![fig1_per_video_dumbbell.png](fig1_per_video_dumbbell.png)

#### 📝 Đánh giá Hình 1
- **PSNR (dB)**: giá trị giữa các video trải trong khoảng 3.31 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.1 (trung bình tuyệt đối) = 3.0% độ trải đó.
- **SSIM**: giá trị giữa các video trải trong khoảng 0.1775 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00224 (trung bình tuyệt đối) = 1.3% độ trải đó.
- **LPIPS**: giá trị giữa các video trải trong khoảng 0.1465 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00548 (trung bình tuyệt đối) = 3.7% độ trải đó.
- **Latent L2**: giá trị giữa các video trải trong khoảng 0.1978 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 0.00511 (trung bình tuyệt đối) = 2.6% độ trải đó.
- **I3D-L2**: giá trị giữa các video trải trong khoảng 10.12 (Base), trong khi chênh lệch Base↔LoRA ở từng video chỉ cỡ 1.73 (trung bình tuyệt đối) = 17.1% độ trải đó.
- **Cách đọc**: hai chấm gần nhau (đoạn nối ngắn) = LoRA gần như không đổi so với Base ở video đó. Thứ tự các video (video nào cao/thấp) gần như giống hệt giữa hai model → *nội dung video* quyết định điểm, không phải model.

### Hình 2 · Cải thiện của LoRA theo video

![fig2_improvement_per_video.png](fig2_improvement_per_video.png)

#### 📝 Đánh giá Hình 2
- **PSNR (dB)**: 3 cột xanh / 5 cột đỏ; trung bình +0.000366. Video LoRA giúp nhiều nhất `9` (+0.206), thiệt nhất `64` (-0.144). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **SSIM**: 6 cột xanh / 2 cột đỏ; trung bình +0.00144. Video LoRA giúp nhiều nhất `60` (+0.00447), thiệt nhất `98` (-0.0023). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **LPIPS**: 6 cột xanh / 2 cột đỏ; trung bình +0.00178. Video LoRA giúp nhiều nhất `9` (+0.0134), thiệt nhất `98` (-0.0112). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **Latent L2**: 4 cột xanh / 4 cột đỏ; trung bình +0.000284. Video LoRA giúp nhiều nhất `65` (+0.00994), thiệt nhất `64` (-0.00865). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **I3D-L2**: 4 cột xanh / 4 cột đỏ; trung bình -0.0522. Video LoRA giúp nhiều nhất `100` (+2.66), thiệt nhất `64` (-3.43). Dải xám (CI95) chứa 0 → không kết luận được LoRA tốt hơn.
- **Cách đọc**: cột xanh và đỏ xen kẽ với biên độ gần như ngang nhau nghĩa là LoRA chỉ tạo *nhiễu* quanh 0 chứ không tạo cải thiện hệ thống.

### Hình 3 · Forest plot hiệu ứng

![fig3_forest_effect_sizes.png](fig3_forest_effect_sizes.png)

#### 📝 Đánh giá Hình 3
- Hiệu ứng chuẩn hoá lớn nhất là **SSIM** (d_z = +0.61; quy ước ~0.2 nhỏ, 0.5 vừa, 0.8 lớn). Mức thay đổi so với Base chỉ trong khoảng 0.00% – 0.46%.
- Các metric có CI95 (của Δ) chứa 0: PSNR (dB), SSIM, LPIPS, Latent L2, I3D-L2. Tất cả điểm xám đi qua đường 0 → LoRA chưa tạo ra khác biệt có thể đo được.
- Lưu ý: d_z từ 8 mẫu rất không ổn định (CI rộng) — hãy đọc xu hướng chung giữa các metric hơn là con số tuyệt đối.

### Hình 4 · Đường cong theo thời gian

![fig4_time_curves.png](fig4_time_curves.png)

#### 📝 Đánh giá Hình 4
- **PSNR (dB)**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 50% số mốc thời gian, |LoRA−Base| lớn nhất là 0.157. Cả hai đều xấu đi theo thời gian (từ 14.5 ở đầu đến 11.4 ở cuối với Base).
- **SSIM***: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 70% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00534. Cả hai đều xấu đi theo thời gian (từ 0.447 ở đầu đến 0.39 ở cuối với Base).
- **LPIPS**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 73% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00881. Cả hai đều xấu đi theo thời gian (từ 0.271 ở đầu đến 0.428 ở cuối với Base).
- **Latent L2**: đường LoRA và Base gần như chồng khít; LoRA tốt hơn Base ở 52% số mốc thời gian, |LoRA−Base| lớn nhất là 0.00708. Cả hai đều xấu đi theo thời gian (từ 0.627 ở đầu đến 0.809 ở cuối với Base).
- **Cách đọc**: hàng dưới là chênh lệch LoRA − Base; nếu dải đen (±1.96 SEM) luôn chứa đường đỏ y = 0 thì không có thời điểm nào LoRA khác Base một cách đáng tin. Phần lớn sai số tích luỹ theo thời gian là của *cả hai* model, tức giới hạn của mô hình nền chứ không phải do LoRA.

### Hình 5 · Heatmap % cải thiện

![fig5_improvement_heatmap.png](fig5_improvement_heatmap.png)

#### 📝 Đánh giá Hình 5
- Ô có thay đổi lớn nhất: video `64` ở **I3D-L2** (-8.75%). Toàn bảng chỉ dao động trong ±8.75%.
- Hàng 'Trung bình' (dưới đường đen): PSNR (dB) -0.02%, SSIM +0.30%, LPIPS +0.50%, Latent L2 +0.05%, I3D-L2 -0.11%.
- **Cách đọc**: nếu một *hàng* (video) xanh đồng loạt thì LoRA giúp nhất quán video đó; nếu một *cột* (metric) xanh đồng loạt thì LoRA cải thiện metric đó. Mảng màu loang lổ xanh/đỏ xen kẽ = tác động không nhất quán.

### Hình 6 · Scatter Base vs LoRA

![fig6_base_vs_lora_scatter.png](fig6_base_vs_lora_scatter.png)

#### 📝 Đánh giá Hình 6
- **PSNR (dB)**: tương quan Base–LoRA r = 0.994; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **SSIM**: tương quan Base–LoRA r = 0.999; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **LPIPS**: tương quan Base–LoRA r = 0.989; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **Latent L2**: tương quan Base–LoRA r = 0.996; các điểm nằm sát đường chéo → LoRA giữ nguyên thứ hạng độ khó giữa các video.
- **I3D-L2**: tương quan Base–LoRA r = 0.837; các điểm lệch khỏi đường chéo đáng kể → LoRA đổi thứ hạng một số video.
- **Cách đọc**: khoảng cách dọc từ điểm tới đường chéo = mức thay đổi do LoRA. Điểm xanh phía tốt, đỏ phía xấu; điểm càng xa đường chéo càng chịu tác động nhiều.

### Hình 7 · FVD

![fig7_fvd.png](fig7_fvd.png)

#### 📝 Đánh giá Hình 7
- Cột Base↔GT = 731.8, LoRA↔GT = 743.2; thanh sai số là CI95 bootstrap theo video — hai thanh chồng lấn mạnh.
- Histogram bên phải là phân phối của FVD(LoRA) − FVD(Base): CI95 = [-54.8, +78.3] → chứa 0 → chưa đủ bằng chứng LoRA khác Base về FVD.
- Cột tím (Base↔LoRA) = 291.2 cho biết hai model sinh ra phân phối khác nhau bao nhiêu; nếu nhỏ hơn nhiều hai cột còn lại thì LoRA chưa dịch chuyển đầu ra nhiều.
- FVD ở đây dựa trên rất ít video nên chỉ mang tính so sánh tương đối (xem lưu ý ở Bảng 4).

### Hình 8 · Tương quan metric

![fig8_metric_correlation.png](fig8_metric_correlation.png)

#### 📝 Đánh giá Hình 8
- Tương quan Spearman ngoài đường chéo nằm trong khoảng [+0.42, +0.91], trung bình +0.71.
- Ô xanh đậm = hai metric xếp hạng các (video, model) giống nhau; ô đỏ/nhạt = hai metric bất đồng, tức chúng đang bắt các khía cạnh chất lượng khác nhau. Vì vậy kết luận về LoRA nên dựa trên *nhiều* metric cùng lúc (Bảng 3, 6 và Hình 3) thay vì chỉ PSNR/SSIM.

### Hình 9 · So sánh trực quan 8 video

![fig9_qualitative_all8.png](fig9_qualitative_all8.png)

### Hình 10a · Diễn tiến theo thời gian (video 1-4)

![fig10a_strips_videos_1-4.png](fig10a_strips_videos_1-4.png)

### Hình 10b · Diễn tiến theo thời gian (video 5-8)

![fig10b_strips_videos_5-8.png](fig10b_strips_videos_5-8.png)

#### 📝 Đánh giá Hình 9–10
- Cột thứ 4 là hiệu tuyệt đối |LoRA − Base| khuếch đại ×5: vùng sáng là nơi LoRA thực sự vẽ khác Base. Trung bình chênh lệch pixel Base↔LoRA chỉ 11.7/255 (Bảng 8).
- ΔPSNR theo video dao động từ -0.14 dB (video `64`) đến +0.21 dB (video `9`).
- Quan sát bằng mắt nên tập trung vào: (1) cánh tay/bàn tay robot có đi đúng quỹ đạo như GT không, (2) vật thể bị gắp có giữ đúng hình dạng/màu không, (3) hậu cảnh có bị 'trôi' dần về cuối clip không. Ở các hàng của Hình 10, so sánh cột frame 92 (cuối clip) giữa GT, Base và LoRA — đây là chỗ sai khác tích luỹ rõ nhất.
- Lưu ý: GT gốc là 20 fps còn video sinh ra là 16 fps nhưng code gốc (và các metric ở đây) căn theo *chỉ số frame*, nên cùng một chỉ số frame có thể tương ứng hai thời điểm hơi khác nhau; điều này làm giảm PSNR/SSIM tuyệt đối của cả Base lẫn LoRA như nhau.

### Bảng 9 · Tổng hợp mọi metric

| Metric | Base | LoRA | Δ % | LoRA thắng | Kết luận |
|---|---|---|---|---|---|
| PSNR (dB) | 12.0772 | 12.0775 | 0.0030 | 3/8 | không có khác biệt rõ rệt |
| SSIM | 0.4434 | 0.4448 | 0.3238 | 6/8 | không có khác biệt rõ rệt |
| LPIPS | 0.3882 | 0.3865 | -0.4573 | 6/8 | không có khác biệt rõ rệt |
| Latent L2 | 0.7424 | 0.7421 | -0.0382 | 4/8 | không có khác biệt rõ rệt |
| I3D-L2 | 39.6409 | 39.6931 | 0.1318 | 4/8 | không có khác biệt rõ rệt |
| FVD | 731.7877 | 743.2240 | 1.5628 | 37% bootstrap | không có khác biệt rõ rệt |

#### 🏁 Kết luận

**Chưa đo được khác biệt đáng tin cậy** giữa LoRA và Base ở thiết lập này.

- Trong 6 metric: **0** nghiêng hẳn về LoRA (có ý nghĩa), **0** nghiêng hẳn về Base, **6** không có khác biệt rõ rệt, còn lại ở mức xu hướng chưa chắc chắn.
- Thang đo của sai số: PSNR trung bình chỉ ~12.1 dB và SSIM ~0.44 cho cả hai model, nghĩa là cả Base lẫn LoRA đều còn *rất xa* video thật; phần chênh lệch giữa hai model (+0.000 dB) nhỏ hơn nhiều so với độ lệch giữa các video.
- **Giới hạn của thí nghiệm** (cần nêu khi báo cáo): (1) chỉ 8 video held-out → nửa độ rộng CI cỡ PSNR (dB) ±0.105, SSIM ±0.00197, LPIPS ±0.00624; (2) LoRA mới huấn luyện 300 iteration trên 24 video nên khó kỳ vọng thay đổi lớn; (3) PSNR/SSIM so khớp từng pixel rất khắt khe với bài toán sinh video (chỉ cần lệch vài frame chuyển động là điểm tụt mạnh) và GT 20 fps bị căn theo chỉ số frame với video 16 fps; (4) FVD/Latent L2 dùng backbone ngoài (xem nhãn backbone ở Bảng 4) nên chỉ so sánh tương đối; (5) một seed sinh mỗi video.
- **Hướng làm tiếp nếu muốn chênh lệch rõ hơn**: huấn luyện lâu hơn/nhiều video hơn, tăng số video đánh giá (≥ 30), nhiều seed mỗi video, và dùng metric bám sát thao tác robot (vị trí tay/vật thể) bên cạnh metric ảnh.