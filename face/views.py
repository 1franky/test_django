from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
from PIL import Image
from face import get_numpy

@api_view(['POST'])
def image_to_numpy(request):
    try:
        image = Image.open(request.FILES['ine'])
        numpy_array = np.array(image)
        r = get_numpy.getNumpy(numpy_array)
        return r
    except Exception as e:
        print(f"error {e}")
        return Response({
            'numRostros': 0,
            'arrays': [],
            'time': 0
        }, status=500)

@api_view(['POST'])
def image_to_numpy2(request):
    try:
        image = Image.open(request.FILES['ine'])
        numpy_array = np.array(image)
        r = get_numpy.getNumpy2(numpy_array)
        return r
    except Exception as e:
        print(f"error {e}")
        return Response({
            'numRostros': 0,
            'arrays': [],
            'time': 0
        }, status=500)


