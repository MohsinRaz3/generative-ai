import streamlit as st
import time

# with st.empty():
#    # while True:
#         for second in range(4):
#             st.write(f"⏳ {second} left to end!")
#             time.sleep(1)
#         st.write("⛽ gas price is 73.23323 gwei")

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Clear all those elements:
