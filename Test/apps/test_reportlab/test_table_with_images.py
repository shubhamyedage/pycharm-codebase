from os.path import expanduser, join
from reportlab.platypus import Image, SimpleDocTemplate, TableStyle, Table
from reportlab.lib.pagesizes import inch, A4

story = []
root_path = join(expanduser('~'), 'PycharmProjects', 'Test', 'docs',)

images = []
table_data = []

img1 = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test1.png'), 4*inch, 3*inch)
# story.append(img1)
images.append(img1)

img2 = Image(join(expanduser('~'), 'PycharmProjects', 'Test', 'docs', 'test2.png'), 4*inch, 3*inch)
# story.append(img2)
images.append(img2)
table_data.append(images)

table = Table(table_data)
story.append(table)

doc = SimpleDocTemplate("img.pdf", pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

doc.build(story)

