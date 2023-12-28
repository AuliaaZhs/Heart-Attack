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
            kcm = st.number_input('Input nilai KCM')
            
        with col2:
            gender = st.selectbox('Select Gender', ['Male', 'Female'])
            pressurehight = st.number_input('Input nilai Pressure High', min_value=0, max_value=500,step=1)
            glucose = st.number_input('Input nilai Glucose', min_value=0, max_value=1000,step=1)
            troponin = st.number_input('Input nilai Troponin')

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
        output = ''
        if user_result[0] == 0:
            output = 'You are healthy'
        else:
            output = 'You are not healthy'
        st.write(output)