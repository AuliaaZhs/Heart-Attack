import streamlit as st
from streamlit_option_menu import option_menu
from overview import *
from klasifikasi import *


def main():
    with st.sidebar:
        selected = option_menu('Project Page',
                                ['Overview Project',
                                 'Prediction'],
                                 default_index=0)

    # menu_options = ['Overview Project', 'Prediction']
    # selected_menu = st.sidebar.selectbox('Select Option', menu_options)

    if selected == 'Overview Project':
        overview()
    if selected == 'Prediction':
        klasifikasi()


if __name__ == '__main__':
    main()
    st.set_option('deprecation.showPyplotGlobalUse', False)