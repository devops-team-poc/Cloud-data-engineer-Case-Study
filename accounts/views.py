# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb
from decimal import Decimal

from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import OuterRef, Subquery
from accounts.models import UberEatsMenu, TripAdvisorOutlet, UberEatsOutlet
from accounts.serializers import OutletSerializer, TripAdvisorOutletSerializer, UberEatsOutletSerializer


class OutletList(APIView):
    serializer_class = OutletSerializer
    def get(self,request, *args, **kwargs):
        try:
            brand = request.GET.get('brand',0)
        except:
            return Response({
                "message": "please pass brand"
            })
        queryset=UberEatsMenu.objects.filter(brand__contains=brand)
        return Response({
            "data": self.serializer_class(queryset, many=True).data,
        })

class UberEatsOutletCreate(generics.GenericAPIView):
    serializer_class = UberEatsOutletSerializer
    def post(self, request, *args):
        UberEatsOutlet = self.serializer_class(data=request.data)
        if UberEatsOutlet.is_valid():
            UberEatsOutlet.save()
            return Response(
                data={
                    "data": UberEatsOutlet.data,
                    "message": "UberEatsOutlet saved successfully.",
                    "success": True,
                }, status=status.HTTP_201_CREATED
            )
        return Response({
            "message": "Something went wrong"
        })


class TripAdvisorOutletCreate(generics.GenericAPIView):
    serializer_class = TripAdvisorOutletSerializer
    def post(self, request, *args):
        TripAdvisorOutlet = self.serializer_class(data=request.data)
        if TripAdvisorOutlet.is_valid():
            TripAdvisorOutlet.save()
            return Response(
                data={
                    "data": TripAdvisorOutlet.data,
                    "message": "TripAdvisorOutlet saved successfully.",
                    "success": True,
                }, status=status.HTTP_201_CREATED
            )
        return Response({
            "message": "Something went wrong"
        })

class SpecificOutlet(APIView):
    def get(self,request, *args, **kwargs):
        try:
            source=request.GET.get('source')
        except:
            return Response({
                "message":"please pass source"
            })
        if source == 'Tripadvisor':
            queryset = TripAdvisorOutlet.objects.all()
            return Response({
                "data": TripAdvisorOutletSerializer(queryset, many=True).data,
            })
        if source== 'Ubereats':
            queryset=UberEatsOutlet.objects.all()
            return Response({
                "data": UberEatsOutletSerializer(queryset, many=True).data,
            })
        return Response({
            "message": "please pass source"
        })


class MenuList(APIView):
    serializer_class = OutletSerializer

    def get(self, request, *args, **kwargs):
        try:
            price = request.GET.get('price', 0)
        except:
            return Response({
                "message": "please pass price"
            })
        queryset = UberEatsMenu.objects.filter(price=float(price))
        return Response({
            "data": self.serializer_class(queryset, many=True).data,
        })