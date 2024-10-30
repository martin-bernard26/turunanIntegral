import streamlit as st
from sympy import *

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
    
