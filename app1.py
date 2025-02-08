import streamlit as st
from sympy import *

st.markdown("""
<style>
#kalkulator-fungsi-turunan-dan-integral{
    font-family:"bauhaus 93";
    color:green;
    text-shadow:2px 2px 2px red;
}
._iframe_nim44_26{
    background-image:url("https://img1.picmix.com/output/stamp/normal/6/4/7/2/1652746_f4f68.gif");
    background-repeat: no-repeat;
    background-size: cover;
}
</style>
""",unsafe_allow_html=True)
st.title("Kalkulator Fungsi Turunan dan Integral")
st.header("Turunan")
masukan = st.text_input("Masukan persamaan")
x, y = symbols(r'x y')
if masukan!="":
    masukan=sympify(masukan)
    turunan=diff(masukan,x)
    st.header("Fungsi")
    pers1 = Eq(y,masukan)
    st.latex(latex(pers1))
    st.header("Hasil Turunan")
    pers2 = Eq(Derivative(y,x),turunan)
    st.latex(latex(pers2))

st.header("Integral")
masukan1 = st.text_input("Masukan Fungsi")
if masukan1!="":
    masukan1=sympify(masukan1)
    integral=Integral(masukan1,x)
    st.header("Fungsi")
    pers1 = Eq(y,masukan1)
    st.latex(latex(pers1))
    st.header("Hasil Integral")
    pers2=Eq(integral,integral.doit())
    st.latex(latex(pers2))
    
