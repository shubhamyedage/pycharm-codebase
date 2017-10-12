from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


styles = getSampleStyleSheet()
# story = [Paragraph("Hello world", style=styles["Normal"])]

story = [Paragraph("<para>Hello world<br /></para><para>Hello world</para>", style=styles["Normal"])]
# story.append(Paragraph("<para style='bullet'><bullet>&bull;</bullet>Line five</para>", style=styles["Normal"]))
# s = "<para><ul><li><para style='normal'>Line one</para></li></ul></para>"
# story.append(Paragraph(s, style=styles["Normal"]))
doc = SimpleDocTemplate(
    "test_text_tags.pdf"
    , pagesize=A4,
    rightMargin=28, leftMargin=28,
    topMargin=72, bottomMargin=18
)
doc.build(story)
