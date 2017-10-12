from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak, Spacer, Image
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import inch

doc = SimpleDocTemplate("simpletable.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
style_1 = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, 'Black'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOX', (0, 0), (-1, -1), 0.25, 'Black'),
    ('SPAN', (0, 0), (0, 1)),
    ('SPAN', (1, 0), (4, 0)),
    ('SPAN', (5, 0), (6, 0)),
    ('SPAN', (7, 0), (7, 1))
])

data_1 = [
    ['Indicator', 'Value, million Dollars', '', '', '', 'Change', '', 'Average annual value, milion Dollar'],
    ['', '', '', '', '', 'million Dollar (col.5 - col.2)', '± %(5-2) : 2', ''],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]
]

data_2 = [
    ['Profitability ratios', 'Value in %', '', '', '', 'Change(col.5 - col.2)'],
    ['', '2014-10', '2015-10', '2016-10', 'TTM', '']
]
style_2 = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, "black"),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOX', (0, 0), (-1, -1), 0.25, "black"),
    ("SPAN", (0, 0), (0, 1)),
    ("SPAN", (1, 0), (4, 0)),
    ("SPAN", (5, 0), (5, 1))
])

style = getSampleStyleSheet()
para_style = ParagraphStyle(
    name='Justify',
    alignment=TA_JUSTIFY,
    leading=24
)
style.add(para_style)
t = Paragraph(text="lilhdskd;sdks;odks;odkw;odkew;doke;eodkke;dw;dok", style=style["Normal"])
elements.append(t)
elements.append(Spacer(1, 12))
elements.append(PageBreak())

t = Table(data=data_1)
t.setStyle(tblstyle=style_1)
elements.append(t)
elements.append(Spacer(1, 6))
img = Image(
                "Screenshot from 2017-07-13 11-57-24.png",
                4.4 * inch,
                3.4 * inch
            )
elements.append(img)
elements.append(Spacer(1, 8))
elements.append(PageBreak())



t = Table(data=data_2)
t.setStyle(tblstyle=style_2)
elements.append(t)
elements.append(Spacer(1, 16))


data_3 = [
    [
        "Indicator",
        "Value",
        "",
        "",
        "",
        "",
        "",
        "Change for the Period\n Analyzed ",
        ""
    ],
    [
        "",
        "In Million $",
        "",
        "",
        "",
        "% of the Balance Total",
        "",
        "Million $ \n(col.5-col.2)",
        "± %((col.5-col.2)\n : col.2)"
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "At the\nBeginning of\nthe Period\nAnalyzed",
        "At the End \nof the Period \nAnalyzed",
        "",
        ""
    ],
    [
        "Assets",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Equity and Liabilities",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    ["liji", "", "", "", "", "", "", "", "", ""],
['Current Assets', 6967.0, 9261.0, 8353.0, 12018.0, 60.55, 65.89, 5051.0, 72.5]
]
style_3 = style_1 = TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, 'Black'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOX', (0, 0), (-1, -1), 0.25, 'Black'),
("SPAN", (0, 0), (0, 2)),
                ("SPAN", (1, 0), (6, 0)),
                ("SPAN", (7, 0), (8, 0)),
                ("SPAN", (1, 1), (4, 1)),
                ("SPAN", (5, 1), (6, 1)),
                ("SPAN", (7, 1), (7, 2)),
                ("SPAN", (8, 1), (8, 2))
])
t = Table(data=data_3)
t.setStyle(tblstyle=style_3)
elements.append(t)
# write the document to disk
doc.build(elements)