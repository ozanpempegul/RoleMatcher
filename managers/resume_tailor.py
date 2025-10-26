import os
import json
from typing import Optional, List, Dict, Any, Union
from openai import OpenAI
from models.job import Job
from managers.html_to_pdf_converter import html_to_pdf_converter


# /c:/Users/ozanp/GitRepos/job_alerts/managers/resume_tailor.py
# Basic OpenAI connection example. Assumes .env was already loaded and contains OPENAI_API_KEY.
# Requires: pip install openai


def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not found in environment")
    return key


class ResumeTailor:
    """
    Tailor a summarized CV to one or many job descriptions using OpenAI ChatCompletion.
    Methods return structured dicts; if the model doesn't produce JSON, the raw assistant text is returned.
    """

    def __init__(
        self,
        model: str = "gpt-5-mini",
        max_tokens: int = 800,
        temperature: float = 0.0,
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    
    def _start_pipeline(self, job: Job, cv_text: str, max_length: Optional[int] = 350):
        html_text = self.tailor_one(job, cv_text, max_length=max_length)
        print("Generated HTML Resume:\n", html_text)
        html_to_pdf_converter.convert(output_path="output.pdf", html_text=html_text)


    def _build_prompt(
        self, cv_text: str, job_description: str, max_length: Optional[int] = 350
    ) -> str:
        """
        Build a clear instruction prompt that requests JSON output with keys:
        - tailored_resume: the resume text tailored to the job (ideally formatted with bullets).
        - summary_of_changes: short bullet list of what was changed and prioritized.
        - keywords: list of 8-15 keywords from the job description to include.
        """
        prompt = (
            "You are an expert resume writer who tailors resumes to job descriptions.\n\n"
            "Job description:\n"
            f"{job_description}\n\n"
            "Candidate summarized CV (plain text):\n"
            f"{cv_text}\n\n"
            "Instructions:\n"
            f"""
            You are a resume HTML generator tasked with producing a concise, reverse-chronological CV section that aligns closely with a given job description. Please follow the rules below:

            1. **Output Format:**
            - **Return only one HTML fragment.**
            - Allowed tags: `<p>`, `<ul>`, `<ol>`, `<li>`, `<strong>`, `<em>`, `<br>`, `<hr>`.
            - No `<script>`, no external CSS, and no wrapper elements.
            - Inline styles are required.

            2. **Visual Styling:**
            - Normal text and list items: `style="font-size:10pt;"`
            - Section titles: `<p style="text-align:center; font-size:12pt;"><strong>Section Name</strong></p>`
            - Name: `<p style="text-align:center; font-size:16pt;"><strong>Full Name</strong></p>`
            - Contact info: Single centered line `<p style="text-align:center; font-size:10pt;">Email | Phone | Location</p>`
            - Major sections are separated by: `<hr style="border:0; border-top:1px solid #000;">`

            3. **Summary Section:**
            - **Include a Summary** section directly after the Contact Info.
            - The Summary should be a brief paragraph (2-3 sentences) that:
                - **Highlights the most relevant skills, experiences, and qualifications** from the candidate’s profile that align with the job description.
                - **Mentions specific keywords or skills** requested in the job description, such as technical proficiencies, core competencies, or industry knowledge (without mentioning the company name).
                - **Avoid company-specific references**; instead, focus on the value the candidate brings to a role similar to the job they're applying for.
                - The tone should be **tailored** to the job description, implying the candidate’s interest in the role and demonstrating how their background makes them a strong fit.

            4. **Experience Section (reverse-chronological):**
            - For each role in the provided resume, include the following details:
                - `<p style="font-size:12pt;"><strong>Role Title</strong></p>`
                - `<p style="font-size:10pt;">Company Name – Location | Start Date – End Date</p>`
                - `<ul style="font-size:10pt;">`
                - `<li>Brief, fact-based, and relevant bullet point (outcome-oriented)</li>`
                - `<li>Another significant achievement or responsibility</li>`
                - `</ul>`
            - Ensure **all relevant experience** is included without omitting any significant information. Do not skip or leave out any job or achievement that could be beneficial.

            5. **Education Section (reverse-chronological, no bullets):**
            - `<p style="font-size:12pt;"><strong>Department Name</strong></p>`
            - `<p style="font-size:10pt;">School Name – Location | Start Date – End Date</p>`

            6. **Content Guidelines:**
            - **Rephrase** bullet points to emphasize measurable outcomes, responsibilities, or technical skills that directly align with the job description.
            - Do not fabricate new skills or positions.
            - **Limit the CV to ≤{max_length} words** while ensuring it is tailored and focused on outcomes.
            - Emphasize **quantifiable achievements**, **key skills**, and responsibilities that match the job description.
            - **Include all relevant experience** from the original resume. Ensure that each job listed is presented with the most relevant and impactful achievements.

            7. **Section Headers:**
            - Ensure proper **section headers** are included and formatted as follows:
                - **Name Section**: Display the full name centered at the top of the document.
                - **Contact Information Section**: Center the contact information below the name.
                - **Summary Section**: Directly below Contact Info, summarize the individual’s career focus and align with the job description.
                - **Experience Section**: For each job, list in reverse chronological order, ensuring all jobs from the original resume are included.
                - **Education Section**: Display all education in reverse chronological order.
            - Separate each major section using a horizontal rule (`<hr>`), as described in the Visual Styling section.

            8. **Output Restrictions:**
            - Return **only the HTML fragment** with the above specifications.
            - Do **not** include explanations, placeholders, or any extra text before or after the HTML.
            - Ensure each section is properly separated by a horizontal rule (`<hr>`) and formatted as described above.
            """
        )
        return prompt


    def _call_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=2000,
        )
        content = response.choices[0].message.content
        return content


    def tailor_one(
        self,
        job: Job,
        cv_text: str,
        max_length: Optional[int] = 350,
    ) -> str:
        """
        Tailor a single job description. Returns a dict:
        {
            "tailored_resume": str,
            "summary_of_changes": List[str],
            "keywords": List[str],
            "raw": str  # raw assistant text if parsing failed
        }
        """
        prompt = self._build_prompt(
            cv_text, job.description, max_length=max_length
        )
        print("Prompt to OpenAI:\n", prompt)
        result = self._call_api(prompt)
        return result


if __name__ == "__main__":
    # quick demo: replace with your actual CV summary and a job description
    example_cv = (
        "Software engineer with 5 years experience in backend development, Python, REST APIs, PostgreSQL, and cloud deployments. "
        "Led a small team, improved API latency by 40%, and contributed to CI/CD automation."
    )
    example_job = (
        "Senior Backend Engineer role. Looking for strong Python experience, building scalable REST APIs, "
        "Postgres performance tuning, cloud deployments (AWS), and mentoring junior engineers."
    )

    tailor = ResumeTailor(model="gpt-3.5-turbo", max_tokens=600, temperature=0.0)
    out = tailor.tailor_one(example_cv, example_job, max_length_words=300)
    print(json.dumps(out, indent=2, ensure_ascii=False))


resume_tailor = ResumeTailor()