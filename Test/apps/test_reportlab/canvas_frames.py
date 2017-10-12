from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate
from reportlab.lib.pagesizes import A4

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading2']
story = []
# add some flowables
story.append(Paragraph("This is a Heading", styleH))
story.append(Paragraph(
    "This is a <index item='paragraph'/>paragraph in <i>Normal</i> style.",
    styleN))


# ------------ With Canvas ----------------------------
c = Canvas('canvas_frames.pdf')
f = Frame(inch, inch, 6 * inch, 9 * inch, showBoundary=1)
f.addFromList(story, c)
c.save()

# ------------ With simple doc -----------------------
# doc = SimpleDocTemplate("doc_frames.pdf", pagesize=A4,
#                                 rightMargin=28, leftMargin=28,
#                                 topMargin=72, bottomMargin=18)
# doc.build()