from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

## Research Task
research_task = Task(
    description=(
        "Summarize the YouTube video url {YT_URL} transcript  into ONLY 4 bullet points. "
        "Max 40 words total. No extra explanation."
        
    ),
    expected_output='4 short bullet points only.',
    agent=blog_researcher,
    tools = [yt_tool],
    max_tokens=120
)


## Writing task with language model config
write_task = Task(
    description=(
        "Using research insights, write a clean SEO-friendly blog.\n"
        "Rules:\n"
        "- Markdown only\n"
        "- No HTML, no iframe, no embed\n"
        "- No repetition\n"
        "- Add a catchy title\n"
        "- 3 sections only: Intro, Body, Conclusion"
    ),
    expected_output="A well structured blog post in markdown format with title, "
        "clear sections and conclusion",
    agent=blog_writer,
    async_execution=False,  # sequential execution
    output_file='new-blog-post.md',  # blog file save hoga
    max_tokens=150,
    context=[research_task]   # VERY IMPORTANT (agent 1 → agent 2 flow)
)