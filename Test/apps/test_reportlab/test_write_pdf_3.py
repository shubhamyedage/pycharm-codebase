from os import getcwd
from os.path import join
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.enums import TA_JUSTIFY


def get_str(msgStr):
    msgStr = msgStr.replace(' ', '&nbsp;')
    msgStr = msgStr.replace('\n', '<br />')
    msgStr = msgStr.replace('\t','&nbsp;&nbsp;&nbsp;&nbsp;')
    return msgStr


story = []
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
s = "Hello world!"
story.append(Paragraph(s, styles["Normal"]))
story.append(PageBreak())
s = get_str("Hii \n %9s <br /> %s" % ("Bobby", "Sue"))

story.append(Paragraph(s, styles["Normal"]))
path = join(getcwd(), "test_write_pdf_3.pdf")
doc = SimpleDocTemplate(path,  pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
doc.build(story)
print(path)
