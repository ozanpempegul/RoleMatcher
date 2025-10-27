from typing import Optional, Dict
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

    def convert(
        self,
        output_path: str,
        html_text: Optional[str] = None,
    ) -> str:
        """
        Convert HTML to PDF and write to output_path.
        Returns the output_path on success.
        """
        # xhtml2pdf doesn't accept many options like other libs; we support basic conversion.
        if html_text is None:
            raise RuntimeError("No content to convert for xhtml2pdf")

        with open(output_path, "wb") as out_f:
            # CreatePDF returns a pisaStatus object with .err attribute
            pisa_status = pisa.CreatePDF(src=html_text, dest=out_f)
            if getattr(pisa_status, "err", None):
                raise RuntimeError("xhtml2pdf failed to create PDF")
        return output_path
    

html_to_pdf_converter = HtmlToPdfConverter()


# Simple usage example (can be removed when used as a module):
if __name__ == "__main__":
    # quick test: create a small PDF using the first available backend
    sample_html = """<p style="text-align:center; font-size:16pt;"><strong>OZAN PEMPEGÜL</strong></p>
<p style="text-align:center; font-size:10pt;">ozanpembegul@gmail.com | +905384306794 | Ankara, Turkey</p>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Summary</strong></p>
<p style="font-size:10pt;">Python software developer with ~3 years of engineering experience building desktop applications, device communication layers, and APIs using PySide6, FastAPI and MVVM patterns. Proven track record designing reusable UI components and modular back-end managers, troubleshooting hardware/software integration, and converting customer feedback into production features. Strong written communication and collaborative problem-solving skills; eager to apply backend/API and UI component experience to build robust, scalable applications.</p>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Experience</strong></p>

<p style="font-size:12pt;"><strong>Software Developer</strong></p>
<p style="font-size:10pt;">NanoMagnetics Instruments – Ankara, Turkey | Nov 2023 – Present</p>
<ul style="font-size:10pt;">
<li>Led development of three Python desktop applications to replace legacy LabVIEW tools, improving performance and maintainability by implementing MVVM architecture, modular Manager classes, and reusable GUI components (PySide6, QtDesigner).</li>
<li>Built local API and experiment analysis features with FastAPI, implemented device communication (PySerial) and data processing using NumPy/SciPy/Matplotlib; incorporated direct customer feedback to iterate functionality.</li>
</ul>

<p style="font-size:12pt;"><strong>Systems Engineer</strong></p>
<p style="font-size:10pt;">NanoMagnetics Instruments – Ankara, Turkey | Jan 2023 – Nov 2023</p>
<ul style="font-size:10pt;">
<li>Performed system testing, calibration, and troubleshooting on complex measurement systems; identified and resolved software bugs and hardware issues to increase system reliability.</li>
<li>Prepared technical documentation and calibration procedures and collaborated with R&D and production teams to improve system performance and test processes.</li>
</ul>

<p style="font-size:12pt;"><strong>Volunteer Assistant</strong></p>
<p style="font-size:10pt;">Patika.dev – Ankara, Turkey | May 2022 – Jan 2023</p>
<ul style="font-size:10pt;">
<li>Solved weekly coding challenges and participated in discussions to refine solutions and improve algorithmic skills.</li>
<li>Guided beginners through problem-solving approaches and best practices, improving participant understanding and progression.</li>
</ul>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Education</strong></p>
<p style="font-size:12pt;"><strong>Geological Engineering</strong></p>
<p style="font-size:10pt;">Middle East Technical University – Ankara, Turkey | Sep 2014 – Jul 2023</p>

"""
    out = "output.pdf"
    conv = HtmlToPdfConverter()
    try:
        conv.convert(output_path=out, html_text=sample_html)
        print(f"PDF written to {out}")
    except Exception as e:
        print("Conversion failed:", e)