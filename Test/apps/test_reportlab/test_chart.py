# http://www.programcreek.com/python/example/52897/reportlab.platypus.Paragraph

from os.path import join, expanduser
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.linecharts import HorizontalLineChart

path = join(expanduser('~'), "PycharmProjects", "Test", "apps", "test_reportlab")
story = []
doc = SimpleDocTemplate("test_charts.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


s = "'' PADDING <font size=10>Net income has <font color='red'>RAISED</font> by {}</font> \n Yes True".format(72.20)
story.append(Paragraph(s, styles["Normal"]))
story.append(Spacer(1, 12))

data = [
 ((1,1), (2,2), (2.5,1), (3,3), (4,5)),
 ((1,2), (2,3), (2.5,2), (3.5,5), (4,6))
]
# lp = LinePlot()
# lp.x = 50
# lp.y = 50
# lp.height = 125
# lp.width = 300
# lp.data = data
# lp.joinedLines = 1
# lp.lines[0].symbol = makeMarker('FilledCircle')
# lp.lines[1].symbol = makeMarker('Circle')
# lp.lineLabelFormat = '%2.0f'
# # lp.strokeColor = "Black"
# lp.xValueAxis.valueMin = 0
# lp.xValueAxis.valueMax = 5
# lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
# lp.xValueAxis.labelTextFormat = '%2.1f'
# lp.yValueAxis.valueMin = 0
# lp.yValueAxis.valueMax = 7
# lp.yValueAxis.valueSteps = [1, 2, 3, 5, 6]
# story.append(lp)

lc = HorizontalLineChart()
lc.x = 50
lc.y = 50
lc.height = 125
lc.width = 300
lc.data = data
lc.joinedLines = 1
catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'n'
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 60
lc.valueAxis.valueStep = 15
lc.lines[0].strokeWidth = 2
lc.lines[1].strokeWidth = 1.5
story.append(Paragraph(lc, styles["Normal"]))

doc.build(story)
