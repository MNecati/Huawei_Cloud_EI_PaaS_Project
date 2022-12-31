
import numpy as np
import pandas as pd
import pickle
import streamlit as st

 
# If you are working on the cloud platform, you should replace the address here with the path on the cloud storage.
 #Read the model from pickle
loaded_model = pickle.load(open('C:/Users/pc/OneDrive/Masaüstü/k8 _proje_streamlit_frontent/data/trained_model.sav', 'rb'))


header = st.container()
dataset = st.container()
feauters = st.container()
modelTraining = st.container()


with header:
    st.title('Welcome to my awesome Random Forest Project')
    st.text('In this project, we measured that we can diagnose \nskin cancer based on the data we have.')

with dataset:
    st.header('Cilt Kanseri Dataset')
    st.text('We created our own dataset. \nHere you can see the first 21 line : ')

    # If you are working on the cloud platform, you should replace the address here with the path on the cloud storage.
    #Read the dataset from exel 
    dataframe=pd.read_excel(r"C:\Users\pc\OneDrive\Masaüstü\makine öğrenmesi\streamlit frontent\data\Cilt_Kanseri.xlsx")
    st.write(dataframe.head(21))
    st.header('Enter your values ​​for diagnostic estimate')


def ciltkanseri_prediction(input_data):
    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if (prediction[0] == 0): return 'The person is not skin cancer'

    else: return 'The person is skin cancer'
    

def main():

    
    Cinsiyet = st.selectbox("Specify gender : ",["Male","Female"])
     
    if Cinsiyet == "Male":
        Cinsiyet = 0
    if Cinsiyet == "Female":
        Cinsiyet = 1

    Kilo = st.text_input('Kilogram of person')
    Yaş = st.text_input('Age of Person')
    Genetik = st.selectbox("Does the patient have a troublesome hereditary history?  ",["yes","no"])

    if Genetik == "yes":
        Genetik = 1
    if Genetik == "no":
        Genetik = 0

    SigaraKullanimi = st.selectbox("Does the patient smoke?  ",["yes","no"])

    if SigaraKullanimi == "yes":
        SigaraKullanimi = 1
    if SigaraKullanimi == "no":
        SigaraKullanimi = 0
        
    KimyasalKullanimi = st.text_input('Chemical use dose')
    
    Cilt_Tonu = st.selectbox("Specify the patient's skin tone : ",["beige","white","brown","pink","black"])

    if Cilt_Tonu == "beige":
        Cilt_Tonu = 0
    if Cilt_Tonu == "white":
        Cilt_Tonu = 1
    if Cilt_Tonu == "brown":
        Cilt_Tonu = 2
    if Cilt_Tonu == "pink":
        Cilt_Tonu = 3
    if Cilt_Tonu == "black":
        Cilt_Tonu = 4

    BeslenmeŞekli = st.selectbox("Is the patient's nutritional status good?",["yes","no"])

    if BeslenmeŞekli == "yes":
        BeslenmeŞekli = 1
    if BeslenmeŞekli == "no":
        BeslenmeŞekli = 0

    Alerji = st.selectbox("Does the patient have allergies?",["yes","no"])
    
    if Alerji == "yes":
       Alerji = 1
    if Alerji == "no":
       Alerji = 0

    UV_Işinindeksi = st.text_input('Ultraviolet ray index (Max 16)')
    RadyasyonOrani = st.text_input('Radiation rate')
   
    YaraDurumu = st.selectbox("Is the patient's wound condition severe?",["yes","no"])

    if YaraDurumu == "yes":
       YaraDurumu = 1
    if YaraDurumu == "no":
       YaraDurumu = 0

    YaraBoyutu = st.text_input('Wound size')

    YaraRengi = st.selectbox("Specify the patient's wound color : ",["white","brown","red","pink","none"])

    if YaraRengi == "white":
        YaraRengi = 0
    if YaraRengi == "brown":
        YaraRengi = 1
    if YaraRengi == "red":
        YaraRengi = 2
    if YaraRengi == "pink":
        YaraRengi = 3
    if YaraRengi == "none":
        YaraRengi = 4

    YaraSayisi = st.text_input('Number of Wounds')



    #code for prediction

    diagnosis = ''

    #creating a button for Prediction

    if st.button('Skin Cancer Test Result'):
        diagnosis = ciltkanseri_prediction([Cinsiyet, Kilo, Yaş, Genetik, SigaraKullanimi, KimyasalKullanimi, Cilt_Tonu, BeslenmeŞekli, Alerji, UV_Işinindeksi, RadyasyonOrani, YaraDurumu, YaraBoyutu, YaraRengi, YaraSayisi])

    st.success(diagnosis)

if __name__ == '__main__':
    main()












