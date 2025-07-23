import streamlit as st

with st.popover("Input Panel"):
    st.markdown("Welcome using Weather Report System." + "\n" +
            "This system uses Hong Kong Observatory Data to report data.")
    District = st.text_input(
        "Enter your Current District",
        label_visibility = "collapsed",
        placeholder = "E.g. Tuen Mun",
    )

st.header(f"Weather Report in {District}" if District != "None" else f"Weather App")


'''
tab1, tab2 = st.tabs(["Input Page", "Result Page"])

with tab1:
    st.header("Welcome using Weather Report System." + "\n" +
            "This system uses Hong Kong Observatory Data to report data.")
    District = st.text_input(
        "Enter some text 👇",
        label_visibility = "collapsed",
        placeholder = "Enter your Current District",
    )
with tab2:
    st.header(f"Weather Report in {District}" if District != None else f"Weather App")  # Using f-string for string interpolation
    # Do this this this
'''
