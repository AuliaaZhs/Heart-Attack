import streamlit as st

def overview():
    st.subheader("About")

    st.write('''
    Penyakit kardiovaskular (CVD) merupakan penyebab utama kematian di seluruh dunia, mencakup berbagai kondisi seperti 
    penyakit jantung koroner, penyakit serebrovaskular, penyakit jantung rematik, dan berbagai masalah jantung dan pembuluh darah lainnya. 
    Menurut data dari Organisasi Kesehatan Dunia (WHO), setiap tahunnya, 17,9 juta orang meninggal akibat CVD. 
    Serangan jantung dan stroke, dua kondisi kritis terkait CVD, menyumbang lebih dari empat dari setiap lima kematian terkait penyakit ini. 
    Alarmingly, sepertiga dari kematian tersebut terjadi sebelum mencapai usia 70 tahun. 
    Data ini mencerminkan urgensi dan kompleksitas dalam menangani tantangan kesehatan global yang ditimbulkan oleh penyakit kardiovaskular.
    ''')

    st.subheader("Goals")

    st.write('''
    Tujuan utama proyek ini adalah mengembangkan model prediktif untuk memproyeksikan kemungkinan seseorang mengalami serangan jantung 
    berdasarkan faktor-faktor kesehatan dalam dataset. Dengan demikian, proyek ini diharapkan dapat memberikan kontribusi pada pemahaman lebih mendalam
    tentang faktor risiko penyakit kardiovaskular dan mendukung langkah-langkah pencegahan yang lebih efektif, 
    memungkinkan identifikasi dini dan tindakan pencegahan yang tepat pada individu yang berpotensi lebih rentan terhadap serangan jantung.
    ''')

    st.subheader("Modelling Roadmap")
    st.image("Roadmap.png", use_column_width=True)