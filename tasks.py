from crewai import Task


class GenAITask():
    def industry_research_task(self, agent, company_name,industry_name):
        return Task(description=(f"""
        "Conduct a detailed market analysis for {company_name} in this {industry_name} industry, "
        "including key trends, common challenges, and opportunities "
        "for AI/ML adoption. Identify major competitors and analyze "
        "their use of AI to enhance operations or customer experiences."
    """),
    expected_output=(
      f"""  "A comprehensive report outlining the market landscape for  {company_name} in this {industry_name} industry, "
        "highlighting key AI/ML trends, competitor analysis, and potential gaps "
        "for strategic AI integration."
    """),
    agent=agent,
)

    def use_case_generation_task(self, agent, company_name,industry_name):
        return Task(
    description=(
        f""" 
        "Generate tailored AI and Generative AI use cases for {company_name} in the {industry_name} industry. 

            Each use case should:
            1. Align with the company’s strategic goals,
            2. Clearly describe the potential benefits to the company (e.g., cost reduction, enhanced customer satisfaction, improved operational efficiency),
            3. Specify applicable AI/ML technologies and implementation considerations.

            The focus is on actionable and impactful use cases that demonstrate clear value to {company_name}."
            """
    ),
    expected_output=(
        f"""
        "A detailed list of AI/ML and Generative AI use cases for {company_name}, including:
            1. Descriptions and applications,
            2. Expected benefits,
            3. Alignment with strategic goals,
            4. Recommended technologies, and
            5. Key implementation considerations."
            """
    ),
    agent=agent,
)
    
    def resource_collection_task(self, agent, company_name,industry_name):
        return Task(
    description=(f"""
        "Collect datasets, research articles, and code repositories relevant to the 
            AI use cases proposed for {company_name} in {industry_name}. 

            Requirements:
            1. Only include resources with verified, functional links (test the links to ensure they are real).
            2. Prefer resources from well-known and reputable sources, such as Kaggle, Hugging Face, GitHub, or academic publishers.
            3. Avoid adding links to low-quality, unrelated, or fake content.
            4. Provide a clear description of why each resource is relevant.
            5. Organize the resources by the specific use case they support."
        """
    ),
    expected_output=("""
        "A curated list of high-quality resources, including datasets and articles, 
            that support the proposed AI use cases for {company_name}. Each entry includes:
            1. A brief description,
            2. A valid and verified link,
            3. Information about licensing or usage restrictions."
        """),
    agent=agent,
)