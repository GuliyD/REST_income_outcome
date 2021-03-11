from django.urls import path, include
from .views import IncomeView, PostIncomeView, PostOutcomeView

urlpatterns = [
    path('', IncomeView.as_view()),
    path('income/', PostIncomeView.as_view()),
    path('outcome/', PostOutcomeView.as_view())
]
