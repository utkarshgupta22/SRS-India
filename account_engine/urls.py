from django.urls import path
from account_engine import views

urlpatterns = [
        path('', views.index, name='index'),
        path('contact/', views.contact, name='contact'),
        path('carrers', views.carrers,name='carrers'),
        # about_Us
        path('company_profile/', views.company_profile, name='company_profile'),
        path('man_power', views.man_power, name='man_power'),
        path('management_credentials', views.management_credentials, name='management_credentials'),
        path('managing_director', views.managing_director, name='managing_director'),
        #approval/accedration
        path('accreditation', views.accreditation,name='accreditation'),
        path('approval', views.approval, name='approval'),
        #operational_area
        path('building_material_test', views.building_material_test, name='building_material_test'),
        path('chemical_test', views.chemical_test, name='chemical_test'),
        path('electrical_test', views.electrical_test, name='electrical_test'),
        path('environment_test', views.environment_test, name='environment_test'),
        path('food_test', views.food_test, name='food_test'),
        path('geo_tech_investigation', views.geo_tech_investigation, name='geo_tech_investigation'),
        path('mechanical_test', views.mechanical_test, name='mechanical_test'),
        path('ndt_test', views.ndt_test, name='ndt_test'),
        path('water_test', views.water_test, name='water_test'),
        #services
        path('planning_advisory', views.planning_advisory, name='planning_advisory'),
        path('inspection', views.inspection, name='inspection'),
        path('testing', views.testing, name='testing'),
        path('engineering_design', views.engineering_design, name='engineering_design'),
        path('project_management', views.project_management, name='project_management'),

]