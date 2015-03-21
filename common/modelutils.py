#! -*- coding:utf-8 -*-

from django.shortcuts import _get_queryset

def get_object_or_none(kclass, *args, **kwargs):
    queryset = _get_queryset(kclass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None
