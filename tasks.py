from crewai import Task


class GenAITask():
    def industry_research_task(self, agent, industry_name):
        return Task(description=(f"""
        "Conduct a detailed market analysis for {industry_name}, "
        "including key trends, common challenges, and opportunities "
        "for AI/ML adoption. Identify major competitors and analyze "
        "their use of AI to enhance operations or customer experiences."
    """),
    expected_output=(
      f"""  "A comprehensive report outlining the market landscape for {industry_name}, "
        "highlighting key AI/ML trends, competitor analysis, and potential gaps "
        "for strategic AI integration."
    """),
    agent=agent,
)

    def use_case_generation_task(self, agent, company_name,industry_name):
        return Task(
    description=(
        f""" 
        "Generate tailored AI and Generative AI use cases for {company_name} "
        "in the {industry_name} industry. Each use case should align with the "
        "company’s strategic goals, such as improving customer satisfaction or "
        "optimizing operations, and should specify applicable AI/ML technologies."
        """
    ),
    expected_output=(
        f"""
        "A list of innovative, actionable use cases for AI/ML and Generative AI "
        "that {company_name} can implement, including expected benefits, "
        "recommended technologies, and considerations for feasibility."
        """
    ),
    agent=agent,
)
    
    def resource_collection_task(self, agent, company_name,industry_name):
        return Task(
    description=(f"""
        "Collect datasets, research articles, and code repositories relevant to the "
        "AI use cases proposed for {company_name} in {industry_name}. Include links "
        "to resources from platforms like Kaggle, Hugging Face, and GitHub, and "
        "organize them by specific use case."
        """
    ),
    expected_output=("""
        "An organized list of resources, including datasets and articles, that support "
        "the proposed AI use cases for {company_name}. Each entry should include a "
        "brief description and the link, ensuring relevance to specific use cases."
    """),
    agent=agent,
)