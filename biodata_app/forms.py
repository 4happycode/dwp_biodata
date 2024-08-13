from django import forms
from django.forms import formset_factory, BaseInlineFormSet
from django.forms import inlineformset_factory
from .models import Pendidikan, PengalamanKerja, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nama', 'alamat', 'no_ktp', 'foto']
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Set field requirements
        self.fields['nama'].required = True
        self.fields['nama'].error_messages = {
            'required': 'nama harus diisi.'
        }
        self.fields['no_ktp'].required = True
        self.fields['no_ktp'].error_messages = {
            'required': 'no_ktp harus diisi.'
        }
        self.fields['foto'].required = True
        self.fields['foto'].error_messages = {
            'required': 'foto harus diisi.'
        }
        self.fields['alamat'].required = False  # bisa kosong

    def clean(self):
        cleaned_data = super().clean()
        # Validate each required field
        for field in ['nama', 'no_ktp', 'foto']:
            value = cleaned_data.get(field)
            if not value:
                self.add_error(field, f"{self.fields[field].label} harus diisi.")


class PendidikanForm(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = ['sekolah', 'jurusan', 'tahun_masuk', 'tahun_lulus']
    
    def __init__(self, *args, **kwargs):
        super(PendidikanForm, self).__init__(*args, **kwargs)
        # Set field requirements and error messages
        self.fields['sekolah'].required = True
        self.fields['jurusan'].required = True
        self.fields['tahun_masuk'].required = True
        self.fields['tahun_lulus'].required = True
    
    def clean(self):
        cleaned_data = super().clean()
        # Validate each required field
        for field in ['sekolah', 'jurusan', 'tahun_masuk', 'tahun_lulus']:
            value = cleaned_data.get(field)
            if not value:
                self.add_error(field, f"{self.fields[field].label} harus diisi.")


class PengalamanKerjaForm(forms.ModelForm):
    class Meta:
        model = PengalamanKerja
        fields = ['perusahaan', 'jabatan', 'tahun', 'keterangan']
    
    def __init__(self, *args, **kwargs):
        super(PengalamanKerjaForm, self).__init__(*args, **kwargs)
        # Set field requirements and custom error messages
        self.fields['perusahaan'].required = True
        self.fields['jabatan'].required = True
        self.fields['tahun'].required = True
        self.fields['keterangan'].required = False
        # Keterangan field is optional, so no required setting here

    def clean(self):
        cleaned_data = super().clean()
        # Validate each required field
        for field in ['perusahaan', 'jabatan', 'tahun']:
            value = cleaned_data.get(field)
            if not value:
                self.add_error(field, f"{self.fields[field].label} harus diisi.")


# Buat formset untuk Pendidikan dan Pengalaman Kerja
PendidikanFormSet = forms.inlineformset_factory(User, Pendidikan, form=PendidikanForm, extra=1, can_delete=True)
PengalamanKerjaFormSet = forms.inlineformset_factory(User, PengalamanKerja, form=PengalamanKerjaForm, extra=1, can_delete=True)

PendidikanFormSetUpdate = inlineformset_factory(User, Pendidikan, form=PendidikanForm, extra=0, can_delete=True)
PengalamanKerjaFormSetUpdate = inlineformset_factory(User, PengalamanKerja, form=PengalamanKerjaForm, extra=0, can_delete=True)