import streamlit as st
from sympy import *

st.markdown("""
<style>
#kalkulator-fungsi-turunan-dan-integral{
    font-family:"bauhaus 93";
    color:green;
    text-shadow:2px 2px 2px red;
}
section.stMain{
    background-image:url("https://i.pinimg.com/originals/f7/d0/02/f7d0021c7065e21a5f437f86686a6241.gif");
    background-repeat: no-repeat;
    background-size: cover;
}
#turunan{
    font-family:broadway;
    color:orange;
    text-shadow:2px 2px 2px black;
}
div.st-key-masukan1 p, div.st-key-masukan2 p{
    color:yellow;
    font-family:"comic sans ms";
    font-size:16px;
}
div.st-key-masukan1 div.st-ae{
    box-shadow: 0px 0px 0px 5px cyan;
}
#integral{
    color:white;
    font-family:broadway;
}
span.katex{
    background-color:yellow;
    padding:5px;
    border-radius:10px;
    border:2px solid blue;
}
div[data-testid="stSidebarContent"]{
    background-image:url("https://i.pinimg.com/originals/27/3f/7f/273f7f9663477fd4bb8420ef95c903d5.gif");
    background-repeat: no-repeat;
    background-size: cover;
}
div.etvjjhi0{
    color:white;
    font-family:"comic sans ms";
    font-size:20px;
}
div[data-testid="st.SidebarCollapseButton"] svg{
    background-color:orange;
}
</style>
""",unsafe_allow_html=True)
st.sidebar.text("Martin Bernard")
st.title("Kalkulator Fungsi Turunan dan Integral")
st.header("Turunan")
masukan = st.text_input("Masukan persamaan",key="masukan1")
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
masukan1 = st.text_input("Masukan Fungsi",key="masukan2")
if masukan1!="":
    masukan1=sympify(masukan1)
    integral=Integral(masukan1,x)
    st.header("Fungsi")
    pers1 = Eq(y,masukan1)
    st.latex(latex(pers1))
    st.header("Hasil Integral")
    pers2=Eq(integral,integral.doit())
    st.latex(latex(pers2))
    
