from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

## Research Task
research_task = Task(
    description=(
        "Analyze the YouTube video {YT_URL} transcript and extract:\n"
        "1. Main topic of the video\n"
        "2. 4-5 key points with specific details\n"
        "Max 120 words total."
    ),
    expected_output='Give 5 bullet points WITH specific details from the video transcript.',
    agent=blog_researcher,
    tools = [yt_tool],
    max_tokens=200
)


## Writing task with language model config
write_task = Task(
    description=(
        "Write a blog STRICTLY based on the research insights.\n"
        "IMPORTANT:\n"
        "- The blog MUST follow the exact topic from the video\n"
        "- DO NOT write about YouTube analysis or APIs\n"
        "- DO NOT add generic AI explanations\n"
        "- Use only provided insights\n\n"
        "Format:\n"
        "- Title\n"
        "- Intro\n"
        "- Body\n"
        "- Conclusion\n"
        "- Max 200 words"
    ),
    expected_output="A well structured blog post in markdown format with title, "
        "clear sections and conclusion",
    agent=blog_writer,
    async_execution=False,  # sequential execution
    output_file='new-blog-post.md',  # blog file save hoga
    max_tokens=3000,
    context=[research_task]   # VERY IMPORTANT (agent 1 → agent 2 flow)
)