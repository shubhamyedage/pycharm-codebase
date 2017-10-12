from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib.pagesizes import letter

story = []
data = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
t = Table(data)
t.setStyle(TableStyle(
    [('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
     ('FONTSIZE', (0, 0), (-1, -1), 15)]
))

doc = SimpleDocTemplate("test_table_style_2.pdf", pagesize=letter,
                        rightmargin=72, leftmargin=72, topmargin=72,
                        bottommargin=18)
doc.build(story)
