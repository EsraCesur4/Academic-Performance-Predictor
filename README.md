# 📊 Enhanced Student Habits & Academic Performance Prediction

![Sample Prediction Banner](https://github.com/user-attachments/assets/0f0cc382-1351-49b4-957a-bdf9622e3bbf)

### Ekip Üyeleri:

- Ata Güneş: [GitHub](https://github.com/AtaGn)
- Esra Cesur: [GitHub](https://github.com/esracesur4)
---

## 🔰 Giriş

Bu proje kapsamında, Kaggle’da yer alan **Enhanced Student Habits and Academic Performance** veri seti kullanılarak öğrencilerin yaşam alışkanlıkları, psikolojik durumları ve akademik geçmişlerine dayanarak sınav başarılarını tahmin eden bir makine öğrenmesi modeli geliştirilmiştir. Proje süresince 80.000'den fazla öğrenciden toplanan veriler analiz edilmiş, çeşitli önişleme teknikleri uygulanmış ve farklı regresyon algoritmaları karşılaştırılmıştır.

Modelleme süreci boyunca sadece tahmin başarısı değil, modelin genellenebilirliği, yorumlanabilirliği ve sürdürülebilirliği de dikkate alınmıştır. En iyi performansı gösteren model, **Gradient Boosting Regressor** olmuştur ve detaylı olarak değerlendirilmiştir.

---

## 📏 Metrikler

Modelleme süreci boyunca farklı algoritmalar denenmiş ve **5-fold cross-validation** yöntemiyle karşılaştırmalar yapılmıştır. Bu süreçte aşağıdaki sonuçlar elde edilmiştir:

| Model               | R² |
|---------------------|----|
| 🌟 Gradient Boosting| **0.8661** |
| Ridge / Linear      | 0.8644 |
| Random Forest       | 0.8618 |
| Extra Trees         | 0.8600 |
| SVR                 | 0.8506 |
| Lasso               | 0.8566 |
| Elastic Net         | 0.7509 |
| Decision Tree / KNN | ~0.717 |

Grid Search ile optimize edilen Gradient Boosting modeli, test verisi üzerinde şu performansı göstermiştir:

| Metrik      | Eğitim Seti | Test Seti |
|-------------|-------------|-----------|
| R²          | 0.8673      | 0.8637    |
| RMSE        | 4.08        | 4.14      |
| MAE         | 3.19        | 3.23      |

Modelin test ve eğitim sonuçları birbirine oldukça yakın çıkmıştır; bu da modelin **overfitting yapmadan genelleme kabiliyeti kazandığını** göstermektedir.

### 🔬 Özellik Önem Düzeyleri

Modelin tahminlerinde en etkili olan değişkenler şunlardır:

- **previous_gpa** (En yüksek katkı, %90+)
- **stress_anxiety_combined** (Stres + sınav kaygısı)
- **attendance_percentage** (Derslere katılım oranı)

---

### 🎯 Örnek Tahminler

Modelin gerçek hayattaki tahmin gücünü göstermek adına test verisinden rastgele seçilen bazı öğrenciler için yapılan tahminler:

| Öğrenci | Gerçek Değer | Tahmin | Hata |
|---------|--------------|--------|------|
| Student 1 | 98.0 | 96.6 | 1.4 |
| Student 2 | 95.0 | 98.0 | 3.0 |
| Student 3 | 79.0 | 75.7 | 3.3 |
| Student 4 | 84.0 | 83.8 | 0.2 |
| Student 5 | 80.0 | 89.1 | 9.1 |

---

## 🧩 Ekler  
🌐 Streamlit Uygulaması  
Proje kapsamında ayrıca bir Streamlit tabanlı arayüz geliştirilmiştir. Bu arayüz sayesinde kullanıcılar, veri yüklemeden modele kadar tüm süreci görsel olarak deneyimleyebilirler. Arayüz, model sonuçlarını grafiklerle birlikte göstererek daha kullanıcı dostu bir deneyim sunar.  

-📄 Uygulama Dosyası: app.py  
-📄 Gereksinimler: requirements.txt  

⚠️ Not: Streamlit uygulaması yalnızca aktif bir oturum süresince çalışır. Uzun süreli erişimsizlik durumunda sayfa kapanabilir. Sayfa kapandığında tekrar başlatılması gerekebilir.  

💡 Uygulamayı lokal olarak çalıştırmak için:  

```python
pip install -r requirements.txt  
streamlit run app.py  
```
## 🚀 Sonuç ve Gelecek Çalışmalar

Bu projede öğrenci davranışları ile akademik başarı arasındaki ilişki başarılı bir şekilde modellenmiştir. Özellikle previous_gpa, stress_anxiety_combined ve attendance_percentage gibi özelliklerin tahmin üzerinde yüksek etkisi olduğu görülmüştür.   

Gelecekte Yapılabilecekler
- Gerçek Zamanlı Veri Toplama: Anket formu/uygulama entegrasyonu ile veri akışı sağlanabilir.
- Web Tabanlı Arayüz: Kullanıcıların kendi verilerini girerek sınav tahmini alabilecekleri bir uygulama geliştirilebilir.
- Psikolojik Faktör Analizi: Stres, uyku, sosyal çevre gibi değişkenlerin daha detaylı analizi yapılabilir.
- Zaman Serisi Modelleme: Uzun vadeli başarı tahminleri için zaman bazlı modeller denenebilir.

## 🔗 Linkler (Bağlantılar)

- 📁 Veri Seti: [Kaggle Dataset - Enhanced Student Habits and Academic Performance](https://www.kaggle.com/datasets/aryan208/student-habits-and-academic-performance-dataset)
- 📓 Kaggle Notebook: [Proje Notebook'u](https://www.kaggle.com/code/atagns/student-habits-and-academic-performance-dataset)

