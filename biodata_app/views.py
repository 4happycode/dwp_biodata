from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, PendidikanFormSet, PengalamanKerjaFormSet, PendidikanFormSetUpdate, PengalamanKerjaFormSetUpdate
from .models import Pendidikan, PengalamanKerja, User

def user_form_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)
        pendidikan_formset = PendidikanFormSet(request.POST, request.FILES, prefix='pendidikan')
        pengalaman_formset = PengalamanKerjaFormSet(request.POST, request.FILES, prefix='pengalaman')

        if user_form.is_valid() and pendidikan_formset.is_valid() and pengalaman_formset.is_valid():
            user = user_form.save()  # Simpan data pengguna
            # Set instance untuk formset dan simpan
            pendidikan_formset.instance = user
            pendidikan_formset.save()

            pengalaman_formset.instance = user
            pengalaman_formset.save()

            return redirect('thank_you')
        else:
            # Jika form tidak valid, Anda bisa mencetak error untuk debugging
            print("User Form Errors:", user_form.errors)
            print("Pendidikan Formset Errors:", pendidikan_formset.errors)
            print("Pengalaman Kerja Formset Errors:", pengalaman_formset.errors)

    else:
        user_form = UserForm()
        pendidikan_formset = PendidikanFormSet(prefix='pendidikan')
        pengalaman_formset = PengalamanKerjaFormSet(prefix='pengalaman')

    return render(request, 'form_template.html', {
        'user_form': user_form,
        'pendidikan_formset': pendidikan_formset,
        'pengalaman_formset': pengalaman_formset
    })


def user_list_view(request):
    users = User.objects.all()  # Ambil semua data pengguna
    return render(request, 'user_list.html', {'users': users})


def user_detail_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    pendidikan_list = Pendidikan.objects.filter(user=user)
    pengalaman_list = PengalamanKerja.objects.filter(user=user)
    
    return render(request, 'user_detail.html', {
        'user': user,
        'pendidikan_list': pendidikan_list,
        'pengalaman_list': pengalaman_list
    })
    

def user_update_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        pendidikan_formset = PendidikanFormSet(request.POST, request.FILES, instance=user, prefix='pendidikan')
        pengalaman_formset = PengalamanKerjaFormSet(request.POST, request.FILES, instance=user, prefix='pengalaman')

        if user_form.is_valid() and pendidikan_formset.is_valid() and pengalaman_formset.is_valid():
            user = user_form.save()

            # Save formsets
            pendidikan_formset.instance = user
            pendidikan_formset.save()
            pengalaman_formset.instance = user
            pengalaman_formset.save()

            return redirect('thank_you')
        else:
            # Debugging: Tampilkan error
            print("User Form Errors:", user_form.errors)
            print("Pendidikan Formset Errors:", pendidikan_formset.errors)
            print("Pengalaman Kerja Formset Errors:", pengalaman_formset.errors)
    else:
        user_form = UserForm(instance=user)
        pendidikan_formset = PendidikanFormSetUpdate(instance=user, prefix='pendidikan')
        pengalaman_formset = PengalamanKerjaFormSetUpdate(instance=user, prefix='pengalaman')

    return render(request, 'form_template.html', {
        'user_form': user_form,
        'pendidikan_formset': pendidikan_formset,
        'pengalaman_formset': pengalaman_formset
    })


def thank_you_view(request):
    return render(request, 'thank_you.html')