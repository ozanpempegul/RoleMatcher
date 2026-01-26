import os
from openai import OpenAI
from typing import Optional, List, Dict, Any, Union
from models.job import Job
from managers.file_manager import file_manager



def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not found in environment")
    return key


class ChatManager:
    """
    Manages OpenAI ChatCompletion interactions.
    """

    def __init__(
        self,
        model: str = "gpt-5-mini",
        max_completion_tokens: int = 4000,
    ):
        self.model = model
        self.max_completion_tokens = max_completion_tokens
        self.client = OpenAI(api_key=get_api_key())


    def _call_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_completion_tokens=self.max_completion_tokens,
        )
        content = response.choices[0].message.content
        print("API response content: ", content)
        return content
    

    def tailor_resume(self, 
                      job: Job,
                      cv_text: str,
                      ) -> str:
        prompt = self._build_tailor_resume_prompt(
            cv_text, job.description
        )
        print("Tailor resume prompt: ", prompt)
        result = self._call_api(prompt)
        return result
    

    def _build_tailor_resume_prompt(self, 
                      cv_text: str, 
                      job_description: str
                      ) -> str:
        prompt = (f"""
            You are an expert resume writer who tailors resumes to job descriptions using Harvard Style format.

            Job description:
            {job_description}

            Candidate summarized CV (plain text):
            {cv_text}

            Instructions:
            You are a resume HTML generator tasked with producing a Harvard Style resume that aligns closely with a given job description. Harvard Style resumes follow a specific format and structure. Please follow the rules below:

            1. **Output Format:**
            - Return only one HTML fragment.
            - Allowed tags: <p>, <ul>, <ol>, <li>, <strong>, <em>, <br>, <hr>.
            - No <script>, no external CSS, and no wrapper elements.
            - Inline styles are required.
            - Use clean, minimal layout with consistent spacing.

            2. **Visual Styling:**
            - Normal text and list items: style="font-size:10pt; margin: 0; padding: 0;"
            - Section titles (left-aligned, bold, uppercase): <p style="font-size:11pt; font-weight:bold; text-transform:uppercase; margin-top:8pt; margin-bottom:4pt;"><strong>SECTION NAME</strong></p>
            - Name (centered, larger font): <p style="text-align:center; font-size:16pt; font-weight:bold; margin-bottom:4pt;"><strong>Full Name</strong></p>
            - Contact info (centered, single line): <p style="text-align:center; font-size:10pt; margin-bottom:8pt;">Email | Phone | City, State</p>
            - Major sections separated by: <hr style="border:0; border-top:1px solid #000; margin:8pt 0;">

            3. **Section Order (MANDATORY Harvard Style order):**
            The sections MUST appear in this exact order:
            a) Contact Information (Name and Contact)
            b) Education (comes BEFORE Experience in Harvard style)
            c) Experience (work experience in reverse chronological order)
            d) Leadership & Activities (mandatory Harvard section - include if available in CV)
            e) Skills (optional, include if relevant to job)

            4. **Contact Information Section:**
            - Name centered at top with larger, bold font
            - Contact details centered below name: Email | Phone | City, State
            - No photos, age, gender, or sensitive information

            5. **Education Section (comes BEFORE Experience):**
            - Format: <p style="font-size:11pt; font-weight:bold; margin-top:8pt; margin-bottom:2pt;"><strong>EDUCATION</strong></p>
            - For each degree (reverse chronological order):
            <p style="font-size:10pt; margin: 0; padding: 0;"><strong>Degree Name</strong>, Institution Name, Location</p>
            <p style="font-size:10pt; margin: 0; padding: 0; font-style:italic;">Month Year – Month Year (or "Expected Month Year" if ongoing)</p>
            - Include honors/distinctions in italics on same line: <em>magna cum laude</em>, <em>Dean's List</em>, etc.
            - Example:
            <p style="font-size:10pt; margin: 0; padding: 0;"><strong>Bachelor of Science in Computer Science</strong>, University Name, City, State</p>
            <p style="font-size:10pt; margin: 0; padding: 0; font-style:italic;">September 2018 – May 2022 | <em>magna cum laude</em></p>

            6. **Experience Section (reverse-chronological order):**
            - Format: <p style="font-size:11pt; font-weight:bold; text-transform:uppercase; margin-top:8pt; margin-bottom:4pt;"><strong>EXPERIENCE</strong></p>
            - For each role:
            <p style="font-size:10pt; margin: 0; padding: 0;"><strong>Job Title</strong> | Company Name, Location</p>
            <p style="font-size:10pt; margin: 0; padding: 0; font-style:italic;">Month Year – Month Year (or "Present" if current)</p>
            <ul style="font-size:10pt; margin: 4pt 0; padding-left: 20pt;">
            <li style="margin: 2pt 0;">Action verb bullet point with quantifiable results</li>
            <li style="margin: 2pt 0;">Another outcome-oriented achievement</li>
            </ul>
            - Use action verbs (developed, implemented, managed, etc.)
            - Emphasize measurable outcomes and quantifiable achievements
            - Tailor bullets to match job description keywords and requirements

            7. **Leadership & Activities Section (MANDATORY for Harvard Style):**
            - Format: <p style="font-size:11pt; font-weight:bold; text-transform:uppercase; margin-top:8pt; margin-bottom:4pt;"><strong>LEADERSHIP & ACTIVITIES</strong></p>
            - Include student organizations, elected offices, volunteer work, clubs, etc.
            - Format similar to Experience:
            <p style="font-size:10pt; margin: 0; padding: 0;"><strong>Role/Position</strong> | Organization Name, Location</p>
            <p style="font-size:10pt; margin: 0; padding: 0; font-style:italic;">Month Year – Month Year</p>
            <ul style="font-size:10pt; margin: 4pt 0; padding-left: 20pt;">
            <li style="margin: 2pt 0;">Key achievement or responsibility</li>
            </ul>
            - If no leadership/activities in CV, create a minimal section or skip if truly none exist

            8. **Skills Section (Optional but recommended if relevant):**
            - Format: <p style="font-size:11pt; font-weight:bold; text-transform:uppercase; margin-top:8pt; margin-bottom:4pt;"><strong>SKILLS</strong></p>
            - List relevant technical skills, languages, software, etc. that match the job description
            - Format as comma-separated or bullet list:
            <p style="font-size:10pt; margin: 0; padding: 0;">Programming Languages: Python, JavaScript, Java | Frameworks: React, Django | Tools: Git, Docker</p>

            9. **Content Guidelines:**
            - Use active voice and action verbs throughout
            - Emphasize quantifiable achievements (numbers, percentages, metrics)
            - Tailor content to match job description keywords and requirements
            - Do not fabricate skills, positions, or achievements
            - Keep to one page if possible (prioritize most relevant content)
            - Use consistent date format: "Month Year" (e.g., "September 2020")
            - Avoid personal pronouns (I, me, my)
            - No abbreviations unless standard (e.g., "USA" is fine, but spell out company names)

            10. **Matching Score:**
            - Estimate a matching score (0-100) between the job description and candidate CV.
            - Include it as an HTML comment **at the very end** of the HTML fragment like this:
            <!-- MATCHING_SCORE: 87 -->
            - Do not include the score anywhere else in the HTML.

            11. **Output Restrictions:**
            - Return **only the HTML fragment** following Harvard Style format above.
            - Sections MUST be in this order: Contact → Education → Experience → Leadership & Activities → Skills
            - Do not include explanations, placeholders, or extra text.
            - Ensure clean, professional appearance suitable for PDF conversion.
            """
        )
        return prompt


    def generate_cover_letter(
        self,
        job: Union[Job, str],
        cv_text: str,
        max_length_words: Optional[int] = 500,
    ) -> str:
        job_description = job.description if hasattr(job, "description") else str(job)
        prompt = self._build_generate_cover_letter_prompt(cv_text, job_description, max_length_words)
        result = self._call_api(prompt)
        return result
    

    def _build_generate_cover_letter_prompt(self, 
                                            cv_text: str, 
                                            job_description: str, 
                                            max_length_words: Optional[int] = 350
                                            ) -> str:
        prompt = f"""
        You are an expert career writer. Given a short candidate CV summary and a job description, produce a single, professional, first-person cover letter tailored to the job.

        Job description:
        {job_description}

        Candidate summarized CV (plain text):
        {cv_text}

        Requirements and instructions:
        - The cover letter MUST start exactly with: "Dear Recruiter," as the very first line.
        - Format requirements to ensure PDF converts paragraphs correctly:
          * Wrap the entire cover letter in a single wrapper element only: <div style="font-size:10pt;">...HTML content...</div>
          * Inside that single wrapper, use explicit paragraph tags for separation. Specifically:
        - Put "Dear Recruiter," in its own paragraph: <p>Dear Recruiter,</p>
        - Use 2-3 short paragraphs for the body, each enclosed in its own <p>...</p>.
        - Place the sign-off block in a separate paragraph tag after the closing paragraph. The sign-off paragraph should contain:
          Best regards,<br>
          &lt;Full Name&gt;
          where &lt;Full Name&gt; is the candidate's name from the CV summary (field 'name') or "Candidate" if absent.
          * Do NOT omit paragraph tags or rely only on line breaks; paragraph tags are required so PDF renderers keep separate blocks.
          * Do not add any other wrapper elements or surrounding metadata outside the single <div> wrapper.
        - Structure the letter content into 2-3 short paragraphs:
          1) Opening: 1-2 sentences showing interest and fit.
          2) Body: 2-3 sentences linking specific achievements/skills from the CV summary to the job requirements.
          3) Closing: 1-2 sentences with a call-to-action.
        - Use a professional, confident tone in first-person. Do NOT mention the company by name.
        - Naturally include 3-8 relevant keywords/skills from the job description within the letter.
        - Do NOT fabricate experience, skills, metrics, or facts not present in the CV summary. Rephrase and prioritize only what aligns with the job.
        - Keep the letter to at most {max_length_words} words.
        - Return ONLY the cover letter as the single HTML string described above (the <div> wrapper containing inner <p> paragraphs and the sign-off). Do NOT include any analysis, JSON, headers, labels, explanations, or any extra text before or after the HTML. Return nothing else.
        """
        return prompt


    def summarize_resume(self,
                         resume_path: str
                         ) -> str:
        extracted = file_manager.extract_docx_text(resume_path)
        prompt = self._build_summarize_resume_prompt(extracted)
        result = self._call_api(prompt)
        file_manager.save_resume_summary(result)
        return result
    

    def _build_summarize_resume_prompt(self, resume_text: str) -> str:
        schema = """
        Produce a single valid JSON object that matches the following schema exactly.
        Do not invent accomplishments or metrics; if a fact is not present, use null, empty list, or empty string.
        Return only the JSON object and nothing else.
        {
        "profile": {
            "name": "<string|null>",
            "email": "<string|null>",
            "phone": "<string|null>",
            "location": "<string|null>",
            "title": "<string|null>",
            "one_line_summary": "<string|null>",
            "years_experience": <number|null>
        },
        "skills": {
            "languages": [<strings>],
            "frameworks": [<strings>],
            "infra": [<strings>],
            "other": [<strings>]
        },
        "experience": [
            {
            "role": "<string|null>",
            "company": "<string|null>",
            "start": "<YYYY-MM|null>",
            "end": "<YYYY-MM|null>",
            "bullets": [<strings>],
            "metrics": <object|null>
            }
        ],
        "education": [<strings>],
        "projects": [{"name":"<string>","desc":"<string>","link":"<string|null>"}],
        "keywords": [<strings>],
        "availability": "<string|null>",
        "notes": "<string|null>"
        }
        """
        prompt = f"{schema}\n\nResume:\n{resume_text}\n\nReturn only the JSON object."
        return prompt


