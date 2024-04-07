from django.shortcuts import render
from .models import Employee
from .models import SocietyInformation

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def bod(request):
  employees = Employee.objects.all()
  return render(request, 'bod.html', {'employees': employees})

def contact(request):
    return render(request, 'contact.html')

def fdCal(request):
  return render(request, 'fdCal.html')

def rdCal(request):
  return render(request, 'rdCal.html')
  
def society_information_view(request):
      all_society_information = SocietyInformation.objects.all()
      for info in all_society_information:
          # Check if detail_info contains only numbers
          if info.detail_info.isdigit():
              # Convert detail_info to integer
              number = int(info.detail_info)
              # Format the integer as desired
              formatted_number = "{:,.2f}".format(number)
              # Assign the formatted number back to detail_info
              info.detail_info = formatted_number
      context = {'all_society_information': all_society_information}
      return render(request, 'info.html', context)

  
from .models import UploadedFile,Scheme

def download_view(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'download.html', {'uploaded_files': uploaded_files})


def scheme_list(request):
    schemes = Scheme.objects.all()
    return render(request, 'scheme_list.html', {'schemes': schemes})