from reportlab.platypus import ListFlowable, ListItem
from reportlab.platypus.flowables import DocPara, DocAssign
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Frame, PageBreak
from reportlab.lib.pagesizes import A4, inch
from reportlab.pdfgen.canvas import Canvas

styles = getSampleStyleSheet()
style = styles["Normal"]
story = []
t = ListFlowable(
    [
        Paragraph("<a href='#ID_1' color='blue'>Item no. 1</a>", style),
        ListFlowable(
            [
                Paragraph('sublist item 1', style),
                Paragraph('sublist item 2', style)
            ],
            bulletType='1',
            bulletColor='white'
        ),
        Paragraph("Item no. 2", style),
    ],
    bulletType='1',
    bulletColor='white'
)
story.append(Paragraph("Hello World", style))
story.append(t)
story.append(PageBreak())
story.append(Paragraph("<a name='ID_1'/>Hello World 2", style))
story.append(PageBreak())
story.append(Paragraph("Hello World 3", style))
story.append(Paragraph("Hello World", style))
doc = SimpleDocTemplate("list_flowables_2.pdf", pagesize=A4,
                        rightMargin=28, leftMargin=28,
                        topMargin=72, bottomMargin=18)
doc.build(story)
# c = Canvas('list_flowables.pdf')
# f = Frame(inch, inch, 6 * inch, 9 * inch, showBoundary=1)
# f.addFromList(story, c)
# c.save()
