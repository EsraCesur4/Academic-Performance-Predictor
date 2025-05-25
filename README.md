# 📊 Enhanced Student Habits & Academic Performance Prediction

![## 🔍 7  Örnek Tahminler (Sample Predictions) Modelin gerçek hayattaki tahmin gücünü göstermek amacıyla test setinden rastgele seçilen öğrenciler için tahminler yapılmıştır  Öğrenci  Gerçek Değer ](https://github.com/user-attachments/assets/0f0cc382-1351-49b4-957a-bdf9622e3bbf)

Bu proje, Kaggle’daki "Enhanced Student Habits and Academic Performance" veri seti kullanılarak, öğrencilerin yaşam alışkanlıkları, psikolojik durumu ve akademik geçmişine göre sınav başarılarını tahmin eden bir makine öğrenmesi modeli geliştirmeyi amaçlamaktadır.

## 🔗 Bağlantılar

- 📁 Veri Seti: [Kaggle Dataset - Enhanced Student Habits and Academic Performance](https://www.kaggle.com/datasets/aryan208/student-habits-and-academic-performance-dataset)
- 📓 Kaggle Notebook: [Proje Notebook'u](https://www.kaggle.com/code/atagns/student-habits-and-academic-performance-dataset)

---

## 🔍 1. Veri Seti Hakkında

Veri Kaggle'dan `pandas` ile yüklenmiş ve `df.head()` ile ilk beş satır incelenmiştir.

### 🧾 Sütun Açıklamaları
-  **student_id**: Öğrenciye ait benzersiz ID
-  **age**: Öğrencinin yaşı (16–28)
-  **gender**: Cinsiyet (Erkek, Kadın, Diğer)
-  **major**: Bölüm/Fakülte (Örn: Computer Science)
-  **study_hours_per_day**: Günlük çalışma süresi
-  **social_media_hours**,  **netflix_hours**,  **screen_time**
-  **part_time_job**: Yarı zamanlı iş durumu
-  **attendance_percentage**
-  **sleep_hours**,  **exercise_frequency**,  **diet_quality**
-  **mental_health_rating**,  **stress_level**,  **exam_anxiety_score**
-  **extracurricular_participation**,  **access_to_tutoring**
-  **family_income_range**,  **parental_support_level**,  **parental_education_level**
-  **motivation_level**,  **time_management_score**
-  **learning_style**,  **study_environment**
-  **dropout_risk**
-  **previous_gpa**,  **exam_score** (hedef değişken)

Toplam: **31 sütun**, hedef değişken: `exam_score`.

---

## 🧪 2. Exploratory Data Analysis (EDA)

### 🧼 Temizlik ve İlk Gözlemler
-  **Toplam örnek**: 80,000
-  **Eksik değer**: ❌ Yok
-  **Bellek**: 68.43 MB
-  **exam_score** ortalaması: 89.14 (Pozitif skew)
-  **previous_gpa** ortalaması: 3.60

---

### 📈 Görselleştirme ve Dağılım
- `exam_score`, `previous_gpa`, `study_hours_per_day`, `screen_time` gibi sütunların dağılımı incelendi.

![image](https://github.com/user-attachments/assets/7cf29091-b53a-4e5b-a52c-88c5187021c4)

-  **Sınav Puanı Dağılımı**: Öğrencilerin büyük kısmı yüksek not almıştır, dağılım sağa çarpık.
-  **Önceki GPA Dağılımı**: Değerler 3.8–4.0 aralığında toplanmıştır.
-  **Günlük Çalışma Süresi**: Ortalama ~4 saat, uç değerler temizlenmiştir.
-  **Ekran Süresi (Toplam)**: Ortalama 9.67 saat, bazı öğrencilerde 20+ saate ulaşmaktadır.
-  **Cinsiyet Dağılımı**: Kadın, erkek ve diğer gruplar arasında dengeli bir dağılım mevcuttur.
-  **Popüler Bölümler**: En çok tercih edilen 10 bölüm bar grafikte gösterilmiştir.
-  **Dropout Riski ve Başarı**: Dropout riski olan öğrencilerin başarı ortalaması daha düşüktür.

---

- Korelasyonlar:

![image](https://github.com/user-attachments/assets/1793159d-8f39-45e6-a286-8c17172a8bb1)

  -  `previous_gpa`: **0.93**
  -  `motivation_level`: 0.25
  -  `study_hours_per_day`: 0.24

Sınav başarısı en çok **previous_gpa** ile ilişkilidir.

---

## 🧹 3. Data Preprocessing

### ✅ İşlenenler:
- **Aykırı değer temizliği** (IQR) → 894 kayıt çıkarıldı

  
- **Yeni özellikler**:
.
  - `screen_time_total` :    
    Tanım: Öğrencinin toplam ekran başında geçirdiği süre  
    Hesaplama: screen_time_total = social_media_hours + netflix_hours + screen_time    
.
  - `study_sleep_ratio` :  
    Tanım: Çalışma süresinin uyku süresine oranı  
    Hesaplama: study_sleep_ratio = study_hours_per_day / sleep_hours  
.
  - `stress_anxiety_combined`:  
    Tanım: Öğrencinin stres seviyesi ile sınav kaygısının toplamı  
    Hesaplama: stress_anxiety_combined = stress_level + exam_anxiety_score  
.
  - `support_motivation_interaction`:  
    Tanım: Ebeveyn desteği ile öğrencinin motivasyon düzeyinin etkileşimi  
    Hesaplama: support_motivation_interaction = parental_support_level * motivation_level  
.

### 📦 Train-Test Ayrımı:
- Eğitim kümesi: **63,284**
- Test kümesi: **15,822**
- Stratified `exam_score` binlerine göre ayrım yapıldı

---

## 🤖 4. Model Initialization

10 farklı regresyon modeli eğitildi:

### Doğrusal Modeller:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net

### Ağaç Tabanlı:
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting

### Diğer:
- SVR
- K-Nearest Neighbors

---

## 📉 5. Cross-Validation Model Comparison

Tüm modeller 5-fold CV ile `R²` skorlarına göre değerlendirildi:

| Model | R² |
|-------|----|
| 🌟 Gradient Boosting | **0.8661** |
| Ridge / Linear | 0.8644 |
| Random Forest | 0.8618 |
| Extra Trees | 0.8600 |
| SVR | 0.8506 |
| Lasso | 0.8566 |
| Elastic Net | 0.7509 |
| Decision Tree / KNN | ~0.717 |

📌 **En başarılı model:** `Gradient Boosting`

![image](https://github.com/user-attachments/assets/3ec37b95-ae95-4fe4-9e57-e27c7deee43b)

---

## 🔧 6. Hyperparameter Tuning (Grid Search)

Kullanılan Parametre Aralığı:
```python
{
  'n_estimators': [100, 200],
  'learning_rate': [0.05, 0.1, 0.15],
  'max_depth': [3, 5, 7],
  'subsample': [0.8, 0.9, 1.0]
}
```
Toplam 3×3×3×3 = 81 farklı kombinasyon denenmiştir.   


`Gradient Boosting` için en iyi hiperparametreler:  
```python
{
  'n_estimators': 100,
  'learning_rate': 0.05,
  'max_depth': 3,
  'subsample': 0.8
}
```
---
## 🧪 6. Nihai Model Değerlendirmesi (Final Model Evaluation)

Grid Search sonucunda en iyi performansı gösteren model olan **Gradient Boosting Regressor**, test verisi üzerinde detaylı şekilde değerlendirilmiştir.

### 📊 Performans Metrikleri

| Metrik                        | Eğitim Seti | Test Seti |
|------------------------------|-------------|-----------|
| 🎯 R² (Determination Coefficient) | 0.8673      | 0.8637    |
| 📉 RMSE (Root Mean Squared Error) | 4.08        | 4.14      |
| 📏 MAE (Mean Absolute Error)      | 3.19        | 3.23      |

- Eğitim ve test skorlarının birbirine yakın olması, modelin **genelleme yeteneğinin güçlü** olduğunu ve **overfitting** sorunu yaşanmadığını göstermektedir.
- Ortalama tahmin hatası yaklaşık ±3 puandır.

---

### 📈 Görselleştirmeler

![image](https://github.com/user-attachments/assets/8c7ff59c-d308-4960-b1a5-ed491a91c359)

####  Actual vs Predicted
Gerçek ve tahmin edilen sınav puanları karşılaştırılmış; dağılım büyük ölçüde doğrusal çizgiye yakındır. Bu, modelin güçlü tahmin kabiliyetine işaret eder.

####  Residual Plot
Artık değerler çoğunlukla ±10 aralığında dağılmıştır. Sistematik bir sapma gözlenmemiştir, bu da modelin **dengeli ve tutarlı tahminler** yaptığını göstermektedir.

####  Özellik Önemi (Feature Importance)
Ağaç tabanlı modellerin sunduğu içgörülerle, modelin en çok dikkate aldığı değişkenler aşağıdaki gibidir:

| Özellik                     | Açıklama                                              |
|-----------------------------|--------------------------------------------------------|
| **previous_gpa**            | En yüksek öneme sahip değişken (%90+ etki)             |
| **stress_anxiety_combined**| Stres ve sınav kaygısı birleşimi                       |
| **attendance_percentage**   | Derslere katılım oranı                                 |

> Bu özellikler, öğrencilerin sınav başarısını tahmin etmekte en belirleyici faktörler olmuştur.

---

## 🔍 7. Örnek Tahminler (Sample Predictions)

Modelin gerçek hayattaki tahmin gücünü göstermek amacıyla test setinden rastgele seçilen öğrenciler için tahminler yapılmıştır:

| Öğrenci | Gerçek Değer | Tahmin | Hata |
|---------|--------------|--------|------|
| Student 1 | 98.0 | 96.6 | 1.4 |
| Student 2 | 95.0 | 98.0 | 3.0 |
| Student 3 | 79.0 | 75.7 | 3.3 |
| Student 4 | 84.0 | 83.8 | 0.2 |
| Student 5 | 80.0 | 89.1 | 9.1 |
