import datetime
import streamlit as st

base = st.context.theme.type
if st.context.locale.startswith("en"):
  st.markdown("Hello there.") # The merely supported language atm
elif st.context.locale == 'zh-Hant':
  st.markdown("Sorry. We will try to provide support for Traditional Chinese as soon as possible.") # Will be provided later
else:
  st.markdown("Sorry. As of the current moment, we do not have any schedule supporting your preferred language. \n"
  +"The only language we support is English at the moment.")
st.markdown("Welcome using Weather Report System. <br>This system uses Hong Kong Observatory Data to report data.", unsafe_allow_html = True)

with st.popover("Current District Input Panel"):
    District = st.text_input(
        "Enter your Current District",
        placeholder = "E.g. Tuen Mun",
    )

st.title(f"Weather Report" if not District else f"Weather Report in {District}")

if not District:
  st.header("Please provide your current district using the Input Panel. Thanks.")
else:
  current_datetime = datetime.datetime.now().astimezone(datetime.timezone(datetime.timedelta(hours=8))); # Enforce Hong Kong Timezone
  st.markdown("Here are the information we gathered from HKO<br><br>" + current_datetime.strftime('Today is *%Y/%m/%d*. <br>Current Hong Kong Time is *%H:%M:%S*<br>'), unsafe_allow_html = True)

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
