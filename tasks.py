from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

## Research Task
research_task = Task(
    description=(
        'Analyze the YouTube video from this URL {YT_URL} '
        'Extract key insights, important points, and structured understanding from the tools'
        
    ),
    expected_output='A comprehensive 5 bullet points only, max 100 words report with key insights based on the transcript of youtube video url {YT_URL} from the video transcript',
    agent=blog_researcher,
    tools = [yt_tool]
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
    #tools = [yt_tool],
    context=[research_task]   # VERY IMPORTANT (agent 1 → agent 2 flow)
)