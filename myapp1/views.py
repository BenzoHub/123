from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.

def index_page(request):

    all_workers = Worker.objects.all()
    print(all_workers)

    if request.method=='POST':
        new_worker = Worker(name='Petya', surname='Ivanov', salary=30000)
        new_worker.save()
        Worker.objects.create(name='Vasya', surname='Ivanov', salary=31000)

    for i in all_workers:
        print(f'Фамилия: {i.surname}, Зп: {i.salary}, ID: {i.id}')

    return render(request, 'index.html')