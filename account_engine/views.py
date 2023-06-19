from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def carrers(request):
    return render(request, 'carrers.html')

# about_us
def company_profile(request):
    return render(request, 'about_us/company_profile.html')

def man_power(request):
    return render(request, 'about_us/man_power.html')

def management_credentials(request):
    return render(request, 'about_us/management_credentials.html')

def managing_director(request):
    return render(request, 'about_us/managing_director.html')

#approval/accreditation
def approval(request):
    return render(request, 'approval/approval.html')

def accreditation(request):
    return render(request, 'approval/accreditation.html')

#operational_area
def building_material_test(request):
    return render(request, 'operational_area/building_material_test.html')

def chemical_test(request):
    return render(request, 'operational_area/chemical_test.html')

def electrical_test(request):
    return render(request, 'operational_area/electrical_test.html')

def environment_test(request):
    return render(request, 'operational_area/environment_test.html')

def food_test(request):
    return render(request, 'operational_area/food_test.html')

def geo_tech_investigation(request):
    return render(request, 'operational_area/geo_tech_investigation.html')

def mechanical_test(request):
    return render(request, 'operational_area/mechanical_test.html')

def ndt_test(request):
    return render(request, 'operational_area/ndt_test.html')

def water_test(request):
    return render(request, 'operational_area/water_test.html')

#services
def planning_advisory(request):
    return render(request, 'services/planning_advisory.html')

def engineering_design(request):
    return render(request, 'services/engineering_design.html')

def project_management(request):
    return render(request, 'services/project_management.html')

def inspection(request):
    return render(request, 'services/inspection.html')

def testing(request):
    return render(request, 'services/testing.html')