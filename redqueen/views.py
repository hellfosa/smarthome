from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Human, Device, Message, Rule
from .forms import MessageForm, RuleForm, DeviceForm, HumanForm
from datetime import datetime, timedelta
import json

@login_required
def index(request):
    devices_count = Device.objects.count()
    rules_count = Rule.objects.count()
    messages_count = Message.objects.count()
    recent_messages = Message.objects.all().order_by('-pk')[:10]
    return render(request, 'index.html', {'devices': devices_count, 'rules': rules_count, 'messages': messages_count, 'recent_messages': recent_messages})

@login_required
def human(request, pk):
    if request.method == 'GET':
        human = get_object_or_404(Human, pk=pk)
        return render(request, 'human.html', {'human': human})
    elif request.method == 'POST':
        human = get_object_or_404(Human, pk=pk)
        form = HumanForm(request.POST, request.FILES)
        if form.is_valid():
            if human is not None:
                human.name = form.cleaned_data['Name']
                human.sex = form.cleaned_data['Sex']
                human.role = form.cleaned_data['Role']
                human.phone = form.cleaned_data['Phone']
                human.photo = form.cleaned_data['Photo']
                human.save()
            else:
                new = Human()
                new.name = form.cleaned_data['Name']
                new.sex = form.cleaned_data['Sex']
                new.role = form.cleaned_data['Role']
                new.phone = form.cleaned_data['Phone']
                new.photo = form.cleaned_data['Photo']
                new.save()
        else:
            form = HumanForm()
    return redirect('/humans')

@login_required
def human_add(request):
    if request.method == 'GET':
        form = HumanForm(request.POST)
        return render(request, 'human_add.html', {'form': form})
    elif request.method == 'POST':
        form = HumanForm(request.POST, request.FILES)
        if form.is_valid():
            new = Human()
            new.name = form.cleaned_data['Name']
            new.sex = form.cleaned_data['Sex']
            new.role = form.cleaned_data['Role']
            new.phone = form.cleaned_data['Phone']
            new.photo = form.cleaned_data['Photo']
            new.save()
        else:
            form = HumanForm()
            return render(request, 'human_add.html', {'form': form})
    return redirect('/humans')

@login_required
def humans(request):
    humans = Human.objects.all()
    return render(request, 'humans.html', {'humans': humans})

@login_required
def device(request, pk):
    if request.method == 'GET':
        device = get_object_or_404(Device, pk=pk)
        return render(request, 'device.html', {'device': device})
    elif request.method == 'POST':
        device = get_object_or_404(Device, pk=pk)
        form = DeviceForm(request.POST)
        if form.is_valid():
            if device is not None:
                device.name = form.cleaned_data['Name']
                device.group = form.cleaned_data['Group']
                device.channel = form.cleaned_data['Channel']
                device.value = form.cleaned_data['Value']
                device.save()
            else:
                new = Device()
                device.name = form.cleaned_data['Name']
                device.group = form.cleaned_data['Group']
                device.channel = form.cleaned_data['Channel']
                device.value = form.cleaned_data['Value']
                new.save()
        else:
            form = DeviceForm()
    return redirect('/devices')

@login_required
def device_add(request):
    if request.method == 'GET':
        form = DeviceForm(request.POST)
        return render(request, 'device_add.html', {'form': form})
    elif request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            print(request.POST)
            new = Device()
            new.name = form.cleaned_data['Name']
            new.channel = form.cleaned_data['Channel']
            new.value = form.cleaned_data['Value']
            new.group = form.cleaned_data['Group']
            new.save()
        else:
            form = DeviceForm()
            return render(request, 'device_add.html', {'form': form})
    return redirect('/devices')

@login_required
def devices(request):
    devices = Device.objects.all()
    return render(request, 'devices.html', {'devices': devices})

