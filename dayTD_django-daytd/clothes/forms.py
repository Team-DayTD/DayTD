import pandas as pd
import requests
from django import forms
from clothes.models import *


# class SigudongForm(forms.ModelForm):
#     class Meta:
#         model = Region
#         fields = 'si','gu','dong'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['gu'].queryset = Gu.objects.none()
#         self.fields['dong'].queryset = Gu.objects.none()

#         if 'si' in self.data:
#             try:
#                 si_id = int(self.data.get('si'))
#                 self.fields['gu'].queryset = Gu.objects.filter(si_id=si_id)
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#             if 'gu' in self.data:
#                 try:
#                     gu_id = int(self.data.get('gu'))
#                     self.fields['dong'].queryset = Dong.objects.filter(gu_id=gu_id)
#                 except (ValueError, TypeError):
#                     pass  # invalid input from the client; ignore and fallback to empty City queryset

#             elif self.instance.pk:
#                 self.fields['dong'].queryset = self.instance.gu.dong_set

#         elif self.instance.pk:
#             self.fields['gu'].queryset = self.instance.si.gu_set