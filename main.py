import streamlit as st

col1, col2 = st.columns(2)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

tab1, tab2, tab3 = st.tabs(["Cat"
,
"Dog"
,
"Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# Eine Überschrift der ersten Ebene
st.write("# Gerätemanagement")
# Eine Überschrift der zweiten Ebene
st.write("## Geräteauswahl")
# Eine Auswahlbox mit hard-gecoded Optionen, das Ergebnis
# wird in current_device_example gespeichert
current_device_example = st.selectbox(
'Gerät auswählen'
,
options = ["Gerät_A"
,
"Gerät_B"], key=
"sbDevice_example")
st.write(F"Das ausgewählte Gerät ist {current_device_example}")

if current_device_example == "Gerät_A":
    st.write("Test")

    