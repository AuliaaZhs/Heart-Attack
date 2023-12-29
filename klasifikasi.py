import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def klasifikasi():
    st.title("Heart Attack Prediction")

    df = pd.read_csv('Heart Attack.csv')

    def user_input():
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input('Input nilai Age', min_value=0, max_value=110,step=1)
            impluse = st.number_input('Input nilai Impluse', min_value=0, max_value=1200,step=1)
            pressurelow = st.number_input('Input nilai Pressure Low', min_value=0, max_value=500,step=1)
            kcm = st.number_input('Input nilai KCM', format="%.3f")
            
        with col2:
            gender = st.selectbox('Select Gender', ['Male', 'Female'])
            pressurehight = st.number_input('Input nilai Pressure High', min_value=0, max_value=500,step=1)
            glucose = st.number_input('Input nilai Glucose', min_value=0, max_value=1000,step=1)
            troponin = st.number_input('Input nilai Troponin', format="%.3f")

        data = {'age': age, 'gender': 1 if gender == 'Male' else 0, 'impluse': impluse, 'pressurehight': pressurehight,
                     'pressurelow': pressurelow, 'glucose': glucose, 'kcm': kcm, 'troponin': troponin}

        features = pd.DataFrame(data, index=[0])
        return features

    user_data = user_input()

    x = df.drop(['class'], axis=1)
    y = df['class'].map({'negative': 0, 'positive': 1})  # Mengubah 'negative' menjadi 0 dan 'positive' menjadi 1

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Standardize the data
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    user_data_scaled = scaler.transform(user_data)

    # Define the RandomForestClassifier with specified parameters
    rf = RandomForestClassifier(max_depth=None, 
                                min_samples_leaf=4, 
                                min_samples_split=10, 
                                n_estimators=50,
                                random_state=42)

    # Fit the model on scaled data
    rf.fit(x_train_scaled, y_train)

    if st.button('Predict'):
        user_result = rf.predict(user_data_scaled)
        st.subheader('Your Report : ')

        if user_result[0] == 0:
            st.write('#### **Anda Sehat!**\n')
            
            input_abnormal = False
            if input_abnormal or (
                user_data['pressurehight'].iloc[0] > 120
                or user_data['pressurelow'].iloc[0] > 80
                or user_data['glucose'].iloc[0] < 70
                or user_data['glucose'].iloc[0] > 100
                or user_data['kcm'].iloc[0] > 25
                or user_data['troponin'].iloc[0] > 0.04
            ):
                st.write('\nNamun terdapat faktor yang bisa menyebabkan Anda terkena penyakit jantung.')
                st.write('Oleh karena itu, terdapat beberapa saran untuk Anda:\n')

                if user_data['pressurehight'].iloc[0] > 120:
                    st.write("##### **Tekanan Darah Tinggi (Sistolik) anda di atas 120mmHg.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Anda dapat mencoba untuk mengontrol stres")
                    st.write("- Menghindari faktor risiko tambahan seperti merokok dan mengonsumsi alkohol\n")
            
                if user_data['pressurelow'].iloc[0] > 80:
                    st.write("##### **Tekanan Darah Rendah (Diastolik) anda di atas 80mmHg.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Pertimbangkan untuk mengurangi konsumsi garam")
                    st.write("- Periksa dan kendalikan kadar kolesterol Anda")
                    st.write("- Tingkatkan aktivitas fisik Anda\n")

                if user_data['glucose'].iloc[0] < 70:
                    st.write("##### **Nilai Glukosa Saat Puasa Anda kurang dari 70 mg/dL.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Anda dapat mengatur pola makan")
                    st.write("- Pertimbangkan untuk meningkatkan asupan karbohidrat sehat\n")

                if user_data['glucose'].iloc[0] > 100:
                    st.write("##### **Nilai Glukosa Saat Puasa Anda lebih dari 100 mg/dL.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Pertimbangkan untuk mmengurangi konsumsi gula")
                    st.write("- Anda dapat meningkatkan aktivitas fisik\n")

                if user_data['kcm'].iloc[0] > 25:
                    st.write("##### **Nilai Creatine Kinase-MB Anda lebih dari 25 U/L.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Pertimbangkan untuk melakukan pemeriksaan lanjutan terkait fungsi jantung")
                    st.write("- Jaga pola hidup sehat dan hindari faktor risiko yang dapat memengaruhi kesehatan jantung\n")

                if user_data['troponin'].iloc[0] > 0.04:
                    st.write("##### **Nilai Troponin Anda lebih dari 0.04 ng/mL.**")
                    st.write("Berikut ini beberapa saran untuk anda:")
                    st.write("- Konsultasi dengan dokter untuk evaluasi lebih lanjut")
                    st.write("- Jaga pola hidup sehat dan hindari faktor risiko yang dapat memengaruhi kesehatan jantung\n")

        else:
            st.write('#### **Anda Tidak Sehat!**\n')

            if user_data['pressurehight'].iloc[0] > 120:
                st.write("##### **Tekanan Darah Tinggi (Sistolik) anda di atas 120mmHg.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Anda dapat mencoba untuk mengontrol stres")
                st.write("- Menghindari faktor risiko tambahan seperti merokok dan mengonsumsi alkohol\n")
            
            if user_data['pressurelow'].iloc[0] > 80:
                st.write("##### **Tekanan Darah Rendah (Diastolik) anda di atas 80mmHg.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Pertimbangkan untuk mengurangi konsumsi garam")
                st.write("- Periksa dan kendalikan kadar kolesterol Anda")
                st.write("- Tingkatkan aktivitas fisik Anda\n")

            if user_data['glucose'].iloc[0] < 70:
                st.write("##### **Nilai Glukosa Saat Puasa Anda kurang dari 70 mg/dL.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Anda dapat mengatur pola makan")
                st.write("- Pertimbangkan untuk meningkatkan asupan karbohidrat sehat\n")

            if user_data['glucose'].iloc[0] > 100:
                st.write("##### **Nilai Glukosa Saat Puasa Anda lebih dari 100 mg/dL.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Pertimbangkan untuk mmengurangi konsumsi gula")
                st.write("- Anda dapat meningkatkan aktivitas fisik\n")

            if user_data['kcm'].iloc[0] > 25:
                st.write("##### **Nilai Creatine Kinase-MB Anda lebih dari 25 U/L.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Pertimbangkan untuk melakukan pemeriksaan lanjutan terkait fungsi jantung")
                st.write("- Jaga pola hidup sehat dan hindari faktor risiko yang dapat memengaruhi kesehatan jantung\n")

            if user_data['troponin'].iloc[0] > 0.04:
                st.write("##### **Nilai Troponin Anda lebih dari 0.04 ng/mL.**")
                st.write("Berikut ini beberapa saran untuk anda:")
                st.write("- Konsultasi dengan dokter untuk evaluasi lebih lanjut")
                st.write("- Jaga pola hidup sehat dan hindari faktor risiko yang dapat memengaruhi kesehatan jantung\n")