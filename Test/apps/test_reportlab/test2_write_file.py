# http://www.programcreek.com/python/example/52897/reportlab.platypus.Paragraph

from os.path import join, expanduser
from os import remove, listdir
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import shutil

path = join(expanduser('~'), "PycharmProjects", "Test", "apps", "test_reportlab")
story = []
doc = SimpleDocTemplate("test2.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


s = "'' PADDING <font size=10>Net income has <font color='red'>RAISED</font> by {}</font> \n Yes True".format(72.20)
story.append(Paragraph(s, styles["Normal"]))
story.append(Spacer(1, 12))

s = "<font size=12>Index Net income has RAISED by {}</font>".format(72.20)
story.append(Paragraph(s, styles["Normal"]))
story.append(Spacer(1, 48))

s = "<font size=18><strong>Index Net income has RAISED by {}</strong></font>".format(72.20)
story.append(Paragraph(s, styles["Normal"]))

f = "luih"
s = "<font size=18 color='blue'><strong>%s</strong></font>" % f
story.append(Paragraph(s, styles["Normal"]))

img = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'), 6*inch, 3*inch)
story.append(img)
img = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'), 6*inch, 3*inch)
story.append(img)
img = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'), 6*inch, 3*inch)
story.append(img)
img = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'), 6*inch, 3*inch)
story.append(img)
img = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test.png'), 6*inch, 3*inch)
story.append(img)

doc.build(story)

path = join(expanduser('~'), 'PycharmProjects', 'Test', 'docs')
for f in listdir(path):
    remove(join(path, f))