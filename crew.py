from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# Create Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    verbose=True   # helpful for debugging
)

# Run Crew
#result = crew.kickoff(
    #inputs={
        
        #"YT_URL": ""
    #}
#)


#print(result)