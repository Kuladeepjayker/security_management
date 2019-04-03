from django.shortcuts import render, redirect, render_to_response
from . models import *
from datetime import datetime, date, time
from django.http import HttpResponse
from django.template import RequestContext
import xlwt

# Create your views here.


def login(request):
    return render(request, 'login.html')

def login_validate(request):
    if request.method == 'POST':
        try:
            user = Users_table.objects.get(user_name = request.POST.get('user_name'))
        except:
            user = None
        if user:
            if request.POST.get('password') == user.password:
                if request.session.get('user_name') is None:
                    request.session.flush()
                    request.session['user_name'] = user.user_name
                    request.session.set_expiry(0)
                return redirect(home)
        else:
            return redirect(access_denied)

def access_denied(request):
    return render(request, 'access_denied.html')

def logout(request):
    del request.session['user_name']
    return redirect(login)

def visitor(request):
    if 'user_name' in request.session:
        return render(request, 'visitor_details.html')
    else:
        return redirect(access_denied)

def visitor_details(request):
    if 'user_name' in request.session:
        if request.method == 'POST':
            visitor_details = visitor_entry_table()
            visitor_details.name = request.POST.get('visitor_name')
            visitor_details.phone_number = request.POST.get('phone_number')
            visitor_details.staff_to_contact = request.POST.get('staff_name')
            visitor_details.staff_phone_number = request.POST.get('staff_phone_number')
            visitor_details.purpose = request.POST.get('purpose')
            visitor_details.entrance_date = date.today()
            visitor_details.entrance_time = datetime.time(datetime.now())
            visitor_details.user_id =  request.POST.get('user_id')
            visitor_details.save()
            context = {
                'visitor_details': visitor_details
            }
        return render(request,'printdetails.html', context)
    else:
        return redirect(access_denied)

def visitor_exit(request, visitor_id):
    return render(request, 'visitor_exit.html')

def home(request):
    if 'user_name' in request.session:
        return render(request, 'home.html')
    else:
        return redirect(access_denied)

def staff_vehicle(request):
    if 'user_name' in request.session:
        return render(request, 'staff_vehicle.html')
    else:
        return redirect(access_denied)

def staff_vehicle_details(request):
    if 'user_name' in request.session:
        if request.method == 'POST':
            visitor_details = staff_vehicle_entry_table()
            visitor_details.name = request.POST.get('staff_name')
            visitor_details.phone_number = request.POST.get('phone_number')
            visitor_details.vehicle_number = request.POST.get('staff_vehicle_number')
            visitor_details.staff_to_contact = request.POST.get('staff_to_contact')
            visitor_details.staff_type = request.POST.get('type')
            visitor_details.staff_phone_number = request.POST.get('s_phone_number')
            visitor_details.purpose = request.POST.get('purpose')
            visitor_details.entrance_date = date.today()
            visitor_details.entrance_time = datetime.time(datetime.now())
            visitor_details.user_id =  request.POST.get('user_id')
            visitor_details.save()
            context = {
                'visitor_details': visitor_details
            }
        return render(request,'printdetails.html', context)
    else:
        return redirect(access_denied)

def staff_vehicle_exit(request, visitor_id):
    return HttpResponse('<h1>Staff Vehicle exit</h1>')

def other_vehicle(request):
    if 'user_name' in request.session:
        return render(request, 'other_vehicle.html')
    else:
        return redirect(access_denied)

def other_vehicle_details(request):
    if 'user_name' in request.session:
        if request.method == 'POST':
            visitor_details = other_vehicle_entry_table()
            visitor_details.name = request.POST.get('visitor_name')
            visitor_details.phone_number = request.POST.get('visitor_phone_number')
            visitor_details.vehicle_number = request.POST.get('visitor_vehicle_number')
            visitor_details.staff_to_contact = request.POST.get('staff_to_contact')
            visitor_details.staff_phone_number = request.POST.get('staff_phone_number')
            visitor_details.purpose = request.POST.get('purpose')
            visitor_details.entrance_date = date.today()
            visitor_details.entrance_time = datetime.time(datetime.now())
            visitor_details.user_id =  request.POST.get('user_id')
            visitor_details.save()
            context = {
                'visitor_details': visitor_details
            }
        return render(request,'printdetails.html', context)
    else:
        return redirect(access_denied)

def export_data(request):
    if 'user_name' in request.session:
        return render(request, 'export_data.html')
    else:
        return redirect(access_denied)

