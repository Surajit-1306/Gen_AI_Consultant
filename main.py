import streamlit as st
from crewai import Crew
from crewai.process import Process
from agents import GenAIAgents
from tasks import GenAITask
from dotenv import load_dotenv
load_dotenv()

# Define the GenerativeAIConsultant class
class GenerativeAIConsultant:
    def __init__(self, industry_name, company_name):
        self.industry = industry_name
        self.company = company_name

    def run(self):
        # Define agents and tasks
        agents = GenAIAgents()
        tasks = GenAITask()

        # Create agent instances
        industry_market_research_agent = agents.industry_market_research_agent()
        use_case_generation_agent = agents.use_case_generation_agent()
        resource_collection_agent = agents.resource_collection_agent()

        # Define custom tasks
        industry_market_research_task = tasks.industry_research_task(
            industry_market_research_agent,self.company, self.industry
        )
        use_case_generation_task = tasks.use_case_generation_task(
            use_case_generation_agent, self.company,self.industry
        )
        resource_collection_task = tasks.resource_collection_task(
            resource_collection_agent, self.company, self.industry
        )

        # Set up Crew with agents and tasks
        crew = Crew(
            agents=[industry_market_research_agent,
                    use_case_generation_agent,
                    resource_collection_agent],
            tasks=[
                industry_market_research_task,
                use_case_generation_task,
                resource_collection_task
            ],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        return result

# Streamlit Application Interface
st.title("Generative AI Consultant")
st.subheader("Get tailored AI/ML use cases and resources for your company")

# Input fields
company = st.text_input("Enter the company name", "Honeywell")
industry = st.text_input("Enter the industry name", "Automation")

# Run the consultant and display the results
if st.button("Generate Insights"):
    consulting_crew = GenerativeAIConsultant(industry_name=industry, company_name=company)
    result = consulting_crew.run()

    st.write("## Analysis and Recommendations")
    st.write("Below are the insights generated for your company:")
    st.write(result)

