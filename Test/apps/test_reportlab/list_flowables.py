from reportlab.platypus import ListFlowable, ListItem
from reportlab.platypus.flowables import DocPara, DocAssign
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Frame
from reportlab.lib.pagesizes import A4, inch
from reportlab.pdfgen.canvas import Canvas

styles = getSampleStyleSheet()
style = styles["Normal"]
story = []
# bulletType = a/i/a/A/ I
t = ListFlowable(
    [
        Paragraph("Item no.1 company_name", style),
        ListItem(Paragraph("Item no. 2", style), bulletColor="green", value=7),
        ListFlowable(
            [
                Paragraph("sublist item 1", style),
                ListItem(Paragraph('sublist item 2', style), bulletColor='red',
                         value='square'),
                ListItem(Paragraph('sublist item 2', style), bulletColor='red',
                         value='square')
            ],
            bulletType='bullet',
            start='square',
        ),
        Paragraph("Item no.4", style)
    ],
    bulletType='i'
)
story.append(Paragraph("Hello World", style))
story.append(t)
story.append(Paragraph("Hello World", style))
doc = SimpleDocTemplate("list_flowables.pdf", pagesize=A4,
                        rightMargin=28, leftMargin=28,
                        topMargin=72, bottomMargin=18)
doc.build(story)
# c = Canvas('list_flowables.pdf')
# f = Frame(inch, inch, 6 * inch, 9 * inch, showBoundary=1)
# f.addFromList(story, c)
# c.save()
