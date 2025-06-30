from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from .models import (
    Complaint
)
from .forms import (
    ComplaintForm

)
from django.contrib import messages
from django.views import View
from django.views.generic import (
    RedirectView,
    DetailView, 
    ListView,
    DeleteView,
    UpdateView,
    CreateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

# class ComplaintCreateView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):

#         form= ComplaintForm()
#         context = {
#             'form': form, 

#         }
#         return render(request, 'services/complaint_form.html', context )
    
#     def post(self, request, *args, **kwargs):

#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.citizen= request.user 
#             complaint.save()
#             # send mail
#             messages.success(request, 'Your complaint submitted ')
#             return redirect('dash:index')

#         else:
#             messages.error(request, 'There is some problem with the data!')

#         context = {
#             'form': form,
#         }
#         return render(request, 'services/complaint.html', context )


class ComplaintCreateView(LoginRequiredMixin,CreateView):

    model = Complaint
    template_name = 'services/complaint_form.html'   
    form_class  = ComplaintForm
    context_object_name = 'form'

    def form_valid(self, form):
        complaint  = form.save(commit=False)
        complaint.citizen = self.request.user 
        messages.success(self.request, "The complaint is created successfuly ")
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, ' the form is invalid ')
        response = super().form_invalid(form)
        return response
    

    def get_success_url(self):
        return reverse_lazy('dash:index')
    
    

class ComplaintDetailView(DetailView):
    
    queryset = Complaint.objects.all()
    template_name = 'services/complaint_detail.html'
    context_object_name = 'complaint'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context 
    

class ComplaintListView(ListView):
    queryset = Complaint.objects.all()
    template_name = 'services/complaints.html'
    context_object_name = 'complaints'

    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)
    

class CancelComplaint(DeleteView):
    model = Complaint
    success_url = reverse_lazy('dash:index')

class ComplaintUpdateView(UpdateView):
    
    queryset = Complaint.objects.all()
    template_name = 'services/update_complaint.html'
    form_class = ComplaintForm
    success_url = reverse_lazy('dash:index')
    

    # def get_context_data(self, request, *args, **kwargs):
    #     context =  super().get(request, *args, **kwargs)
    #     object = self.get_object()
    #     form  = ComplaintForm(instance=object)
    #     context['form']  = form
    #     return context 
    
    def form_valid(self, form):
        complaint = form.save(commit=False)
        
        complaint.citizen = self.request.user
        print('fuck you nigga ')
        print(complaint.citizen)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    


