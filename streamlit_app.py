import streamlit as st

tab1, tab2 = st.tabs(["Input Page", "Result Page"])

With tab1:
    st.header("Welcome using Weather Report System." + "\n" +
            "This system uses Hong Kong Observatory Data to report data.")
    District = st.text_input(
        "Enter some text 👇",
        label_visibility = "collapsed",
        placeholder = "Enter your Current District",
    )

With tab2:
    st.header(f"Weather Report in {test}" if test != None else f"Weather App")  # Using f-string for string interpolation
    # Do this this this
