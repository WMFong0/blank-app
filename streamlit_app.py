import streamlit as st

base = st.context.theme.type
if st.context.locale.startswith("en"):
  st.write("Hello there.") # The merely supported language atm
elif st.context.locale == 'zh-Hant':
  st.write("Sorry. We will try to provide support for Traditional Chinese as soon as possible.") # Will be provided later
else:
  st.write("Sorry. As of the current moment, we do not have any schedule supporting your preferred language. \n"
  +"The only language we support is English at the moment.")

with st.popover("Input Panel"):
    st.markdown("Welcome using Weather Report System." + "\n" +
            "This system uses Hong Kong Observatory Data to report data.")
    District = st.text_input(
        "Enter your Current District",
        placeholder = "E.g. Tuen Mun",
    )

display_district = "Weather Report" if not District else f"Weather Report in {District}"
st.header(display_district)
st.header(f"Weather Report" if District == "None" else f"Weather Report in {District}")


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
