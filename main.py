from crewai import Crew
from textwrap import dedent
from agents import GenAIAgents
from tasks import GenAITask

from dotenv import load_dotenv
load_dotenv()

inputs={
    "company":"Honeywell",
    "industry":"Automation"
}


class GenerativeAIConsultant:
    def __init__(self, industry_name,company_name):
        self.industry= industry_name
        self.company= company_name

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = GenAIAgents()
        tasks = GenAITask()

        # Define your custom agents and tasks here
        industry_market_research_agent = agents.industry_market_research_agent()
        use_case_generation_agent = agents.use_case_generation_agent()
        resource_collection_agent = agents.resource_collection_agent()

        # Custom tasks include agent name and variables as input
        industry_market_research_task = tasks.industry_research_task(
            industry_market_research_agent,self.industry

        )

        use_case_generation_task = tasks.use_case_generation_task(
            use_case_generation_agent,
            self.industry,self.company
        )

        resource_collection_task = tasks.resource_collection_task(
            resource_collection_agent,self.company,self.industry
        )

        # Define your custom crew here
        crew = Crew(
            agents=[industry_market_research_agent,
                    use_case_generation_agent,
                    resource_collection_agent
                    ],
            tasks=[
                industry_market_research_task,
                use_case_generation_task,
                resource_collection_task
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')
    company = input(
        dedent("""
      From where will you be traveling from?
    """))
    industry = input(
        dedent("""
      What are the cities options you are interested in visiting?
    """))
    

    consulting_crew = GenerativeAIConsultant(company,industry)
    result = consulting_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)
