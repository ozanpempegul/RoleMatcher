# ...existing code...
from docx import Document
import os
import re
import json
import uuid
from openai import OpenAI
from datetime import datetime
from PySide6.QtCore import Signal, QObject



class ResumeSummarizer(QObject):

    signal_resume_summarized = Signal(str)

    def __init__(self, model: str | None = "gpt-4"):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4")
        self.use_responses = "-chat" not in self.model

    def start_pipeline(self, resume_path: str) -> dict:
        text = self.extract_docx_text(resume_path)
        redacted = self.redact_pii(text)
        summary = self.summarize_resume(
            redacted, source_id=os.path.basename(resume_path)
        )
        print("summary keys:", list(summary.keys()))
        return summary

    def extract_docx_text(self, path: str) -> str:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text and p.text.strip())

    def redact_pii(self, text: str) -> str:
        # basic redaction: emails, phones
        text = re.sub(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", text
        )
        text = re.sub(
            r"\b(\+?\d{1,3}[-.\s]?)?(\(?\d{2,4}\)?[-.\s]?){1,3}\d{2,4}\b",
            "[REDACTED_PHONE]",
            text,
        )
        return text

    def build_prompt(self, resume_text: str, source_id: str) -> str:
        # Schema-only prompt: no job description included
        schema = """
Produce a single valid JSON object that matches the following schema exactly.
Do not invent accomplishments or metrics; if a fact is not present, use null, empty list, or empty string.
Return only the JSON object and nothing else.

{
  "meta": {
    "id": "<string>",
    "seniority": "<Senior|Mid|Junior|null>",
    "preferred_role": "<string|null>",
    "location_preferences": "<string|null>",
    "redacted": true
  },
  "profile": {
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
  "notes": "<string|null>",
  "raw_text_snippet": "<string|null>"
}
"""
        snippet = resume_text[:8000]  # keep prompt size reasonable
        prompt = f"{schema}\n\nResume (redacted, source_id={source_id}):\n{snippet}\n\nReturn only the JSON object."
        return prompt

    def save_string_as_json(self, content: str, filename: str | None = None) -> str:
        """Save a string as JSON to the summaries directory. If content is not valid JSON,
        it will be saved under {"raw": <content>}.
        Returns the path to the saved file.
        """
        os.makedirs("summaries", exist_ok=True)
        if not filename:
            filename = f"{uuid.uuid4()}.json"
        if not filename.endswith(".json"):
            filename += ".json"
        path = os.path.join("summaries", filename)

        try:
            obj = json.loads(content)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(obj, f, ensure_ascii=False, indent=2)
        except json.JSONDecodeError:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"raw": content}, f, ensure_ascii=False, indent=2)

        return path

    def summarize_resume(self, resume_text: str, source_id: str) -> dict:
        prompt = self.build_prompt(resume_text, source_id)
        print("Using model:", self.model)
        if self.use_responses:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=1500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            content = response.choices[0].message.content
        else:
            response = self.client.completions.create(
                model=self.model,
                prompt=prompt,
                temperature=0.0,
                max_tokens=1500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                n=1,
                stop=None,
            )
            content = response.choices[0].text

        try:
            summary = json.loads(content)
            if "meta" not in summary:
                summary["meta"] = {}
            summary["meta"]["id"] = str(uuid.uuid4())
            summary["meta"]["redacted"] = True

            # save the finalized summary JSON before returning
            summary_json_str = json.dumps(summary, ensure_ascii=False)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.json"
            saved_path = self.save_string_as_json(
                summary_json_str, filename=filename
            )
            print("Saved summary to:", saved_path)

            self.signal_resume_summarized.emit(saved_path)
            return summary
        except json.JSONDecodeError as e:
            print("Failed to parse JSON from model response:", e)
            print("Response content:", content)
            # save the raw model response for inspection
            saved_path = self.save_string_as_json(
                content, filename=f"failed_{uuid.uuid4()}.json"
            )
            print("Saved raw response to:", saved_path)
            return {"error": "Failed to parse JSON from model response."}


resume_summarizer = ResumeSummarizer()  # Module-level instance


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    models = client.models.list()
    for m in models:
        print(m.id)
