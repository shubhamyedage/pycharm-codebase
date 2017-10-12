
from os.path import join, expanduser
from os import remove, listdir
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
import shutil


def make_note():
    """Builds a pdf note based on the passed dictionary of parameters.
    For the structure of the parameters, see the code of the function
    make_example_note.
    """
    story = []
    data = [[1,'   ',1,1,1,1], [1,'',1,1,1,1], [1,'',1,1,1,1]]
    # t = Table(data, 5 * [1.25 * inch], len(data) * [0.25 * inch])
    i = [1 * inch,1 * inch,0.5 * inch,1.25 * inch,1.25 * inch,1.25 * inch]
    t = Table(data, i, len(data) * [0.25 * inch])

    t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2),'RIGHT'),
                           ('FONTSIZE', (0, 0), (-1, -1), 15),
                           ('VALIGN', (0, 0), (0, -1), 'TOP'),
                           ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                           ('INNERGRID', (0, 0), (-1, -1), 1,"red"),
                           ('BOX', (0, 0), (-1, -1), 0.25, "black"),
                           ]))
    story.append(t)
    doc = SimpleDocTemplate("table_style_1.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    doc.build(story)

make_note()
