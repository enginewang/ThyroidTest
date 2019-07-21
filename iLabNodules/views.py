# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


pdfmetrics.registerFont(TTFont('PingFang', 'index/static/PingFang-SC-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Regular', 'index/static/font/PingFang Regular.ttf'))
pdfmetrics.registerFont(TTFont('Light', 'index/static/font/PingFang Light.ttf'))
pdfmetrics.registerFont(TTFont('Bold', 'index/static/font/PingFang Bold.ttf'))

def index(request):
    context = {}
    nodules = {}

    data = []
    data.append(nodules)

    # TODO
    # 初始化的时候，生成所有的切片（异步）,和可疑结节的信息：编号、坐标、半径，保存
    # data: nodules id and coordinates

    context['nodules'] = data
    return render(request, 'index.html', context)


def print_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # Get Data
    name = "王小明"
    gender = "男"
    age = "20"
    id_num = "123456"
    nodules = [{'name': '结点1',
               'diameter': '12.0',
               'positionX': '240',
               'positionY': '222',
               'positionZ': '293',
               'volume': '127.23',
               'rate': '33.6%'},
              {'name': '结点2',
               'diameter': '14.0',
               'positionX': '260',
               'positionY': '278',
               'positionZ': '234',
               'volume': '456.65',
               'rate': '70.9%'},
              ]
    p = canvas.Canvas(response)
    p.setFont('Bold', 18, leading=None)
    # report = []
    # report_title = '<para autoLeading="off" fontSize=15 align=center><b><font face="PingFang">检查报告</font></b><br/><br/><br/></para>'
    # report.append(Paragraph(report_title, normalStyle))
    p.drawCentredString(105 * mm, 275 * mm, "检查报告")
    p.line(20 * mm, 265 * mm, 190 * mm, 265 * mm)
    p.setFont('Regular', 12, leading=None)
    p.drawString(30 * mm, 255 * mm, "姓名：" + name)
    p.drawString(70 * mm, 255 * mm, "性别：" + gender)
    p.drawString(110 * mm, 255 * mm, "年龄：" + age)
    p.drawString(150 * mm, 255 * mm, "ID号：" + id_num)
    p.line(20 * mm, 248 * mm, 190 * mm, 248 * mm)
    p.setFont('Light', 10, leading=None)
    p.drawCentredString(60 * mm, 238 * mm, "直径(mm)")
    p.drawCentredString(95 * mm, 238 * mm, "结点位置")
    p.drawCentredString(130 * mm, 238 * mm, "体积大小(mm^3)")
    p.drawCentredString(165 * mm, 238 * mm, "良恶率(%)")
    bottomY = 238
    for nodule in nodules:
        bottomY -= 10
        p.drawCentredString(30 * mm, bottomY * mm, nodule['name'])
        p.drawCentredString(60 * mm, bottomY * mm, nodule['diameter'])
        p.drawCentredString(95 * mm, bottomY * mm, "(" + nodule['positionX'] + "," + nodule['positionY'] + "," + nodule['positionZ'] + ")")
        p.drawCentredString(130 * mm, bottomY * mm, nodule['volume'])
        p.drawCentredString(165 * mm, bottomY * mm, nodule['rate'])

    p.showPage()
    p.save()
    return response
