# -*- coding: utf-8 -*-

from django.shortcuts import render


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
