import os
from xhtml2pdf import pisa  # type: ignore


"""
html_to_pdf_converter.py

Utility to convert HTML (string / file / URL) to PDF using an available backend.
    - xhtml2pdf (pip install xhtml2pdf)
"""


class HtmlToPdfConverter:
    def __init__(self):
        """
        backend_preference: Optional[str] -> "weasyprint", "xhtml2pdf", "pdfkit", or "playwright".
        If None, the converter will pick the first available backend.
        """

    def save_cover_letter_as_pdf(self,
                                    text: str = None,
                                    output_folder_name: str = None
                                    ) -> str:
        """
        output_folder_name: str -> name of the output folder.
        Convert HTML to PDF and write to output_path.
        Returns the output_path on success.
        """

        _tailored_resume_folder_name = "tailored_resumes"
        # xhtml2pdf doesn't accept many options like other libs; we support basic conversion.
        if text is None:
            raise RuntimeError("No content to convert for xhtml2pdf")
        
        if output_folder_name is None:
            raise RuntimeError("Output folder name must be provided")
        else:
            output_folder_name = str(output_folder_name)

        os.makedirs(output_folder_name, exist_ok=True)
        os.makedirs(_tailored_resume_folder_name, exist_ok=True)
        _path = os.path.join(_tailored_resume_folder_name, output_folder_name, "Cover Letter.pdf")

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
    

html_to_pdf_converter = HtmlToPdfConverter()


# Simple usage example (can be removed when used as a module):
if __name__ == "__main__":
    # quick test: create a small PDF using the first available backend
    sample_html = """<p style="text-align:center; font-size:16pt;"><strong>OZAN PEMPEGÜL</strong></p>
"""
    out = 2
    conv = HtmlToPdfConverter()
    try:
        conv.save_cover_letter_as_pdf(output_folder_name=out, text=sample_html)
        print(f"PDF written to {out}")
    except Exception as e:
        print("Conversion failed:", e)