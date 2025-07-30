from crewai import Crew, Process
from agents import property_researcher, property_analyst
from tasks import research_task, analysis_task

def crew_compile(query: str):
    crew = Crew(
    agents = [property_researcher, property_analyst],
    tasks = [research_task, analysis_task],
    verbose = True,
    process = Process.sequential
    )

    inputs = {
    "country": f"Reviewing for {query}"
    }

    result = crew.kickoff(inputs = inputs)
    return result.raw