chat_manager = ChatManager()


if __name__ == "__main__":
    # Test summarize_resume

    prompt = """
Job description:
**About solarVis**




 SolarVis is a dynamic, fast\-growing B2B SaaS startup revolutionizing the sustainable energy landscape. We are leading the digital transformation of the energy value chain by offering innovative software solutions that streamline the sales and marketing processes of businesses installing electrification products such as solar systems, EV chargers, batteries, and heat pumps. Think of us as the Salesforce and SAP of Sustainable Energy.










**About the Position**




 As a rapidly growing company, solarVis is looking for a Software Engineer to join our team in our Ankara office, located in the relaxed and vibrant environment of ODTÜ TEKNOKENT CoZone.










**Here’s what you will be doing:**



* Collaborate to design and implement robust and scalable web applications
* Develop frontend interfaces with a focus on user experience, ensuring responsiveness and compatibility across devices
* Write clean, efficient, and well\-documented code while adhering to industry best practices and coding standards
* Troubleshoot and debug issues, ensuring the timely resolution of bugs and other technical challenges









**Education \& Work Experience \& Technical Requirements:**



* Based in Ankara, Türkiye
* Bachelor’s/Master’s degree in Engineering, Computer Science (or equivalent experience)
* 2\+ years of software engineering and hands\-on programming experience
* Experience in architecting component libraries, building reusable UI components
* Extensive experience working with Python
* Practical experience working with ReactJS
* Familiarity with modern software development lifecycle and infrastructure tools (Git, Docker, AWS, Vercel) is a plus
* Understanding of Object\-Oriented Programming (OOP) principles and practices
* Having knowledge of FastAPI is a plus
* Having knowledge of NextJS is a plus
* Having knowledge of TypeScript is a plus
* Having knowledge of cache mechanism and Redis is a plus
* Having knowledge of game development basics is a plus
* Excellent conversational and written English communication skills









**Personal Specifications/Skills:**



* Demonstrate a strong capability for end\-to\-end execution
* Being self\-guided and being able to take on increasing responsibilities with enthusiasm
* Adaptability to rapidly changing conditions and a strong problem\-solving attitude
* Good team player, result oriented attitude and analytical mind









**We Offer**



* Competitive compensation package
* Private medical insurance
* A chance to be part of a passionate and driven team dedicated to making a difference
* Access to cutting\-edge technologies and tools to enhance your development skills
* Supportive and collaborative team environment that encourages learning and growth
* Opportunities to work on diverse and challenging projects with a real impact
* Room for creativity and autonomy in your projects, fostering innovation









**Hiring Process**



* **Phone Call:**
 A brief phone call with one of the Founders to pre\-evaluate your situation and assess your fit for the position. (15 mins)
* **Non\-Technical Interview with Founders:**
 Focused on your background, mindset, and expectations. (30 mins)
* **Case Study:**
 You will receive a case study after the interview. (7 days to complete)
* **Technical Interview:**
 A technical interview with the team, including case assessment and live coding. (120 mins)
* **Offer Stage:**
 Final alignment and offer delivery.

Candidate summarized CV (plain text):
{'meta': {'id': '117c0502-fd01-4b1e-bbea-f62e09a48e5a', 'seniority': None, 'preferred_role': 'Software Developer', 'location_preferences': 'Ankara, Turkey', 'redacted': True}, 'profile': {'name': 'Ozan Pempegül', 'phone': '+90 538 430 6794', 'email': 'ozanpembegul@gmail.com', 'title': 'Software Developer', 'one_line_summary': 'Geological engineer living in Ankara, Turkey, who transitioned into software development', 'years_experience': None}, 'skills': {'languages': ['English (Advanced)', 'Turkish (Native Language)'], 'frameworks': [], 'infra': [], 'other': ['LabVIEW', 'Python', 'Written Communication', 'Problem Solving']}, 'experience': [{'role': 'Software Developer', 'company': 'NanoMagnetics Instruments', 'start': '11/2023', 'end': 'Present', 'bullets': ['Built three desktop apps in Python to replace old LabVIEW-based apps', 'Communicated directly with customers to understand what they needed, gathered feedback, and turned it into features they actually used'], 'metrics': None}, {'role': 'Systems Engineer', 'company': 'NanoMagnetics Instruments', 'start': '01/2023', 'end': '11/2023', 'bullets': ['Worked with complex measurement systems and researched and gained a solid understanding of their underlying physics', 'Prepared technical documentation, calibration procedures'], 'metrics': None}, {'role': 'Volunteer Assistant', 'company': 'Patika.dev', 'start': '05/2022', 'end': '01/2023', 'bullets': ['Solved weekly coding challenges and participated in discussions for better solutions', 'Helped beginners who were struggling with problems by guiding them towards the solution'], 'metrics': None}], 'education': [{'Degree': "Bachelor's", 'Department': 'Geological Engineering', 'University': 'Middle East Technical University', 'Location': 'Ankara, Turkey', 'Start': '09/2014', 'End': '07/2023'}], 'projects': [], 'keywords': [], 'availability': None, 'notes': None, 'raw_text_snippet': None}

Instructions:

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
            - If you cannot summarize, return the reason why.

"""
    summary = chat_manager._call_api(prompt)
    print("Resume Summary:\n", summary)