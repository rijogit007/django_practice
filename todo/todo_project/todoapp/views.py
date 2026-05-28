from django.shortcuts import render,redirect
from todoapp.models import Task
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    task_list=Task.objects.filter(is_completed=False).order_by('updated_at')
    completed_task=Task.objects.filter(is_completed=True)
    
    context={
        
        'task_list':task_list,
        'completed_task':completed_task
        
    }
    return render(request,'home.html',context)



def add_task(request):
    if request.method=="POST":
        taskname=request.POST.get('taskname')
        Task.objects.create(taskname=taskname)  
        return redirect('/')
        
    return render(request,'home.html')    
        
        
        
def mark_as_done(request,id):
    complete=get_object_or_404(Task,id=id)
    complete.is_completed=True
    complete.save()
    return redirect('/')
    
    # return redirect('/')   

def mark_as_undone(request,id):
    incomplete=get_object_or_404(Task,id=id)
    incomplete.is_completed=False
    incomplete.save()
    return redirect('/')


def delete_task(request,id):
    delete=get_object_or_404(Task,id=id)
    delete.delete()
    return redirect('/')
    

def delete_completed_task(request,id):
    
    completed_task=get_object_or_404(Task,id=id)
    
    completed_task.delete()
    
    return redirect('/')


def edit_task(request,id):
    task=get_object_or_404(Task,id=id)
    
    if request.method=='POST':
        update_taskname=request.POST.get('taskname')
        
        
        
        
        task.taskname=update_taskname
        task.save()
       
        return redirect('/')
    context={
            
           "task":task
            
        }
    return render(request,'edit_todo.html',context)    
        
        
        
        