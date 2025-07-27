# Agentic-AI-Real-Estate-Investment 🤖 
## Retail Property Investment Analysis 🌆

## 📜 Overview

This project leverages CrewAI agents to conduct a comprehensive analysis of potential retail property investments in a specified country. The workflow automates research, financial analysis, risk assessment, and reporting, providing actionable insights for property investors.

## 🛠 Tech Stack
- Model used:  DeepSeek-R1-70B
- Framework: CrewAI

## 📁 Folder Structure 
retail_property_investemnt_project/
│
├── agents.py                # Defines CrewAI agents and LLM setup
├── tasks.py                 # Defines CrewAI tasks and workflow logic
├── main.py                  # Main script to run the CrewAI workflow
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys, etc.)
├── README.md                # Project documentation
│── research_task_output_internet.txt   # Research task output
└── task2_output.txt                    # Analysis task output

## 🚀 Features

- **Market Analysis:**  
  Identifies top retail property investment locations, analyzes market trends, economic indicators, demographics, and local retail ecosystems.

- **Property Evaluation:**  
  Assesses foot traffic, accessibility, proximity to complementary businesses, and local economic development plans.

- **Financial Analysis:**  
  Estimates rental yields, calculates projected ROI, assesses property valuation and appreciation, and identifies renovation opportunities.

- **Risk Assessment:**  
  Analyzes competitor landscape, evaluates e-commerce impact, regulatory challenges, and long-term growth barriers.

- **Detailed Reporting:**  
  Generates comprehensive reports with executive summaries, market insights, property recommendations, financial projections, risk analysis, and visual aids.

## Tasks

### 1. 🔍 Research Task

Conducts in-depth research and analysis, producing a data-driven investment recommendation report.  
**Deliverable:**  
- Market analysis summary  
- Top 3-5 recommended retail property investments  
- Comprehensive financial projections  
- Risk assessment  
- Recommendations for further due diligence

### 2. 📊 Analysis Task

Summarizes property information into a structured bullet-point list for each city, including:  
- City name  
- Mean price  
- Rental vacancy  
- Rental yield  
- Background information

## 💻Installation and Setup

1. **Install dependencies:**  
   ```bash
   pip install crewai
   ```

2. **Configure agents:**  
   Edit `agents.py` to define your property researcher and analyst agents.

3. **Run tasks:**  
   Execute your main script to generate the research and analysis reports.  
   Output files:
   - `research_task_output_internet.txt`
   - `task2_output.txt`

## 💾 Output Format

- **Research Report:**  
  Comprehensive, data-driven investment recommendation.

- **Analysis Summary:**  
  Bullet-point list for each city, formatted as:
  ```
  City 1: Name of the city
  Mean Price: $1,200,000
  Rental Vacancy: x%
  Rental Yield: y%
  Background Information: ...
  ```

## License

MIT

---

*For more details,