def get_excel(request):
    category = request.POST.get('category')
    from_date = request.POST.get('from')
    to_date = request.POST.get('to')
    print(category)
    print(from_date)
    print(to_date)
    if category == 'visitor':
        columns = ['Entrance Date', 'Visitor Name', 'Phone Number', 'Staff To Contact', 'Staff Phone Number', 'Purpose', 'Entrance Time', 'User']
    elif category == 'staff':
        columns = ['Entrance Date', 'Staff Name', 'Phone Number', 'Vehicle Number', 'Staff Type', 'Purpose', 'Entrance Time', 'User']
    else:
        columns = ['Entrance Date', 'Visitor Name', 'Phone Number', 'Vehicle Number', 'Staff To Contact', 'Staff Phone Number', 'Purpose', 'Entrance Time', 'User']


    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{{category}}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(category)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    #date_format = wb.add_format({'num_format': 'mm/dd/yy'})
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'yyyy-mm-dd'
    time_format = xlwt.XFStyle()
    time_format.num_format_str = 'hh:mm AM/PM'
    #time_format = wb.add_format({'num_format': ''})
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    if category == 'visitor':
        rows = visitor_entry_table.objects.filter(entrance_date__range=[from_date, to_date]).values_list( 'entrance_date', 'name', 'phone_number', 'staff_to_contact', 'staff_phone_number', 'purpose', 'entrance_time', 'user')
    elif category == 'staff':
        rows = staff_vehicle_entry_table.objects.all().values_list( 'entrance_date', 'name', 'phone_number', 'vehicle_number', 'staff_type', 'purpose', 'entrance_time', 'user')
    else:
        rows = other_vehicle_entry_table.objects.all().values_list( 'entrance_date', 'name', 'phone_number', 'vehicle_number', 'staff_to_contact', 'staff_phone_number', 'purpose', 'entrance_time', 'user')

    col_width = 256 * 25
    for row in rows:
        row_num += 1
        col_num = 0
        for col_num in range(len(row)):
            ws.col(col_num).width = col_width
            if col_num == 0:
                ws.write(row_num, col_num, row[col_num], date_format)
            elif col_num == 6:
                ws.write(row_num, col_num, row[col_num], time_format)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
    return redirect(home)

def exit(request):
    if 'user_name' in request.session:
        return render(request, 'exit.html')
    else:
        return redirect(access_denied)

def check_for_exit(request):
    if 'user_name' in request.session:
        category = request.POST.get('category')
        visitor_id = int(request.POST.get('receipt_number'))
        if category == 'visitor':
            try:
                visitor = visitor_entry_table.objects.get(id = visitor_id)
            except:
                visitor = None
            try:
                exit_check = visitor_exit_table.objects.get(receipt_no = visitor_id)
            except:
                exit_check = None
            if exit_check:
                visitor = None
            context = {
                'visitors': visitor
            }
            return render(request, 'visitor_exit.html', context)
        elif category == 'staff':
            try:
                visitor = staff_vehicle_entry_table.objects.get(id = visitor_id)
            except:
                visitor = None
            try:
                exit_check = staff_vehicle_exit_table.objects.get(receipt_no = visitor_id)
            except:
                exit_check = None

            if exit_check:
                visitor = None
            context = {
                'visitors': visitor
            }
            print(staff_vehicle_entry_table.objects.filter(id = visitor_id).values())
            return render(request, 'staff_vehicle_exit.html', context)
        else:
            try:
                visitor = other_vehicle_entry_table.objects.get(id = visitor_id)
            except:
                visitor = None
            try:
                exit_check = other_vehicle_exit_table.objects.get(receipt_no = visitor_id)
            except:
                exit_check = None
            if exit_check:
                visitor = None
            context = {
                'visitors': visitor
            }
            return render(request, 'other_vehicle_exit.html', context)

    else:
        return redirect(access_denied)

def confirm_exit(request):
    type = request.POST.get('type')
    visitor_id = request.POST.get('receipt_no')
    person = visitor_exit_table()
    staff = staff_vehicle_exit_table()
    other = other_vehicle_exit_table()
    print(visitor_id)
    if type == 'visitor':
        visitor = visitor_entry_table.objects.get(id = visitor_id)
        person.receipt_no = visitor
        person.name = visitor.name
        person.exit_time = datetime.time(datetime.now())
        person.save()
    elif type == 'staff':
        print("in Staff")
        visitor = staff_vehicle_details.objects.get(id= visitor_id)
        staff.receipt_no = visitor
        staff.name = visitor.name
        staff.exit_time = datetime.time(datetime.now())
        staff.save()
    else:
        visitor = other_vehicle_details.objects.get(id = visitor_id)
        other.receipt_no = visitor
        other.name = visitor.name
        other.exit_time = datetime.time(datetime.now())
        other.save()

    return redirect(exit)
