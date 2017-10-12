from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Paragraph
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)


def stylesheet():
    styles = {
        'default': ParagraphStyle(
            'default',
            fontName='Times-Roman',
            fontSize=10,
            leading=12,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            textColor=black,
            backColor=None,
            wordWrap=None,
            borderWidth=0,
            borderPadding=0,
            borderColor=None,
            borderRadius=None,
            allowWidows=1,
            allowOrphans=0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    return styles


def build_flowables(stylesheet):
    return [
        Paragraph('The analysis given below on TWX’s financial state and operating efficiency is made for the period 01-12-201 \
4 to 20-09-2017 based on the financial statements data prepared according to Generally Accepted Accounti \
ng Principles (GAAP). ', stylesheet['default']),
        Paragraph('more text. ' * 30, stylesheet['default']),
    ]


def build_pdf(filename, flowables):
    doc = BaseDocTemplate(filename)
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,
                        doc.bottomMargin,
                        doc.width,
                        doc.height,
                        id=None
                    ),
                ]
            ),
        ]
    )

    doc.build(flowables)

build_pdf('p0150_1.pdf', build_flowables(stylesheet()))
