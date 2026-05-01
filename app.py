from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
import streamlit as st
import base64
import time

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    cache=True,
    verbose=True   # ✅ helpful for debugging
)


st.set_page_config(page_title="VideoToVibes", page_icon='image.png', layout="centered")
# ---------- HEADER ----------
def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_image_base64("image.png")

st.markdown(
    f"""
    <div style="display:flex; align-items:center; justify-content:center; gap:12px;">
        <img src="data:image/png;base64,{img_base64}" width="50">
        <h1 style="margin:0;">VideoToVibes AI</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("YouTube Video → Blog Generator")

video_url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Blog"):

    if not video_url:
        st.warning("Please enter a valid YouTube URL")
    else:
        with st.spinner("AI is analyzing video..."):

            try:
                time.sleep(10)
                result = crew.kickoff(
                    inputs={"YT_URL": video_url}
                )

                st.success("Blog Generated Successfully 🎉")

                st.markdown("## 📝 Generated Output")
                st.markdown(result.raw)

            except Exception as e:
                st.error(f"Error: {str(e)}")