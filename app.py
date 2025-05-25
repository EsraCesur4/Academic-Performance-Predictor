import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge, Lasso, LinearRegression, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import warnings
warnings.filterwarnings('ignore')


@st.cache_data
def load_data():
    return pd.read_csv("enhanced_student_habits_performance_dataset.csv")


def preprocess(df):
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include='object').columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    for col in ['study_hours_per_day', 'exam_score', 'previous_gpa', 'stress_level']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

    df['screen_time_total'] = df['social_media_hours'] + df['netflix_hours'] + df.get('screen_time', 0)
    df['study_sleep_ratio'] = df['study_hours_per_day'] / df['sleep_hours']
    df['stress_anxiety_combined'] = df['stress_level'] + df['exam_anxiety_score']
    df['support_motivation_interaction'] = df['parental_support_level'] * df['motivation_level']

    X = df.drop(columns=['student_id', 'exam_score'])
    y = df['exam_score']

    cat_cols = X.select_dtypes(include='object').columns.tolist()
    num_cols = X.select_dtypes(include=np.number).columns.tolist()

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), cat_cols)
    ])

    return X, y, preprocessor


def train_all_models(X_train, X_test, y_train, y_test, preprocessor):
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'ElasticNet': ElasticNet(),
        'Random Forest': RandomForestRegressor(n_jobs=-1),
        'Gradient Boosting': GradientBoostingRegressor(),
        'Extra Trees': ExtraTreesRegressor(n_jobs=-1),
        'SVR': SVR(),
        'KNN': KNeighborsRegressor(),
        'Decision Tree': DecisionTreeRegressor()
    }

    results = {}
    for name, model in models.items():
        pipe = Pipeline([('preprocessor', preprocessor), ('regressor', model)])
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        results[name] = {
            'model': pipe,
            'r2': r2,
            'rmse': rmse,
            'mae': mae,
            'y_pred': y_pred
        }

    return results


def show_model_results(name, result, y_test):
    st.subheader(f"📊 {name} Sonuçları")
    st.markdown(f"""
    - **R²:** {result['r2']:.4f}  
    - **RMSE:** {result['rmse']:.4f}  
    - **MAE:** {result['mae']:.4f}
    """)

    df_pred = pd.DataFrame({'Actual': y_test.values, 'Predicted': result['y_pred']})

    st.markdown("**📈 Actual vs Predicted Line Chart**")
    st.line_chart(df_pred.reset_index(drop=True))

    st.markdown("**🔍 Scatter Plot**")
    fig, ax = plt.subplots()
    ax.scatter(y_test, result['y_pred'], alpha=0.6)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    st.pyplot(fig)

    st.markdown("**🔁 Residual Plot**")
    fig, ax = plt.subplots()
    residuals = y_test - result['y_pred']
    ax.scatter(result['y_pred'], residuals, alpha=0.6)
    ax.axhline(0, color='red', linestyle='--')
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Residuals")
    st.pyplot(fig)


def compare_models(results):
    st.header("📊 Genel Model Karşılaştırması")

    metrics_df = pd.DataFrame({
        'Model': list(results.keys()),
        'R²': [v['r2'] for v in results.values()],
        'RMSE': [v['rmse'] for v in results.values()],
        'MAE': [v['mae'] for v in results.values()]
    }).sort_values(by='R²', ascending=False)

    st.dataframe(metrics_df.set_index("Model"))

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=metrics_df, x='Model', y='R²', palette='viridis')
    ax.set_title("R² Karşılaştırması")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)


def eda(df):
    st.subheader("📁 Veri Önizleme")
    st.write(df.head())
    st.write(df.describe())
    st.write("Eksik Değer Sayısı:", df.isnull().sum().sum())

    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(df['gender'].value_counts())
    with col2:
        st.bar_chart(df['major'].value_counts().head(10))

    st.subheader("📌 exam_score Korelasyonu")
    corr = df.select_dtypes(include=[np.number]).corr()['exam_score'].sort_values(ascending=False)
    st.bar_chart(corr)

    st.subheader("🔥 Isı Haritası")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)


def main():
    st.title("🎓 Öğrenci Başarı Tahmin Dashboard")

    df = load_data()
    eda(df)
    X, y, preprocessor = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=pd.cut(y, bins=5, labels=False))

    st.info("📦 Tüm modeller eğitiliyor...")
    results = train_all_models(X_train, X_test, y_train, y_test, preprocessor)
    st.success("✅ Tüm modeller başarıyla eğitildi!")

    for model_name, result in results.items():
        show_model_results(model_name, result, y_test)

    compare_models(results)


if __name__ == "__main__":
    main()
