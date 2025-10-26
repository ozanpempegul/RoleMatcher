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
    sample_html = """<p style="text-align:center; font-size:16pt;"><strong>Ozan Pempegül</strong></p>
<p style="text-align:center; font-size:10pt;">ozanpembegul@gmail.com | +90 538 430 6794 | Ankara, Turkey</p>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Summary</strong></p>
<p style="font-size:10pt;">Software developer with a strong foundation in Python and experience building desktop applications. Skilled in translating requirements into efficient, maintainable code and capable of managing projects independently. Familiar with AI concepts and problem-solving, with a demonstrated ability to learn and apply technical skills in software development and algorithmic solutions.</p>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Professional Experience</strong></p>

<p style="font-size:12pt;"><strong>Software Developer</strong></p>
<p style="font-size:10pt;">NanoMagnetics Instruments – Ankara, Turkey | 11/2023 – Present</p>
<ul style="font-size:10pt;">
  <li>Developed three Python desktop applications replacing legacy LabVIEW systems, improving efficiency and maintainability</li>
  <li>Gathered and implemented user feedback to enhance functionality and usability</li>
  <li>Managed full software development lifecycle independently, from design to deployment</li>
</ul>

<p style="font-size:12pt;"><strong>Systems Engineer</strong></p>
<p style="font-size:10pt;">NanoMagnetics Instruments – Ankara, Turkey | 01/2023 – 11/2023</p>
<ul style="font-size:10pt;">
  <li>Analyzed complex measurement systems to support software integration and development</li>
  <li>Prepared technical documentation and calibration procedures to ensure system reliability</li>
</ul>

<p style="font-size:12pt;"><strong>Volunteer Assistant</strong></p>
<p style="font-size:10pt;">Patika.dev – Remote | 05/2022 – 01/2023</p>
<ul style="font-size:10pt;">
  <li>Solved weekly Python coding challenges, refining algorithmic and problem-solving skills</li>
  <li>Guided beginners in understanding technical concepts and solving programming problems</li>
</ul>
<hr style="border:0; border-top:1px solid #000;">
<p style="text-align:center; font-size:12pt;"><strong>Education</strong></p>

<p style="font-size:12pt;"><strong>Geological Engineering</strong></p>
<p style="font-size:10pt;">Middle East Technical University – Ankara, Turkey | 09/2014 – 07/2023</p>

"""
    out = "output.pdf"
    conv = HtmlToPdfConverter()
    try:
        conv.convert(output_path=out, html=sample_html)
        print(f"PDF written to {out}")
    except Exception as e:
        print("Conversion failed:", e)