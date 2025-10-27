import json
import uuid
from datetime import datetime
import os
import re
from pathlib import Path
from docx import Document
from common.imports.log import*
from PySide6.QtCore import Signal, QThread



class FileManager(QThread):

    signal_last_summary_json_loaded = Signal(dict)

    def __init__(self):
        super().__init__()
        self.last_summary_data = None
        self._load_last_summary_json()


    def extract_docx_text(self, path: str) -> str:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text and p.text.strip())


    def save_resume_summary(self,
                            summary_data: dict,
                            ):
        summary = json.loads(summary_data)        
        # save the finalized summary JSON before returning
        summary_json_str = json.dumps(summary, ensure_ascii=False)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}.json"

        os.makedirs("summaries", exist_ok=True)
        if not filename:
            filename = f"{uuid.uuid4()}.json"
        if not filename.endswith(".json"):
            filename += ".json"
        path = os.path.join("summaries", filename)

        obj = json.loads(summary_json_str)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)

        self._load_last_summary_json()
        return path
    

    def _find_last_summary_path(self):
        cwd = Path.cwd()
        module_dir = Path(__file__).resolve().parent

        search_roots = []
        for p in [cwd, *cwd.parents, module_dir, *module_dir.parents]:
            if p not in search_roots:
                search_roots.append(p)

        for root in search_roots:
            summaries_dir = root / "summaries"
            if summaries_dir.is_dir():
                json_files = [f for f in summaries_dir.iterdir() if f.is_file() and f.suffix.lower() == ".json"]
                if not json_files:
                    return None
                json_files.sort(key=lambda p: p.name)
                _path = str(json_files[-1])
                return _path

        return None
    

    def _load_last_summary_json(self) -> dict | None:
        try:
            _path = self._find_last_summary_path()
            if not _path:
                return None
            self.last_summary_data = json.loads(Path(_path).read_text(encoding="utf-8-sig"))
            self.signal_last_summary_json_loaded.emit(self.last_summary_data)
            return self.last_summary_data
        except Exception as e:
            logging.error(f"Error reading last summary JSON: {e}")
            return None
        
    
    def get_last_summary_json(self) -> dict | None:
        return self.last_summary_data
    

    def save_tailored_resume(self, content: str, filename: str) -> str:
        os.makedirs("tailored_resumes", exist_ok=True)
        if not filename:
            filename = f"{uuid.uuid4()}.txt"
        if not filename.endswith(".txt"):
            filename += ".txt"
        path = os.path.join("tailored_resumes", filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path
    

file_manager = FileManager()