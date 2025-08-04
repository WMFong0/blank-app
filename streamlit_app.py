import streamlit as st
import pytz

# Initialize session state variables
if "inside_clock" not in st.session_state:
    st.session_state.inside_clock = False

if "timezone" not in st.session_state:
    st.session_state.timezone = None

# Apply custom CSS for the clock UI
st.markdown("""
<style>
html, body {
    overflow: hidden !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}
.time-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh !important;
    width: 100vw !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
}
.big-time {
    font-size: 20vw !important;
    font-family: monospace;
    line-height: 1;
    white-space: nowrap;
    margin: 0;
    padding: 0;
}
.date-header {
    font-size: 3vw !important;
    margin-bottom: 2vh;
    color: #666;
}
.timezone-label {
    font-size: 2vw !important;
    color: #888;
    margin-top: 1vh;
}
.affiliate-label {
    font-size: 3vw !important;
    margin-bottom: 1vh;
    color: #777;
}
</style>
""", unsafe_allow_html=True)

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

    # Create an empty placeholder for the clock
    clock_container = st.empty()

    # JavaScript code for the real-time clock
    js_code = f"""
    <div class="time-container">
        <div id="date-header" class="date-header"></div>
        <div id="time" class="big-time"></div>
        <div id="timezone" class="timezone-label"></div>
    </div>
    <script>
        function updateClock() {{
            const now = new Date();
            const timeOptions = {{
                timeZone: '{st.session_state.timezone}',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: false
            }};
            const dateOptions = {{
                timeZone: '{st.session_state.timezone}',
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: '2-digit'
            }};
            const timeString = now.toLocaleTimeString('en-US', timeOptions);
            const dateString = now.toLocaleDateString('en-US', dateOptions);
            document.getElementById('time').innerText = timeString;
            document.getElementById('date-header').innerText = dateString;
            document.getElementById('timezone').innerText = '{st.session_state.timezone} Time';
        }}
        updateClock(); // Initial call
        setInterval(updateClock, 1000); // Update every second
    </script>
    """

    # Embed the JavaScript clock in the placeholder
    clock_container.html(js_code, height=600)

    # Back button to return to timezone selection
    if st.button("Back to Timezone Selection"):
        st.session_state.inside_clock = False
        st.rerun()

# Check boolean directly instead of using `in`
if not st.session_state.inside_clock:
    selected_timezone = st.selectbox("Select your timezone", [None] + list(pytz.all_timezones))
    st.write(f"Selected: {selected_timezone}")

    if st.button(f"Go to {selected_timezone}'s Live Clock" if selected_timezone else "Please select your timezone first", disabled=not selected_timezone):
        if selected_timezone:
            st.session_state.timezone = selected_timezone
            st.session_state.inside_clock = True
            st.rerun()
else:
    Clock()
