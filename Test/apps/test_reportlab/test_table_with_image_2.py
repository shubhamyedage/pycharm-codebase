from os.path import expanduser, join
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm,landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch

a = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test1.png'), 4*inch, 3*inch)
b = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test2.png'), 4*inch, 3*inch)
# a.drawHeight = 2*inch
# a.drawWidth = 2*inch
data=[[a, b]]
c = canvas.Canvas("Reportlabtest.pdf", pagesize=A4)
table = Table(data)
table.setStyle(TableStyle([
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ('BACKGROUND',(0,0),(-1,2),colors.lightgrey)
                           ]))
table.wrapOn(c, 200, 400)
table.drawOn(c,20,50)
c.save()