@login_required
def rule(request, pk):
    if request.method == 'GET':
        rule = get_object_or_404(Rule, pk=pk)
        return render(request, 'rule.html', {'rule': rule})
    elif request.method == 'POST':
        rule = get_object_or_404(Rule, pk=pk)
        form = RuleForm(request.POST)
        if form.is_valid():
            if rule is not None:
                rule.name = form.cleaned_data['Name']
                rule.group = form.cleaned_data['Group']
                rule.action = form.cleaned_data['Action']
                rule.start_at = form.cleaned_data['Start_at']
                rule.end_at = form.cleaned_data['End_at']
                rule.repeat = form.cleaned_data['Repeat']
                rule.save()
            else:
                new = Rule()
                rule.name = form.cleaned_data['Name']
                rule.group = form.cleaned_data['Group']
                rule.action = form.cleaned_data['Action']
                rule.start_at = form.cleaned_data['Start_at']
                rule.end_at = form.cleaned_data['End_at']
                rule.repeat = form.cleaned_data['Repeat']
                new.save()
        else:
            form = RuleForm()
    return redirect('/rules')

@login_required
def rule_add(request):
    if request.method == 'GET':
        form = RuleForm(request.POST)
        return render(request, 'rule_add.html', {'form': form})
    elif request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            new = Rule()
            new.name = form.cleaned_data['Name']
            new.group = form.cleaned_data['Group']
            new.action = form.cleaned_data['Action']
            new.start_at = form.cleaned_data['Start_at']
            new.end_at = form.cleaned_data['End_at']
            new.repeat = form.cleaned_data['Repeat']
            new.save()
        else:
            form = RuleForm()
            return render(request, 'rule_add.html', {'form': form})
    return redirect('/rules')

@login_required
def rules(request):
    rules = Rule.objects.all()
    return render(request, 'rules.html', {'rules': rules})

@login_required
def message(request, pk):
    if request.method == 'GET':
        message = get_object_or_404(Message, pk=pk)
        return render(request, 'message.html', {'message': message})
    elif request.method == 'POST':
        message = get_object_or_404(Message, pk=pk)
        form = MessageForm(request.POST)
        if form.is_valid():
            if message is not None:
                message.channel = form.cleaned_data['Channel']
                message.signal = form.cleaned_data['Signal']
                message.save()
            else:
                new = Message()
                new.channel = form.cleaned_data['Channel']
                new.signal = form.cleaned_data['Signal']
                new.save()
        else:
            form = MessageForm()
    return redirect('/messages')

@login_required
def message_add(request):
    if request.method == 'GET':
        form = MessageForm(request.POST)
        return render(request, 'message_add.html', {'form': form})
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new = Message()
            new.channel = form.cleaned_data['Channel']
            new.signal = form.cleaned_data['Signal']
            new.save()
        else:
            form = MessageForm()
            return render(request, 'message_add.html', {'form': form})
    return redirect('/messages')

@login_required
def messages(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('-pk')[:100]
        #Message.objects.all().delete()
        return render(request, 'messages.html', {'messages': messages})

@login_required
def sensors(request):
    time_threshold = datetime.now() - timedelta(hours=24)
    master_temp = Message.objects.filter(channel='/climate/master_bedroom/temperature', published__gt=time_threshold).order_by('-published')
    master_humi = Message.objects.filter(channel='/climate/master_bedroom/humidity', published__gt=time_threshold).order_by('-published')
    master_co2 = Message.objects.filter(channel='/climate/master_bedroom/CO2', published__gt=time_threshold).order_by('-published')
    master_pres = Message.objects.filter(channel='/climate/master_bedroom/pressure', published__gt=time_threshold).order_by('-published')
    return render(request, 'sensors.html', {'master_temp': master_temp, 'master_humi': master_humi, 'master_co2': master_co2, 'master_pres': master_pres})

@login_required
def graphs(request):
    if request.is_ajax():
        q = request.GET.get('query')
        if q is not None and request.GET.get('range') == 'day' and request.GET.get('room') == 'master_bedroom':
            time_threshold = datetime.now() - timedelta(hours=24)
            queryset = Message.objects.filter(channel__icontains='/climate/master_bedroom/', published__gt=time_threshold).order_by('published')
            data = [{"channel": item.channel, "signal": item.signal, "published": item.published.strftime("%d %m %H:%M:%S")} for item in queryset]
            return HttpResponse(json.dumps(data), 'application/javascript')
    else:
        raise Http404("Page for AJAX only")

@login_required
def blank(request):
    devices = Device.objects.all()
    return render(request, 'blank.html', {'devices': devices})
