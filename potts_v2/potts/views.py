from django.shortcuts import render
from django.views.generic import View

class DashboardView(View):
	def get(self, request):
		context = {
			"dashboard_active":"active"
		}
		return render(request, "dashboard.html", context)

class CashFlowView(View):
	def get(self, request):
		return render(request, "index.html")

class ProjectionView(View):
	def get(self, request):
		return redner(request, "index.html")
