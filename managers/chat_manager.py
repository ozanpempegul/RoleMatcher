import os
from openai import OpenAI
from typing import Optional, Union
from common.paths import prompts_dir
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
        self._prompt_cache: dict[str, str] = {}


    def _load_prompt_template(self, name: str) -> str:
        if name not in self._prompt_cache:
            path = prompts_dir() / f"{name}.txt"
            if not path.is_file():
                raise FileNotFoundError(f"Prompt template not found: {path}")
            self._prompt_cache[name] = path.read_text(encoding="utf-8-sig")
        return self._prompt_cache[name]


    def _render_prompt(self, name: str, **values: str) -> str:
        prompt = self._load_prompt_template(name)
        for key, value in values.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", str(value))
        return prompt


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
        return self._render_prompt(
            "tailor_resume",
            job_description=job_description,
            cv_text=cv_text,
        )


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
        return self._render_prompt(
            "cover_letter",
            job_description=job_description,
            cv_text=cv_text,
            max_length_words=max_length_words,
        )


    def summarize_resume(self,
                         resume_path: str
                         ) -> str:
        extracted = file_manager.extract_docx_text(resume_path)
        prompt = self._build_summarize_resume_prompt(extracted)
        result = self._call_api(prompt)
        file_manager.save_resume_summary(result)
        return result
    

    def _build_summarize_resume_prompt(self, resume_text: str) -> str:
        return self._render_prompt(
            "summarize_resume",
            resume_text=resume_text,
        )


chat_manager = ChatManager()
