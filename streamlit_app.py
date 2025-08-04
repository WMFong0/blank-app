import datetime
import streamlit as st

import streamlit as st
import pytz

# Initialize session state variables
if "inside_clock" not in st.session_state:
    st.session_state.inside_clock = False

if "timezone" not in st.session_state:
    st.session_state.timezone = None

def Clock():
    st.title("Live Clock")

    # Validate timezone
    if not st.session_state.timezone:
        st.error("No timezone selected. Please go back and select a timezone.")
        if st.button("Back to Timezone Selection"):
            st.session_state.inside_clock = False
            st.rerun()
        return

    try:
        timezone = pytz.timezone(st.session_state.timezone)
    except pytz.exceptions.PytzError:
        st.error("Invalid timezone selected. Please go back and select a valid timezone.")
        if st.button("Back to Timezone Selection"):
            st.session_state.inside_clock = False
            st.rerun()
        return

    # JavaScript code for the real-time clock
    js_code = f"""
    <div id="clock" style="font-size: 48px; font-family: 'Orbitron', sans-serif; color: #66ff99; text-align: center; padding: 20px;">
        Loading...
    </div>
    <script>
        function updateClock() {{
            const now = new Date();
            const options = {{
                timeZone: '{st.session_state.timezone}',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: true
            }};
            const timeString = now.toLocaleTimeString('en-US', options);
            document.getElementById('clock').innerText = `{st.session_state.timezone}: ${{timeString}}`;
        }}
        updateClock(); // Initial call
        setInterval(updateClock, 1000); // Update every second
    </script>
    <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
    """

    # Embed the JavaScript clock in Streamlit
    st.components.v1.html(js_code, height=150)

    # Back button to return to timezone selection
    if st.button("Back to Timezone Selection"):
        st.session_state.inside_clock = False
        st.rerun()

# Main app logic
if not st.session_state.inside_clock:
    st.title("Timezone Selection")
    selected_timezone = st.selectbox("Select your timezone", [None] + list(pytz.all_timezones), index=0)
    st.write(f"Selected: {selected_timezone}")

    # Disable button if no timezone is selected
    if st.button("Go to Live Clock", disabled=not selected_timezone):
        st.session_state.timezone = selected_timezone
        st.session_state.inside_clock = True
        st.rerun()
else:
    Clock()
