from os.path import join, expanduser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

path = join(expanduser('~'), "PycharmProjects", "Test", "apps", "test_reportlab")
print(path)
c = canvas.Canvas(join(path, "Hello.pdf"), pagesize=letter)
c.setLineWidth(.3)
c.setFont('Helvetica', 12)
c.setFillColor(aColor="RED")
c.drawString(100, 750, "Welcome!!")
c.save()