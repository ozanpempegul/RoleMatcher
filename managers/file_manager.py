import json
import uuid
from datetime import datetime
import os
from pathlib import Path
from docx import Document
from common.imports.log import*
from PySide6.QtCore import Signal, QThread
from xhtml2pdf import pisa  # type: ignore


class FileManager(QThread):

    signal_last_summary_json_loaded = Signal(dict)

    def __init__(self):
        super().__init__()
        self.last_summary_data = None
        self._tailored_resume_folder_name = "tailored_resumes"
        self._cover_letter_folder_name = "cover_letters"
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
    
    
    def save_tailored_resume_as_pdf(self,
                                    html_text: str = None,
                                    output_folder_name: str = None
                                    ) -> str:
        """
        output_folder_name: str -> name of the output folder.
        Convert HTML to PDF and write to output_path.
        Returns the output_path on success.
        """
        # xhtml2pdf doesn't accept many options like other libs; we support basic conversion.
        if html_text is None:
            raise RuntimeError("No content to convert for xhtml2pdf")
        
        if output_folder_name is None:
            raise RuntimeError("Output folder name must be provided")
        else:
            output_folder_name = str(output_folder_name)

        os.makedirs(output_folder_name, exist_ok=True)
        os.makedirs(self._tailored_resume_folder_name, exist_ok=True)
        _path = os.path.join(self._tailored_resume_folder_name, output_folder_name, "Resume.pdf")

        # ensure target directory exists
        os.makedirs(os.path.dirname(_path), exist_ok=True)
        with open(_path, "wb") as out_f:
            # CreatePDF returns a pisaStatus object with .err attribute
            pisa_status = pisa.CreatePDF(src=html_text, dest=out_f)
            if getattr(pisa_status, "err", None):
                # try to include any available log/message for easier debugging
                log = getattr(pisa_status, "log", None)
                if log:
                    raise RuntimeError(f"xhtml2pdf failed to create PDF: {log}")
                raise RuntimeError("xhtml2pdf failed to create PDF")
        return _path
    

    def save_cover_letter_as_pdf(self,
                                    text: str = None,
                                    output_folder_name: str = None
                                    ) -> str:
        """
        output_folder_name: str -> name of the output folder.
        Convert HTML to PDF and write to output_path.
        Returns the output_path on success.
        """
        # xhtml2pdf doesn't accept many options like other libs; we support basic conversion.
        if text is None:
            raise RuntimeError("No content to convert for xhtml2pdf")
        
        if output_folder_name is None:
            raise RuntimeError("Output folder name must be provided")
        else:
            output_folder_name = str(output_folder_name)

        os.makedirs(output_folder_name, exist_ok=True)
        os.makedirs(self._tailored_resume_folder_name, exist_ok=True)
        _path = os.path.join(self._tailored_resume_folder_name, output_folder_name, "Cover Letter.pdf")

        # ensure target directory exists
        os.makedirs(os.path.dirname(_path), exist_ok=True)
        with open(_path, "wb") as out_f:
            # CreatePDF returns a pisaStatus object with .err attribute
            pisa_status = pisa.CreatePDF(src=text, dest=out_f)
            if getattr(pisa_status, "err", None):
                # try to include any available log/message for easier debugging
                log = getattr(pisa_status, "log", None)
                if log:
                    raise RuntimeError(f"xhtml2pdf failed to create PDF: {log}")
                raise RuntimeError("xhtml2pdf failed to create PDF")
        return _path
    

file_manager = FileManager()