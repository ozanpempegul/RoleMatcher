import os
import json
from typing import Optional, List, Dict, Any, Union
from openai import OpenAI

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
        model: str = "gpt-3.5-turbo",
        max_tokens: int = 800,
        temperature: float = 0.0,
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def _build_prompt(
        self, cv_text: str, job_text: str, max_length_words: Optional[int] = 350
    ) -> str:
        """
        Build a clear instruction prompt that requests JSON output with keys:
        - tailored_resume: the resume text tailored to the job (ideally formatted with bullets).
        - summary_of_changes: short bullet list of what was changed and prioritized.
        - keywords: list of 8-15 keywords from the job description to include.
        """
        max_len_note = (
            f"Do not exceed {max_length_words} words in the tailored resume."
            if max_length_words
            else ""
        )
        prompt = (
            "You are an expert resume writer who tailors resumes to job descriptions.\n\n"
            "Job description:\n"
            f"{job_text}\n\n"
            "Candidate summarized CV (plain text):\n"
            f"{cv_text}\n\n"
            "Instructions:\n"
            "1) Produce a concise Harvard-style academic CV section (academic/Harvard template). "
            "Use reverse-chronological ordering"
            "Format section headings as <p><strong>Section Name</strong></p> followed by a <ul> of concise bullet <li> items. "
            "Prioritize job-relevant items; keep bullets short and factual. "
            f"{max_len_note}\n"
            "2) RETURN ONLY a single HTML fragment (no JSON, no markdown, no surrounding commentary). "
            "Only use these tags: p, ul, ol, li, strong, em, br. Do NOT include <script> or external CSS. Keep the HTML minimal and compact.\n\n"
            "If you cannot generate tailored content, return an empty string (i.e., no HTML).\n"
        )
        return prompt

    def _call_api(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.0,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        content = response.choices[0].message.content
        return content

    def tailor_one(
        self,
        cv_text: str,
        job_text: str,
        max_length_words: Optional[int] = 350,
    ) -> Dict[str, Any]:
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
            cv_text, job_text, max_length_words=max_length_words
        )
        assistant_text = self._call_api(prompt)
        result: Dict[str, Any] = {
            "raw": assistant_text,
            "tailored_resume": "",
            "summary_of_changes": [],
            "keywords": [],
        }

        # try to parse JSON from assistant_text
        try:
            parsed = json.loads(assistant_text)
            # merge parsed fields into result (be tolerant to missing keys)
            result["tailored_resume"] = parsed.get("tailored_resume", "")
            result["summary_of_changes"] = parsed.get("summary_of_changes", [])
            result["keywords"] = parsed.get("keywords", [])
        except json.JSONDecodeError:
            # If not valid JSON, attempt to extract a JSON substring
            try:
                start = assistant_text.index("{")
                end = assistant_text.rindex("}") + 1
                parsed = json.loads(assistant_text[start:end])
                result["tailored_resume"] = parsed.get("tailored_resume", "")
                result["summary_of_changes"] = parsed.get("summary_of_changes", [])
                result["keywords"] = parsed.get("keywords", [])
            except Exception:
                # leave as-is with raw text; optionally, place whole text into tailored_resume
                result["tailored_resume"] = assistant_text

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
