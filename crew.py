from crewai import Crew, Process
from agents import property_researcher, property_analyst
from tasks import research_task, analysis_task

crew = Crew(
    agents = [property_researcher, property_analyst],
    tasks = [research_task, analysis_task],
    verbose = True,
    process = Process.sequential
)

inputs = {
    "country": input("Enter the country of your choice: ")
}

result = crew.kickoff(inputs = inputs)

print("=====FINAL REPORT=====")
print(result.raw)