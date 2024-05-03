# -*- coding:utf-8 -*-
from subjects.models import Subject
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'pk',
            'name',
            'age',
            'sex',
            'measurement_date',
            'int_dt',
            'upt_dt'
        )