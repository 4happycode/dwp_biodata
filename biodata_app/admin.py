from django.contrib import admin
from django.utils.html import format_html
from .models import Pendidikan, PengalamanKerja, User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'no_ktp', 'foto_tag')
    search_fields = ('nama', 'alamat', 'no_ktp')
    
    readonly_fields = ('foto_tag',)

    def foto_tag(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.foto.url))
        return "-"

    foto_tag.short_description = 'Foto'

@admin.register(Pendidikan)
class PendidikanAdmin(admin.ModelAdmin):
    list_display = ('user', 'sekolah', 'jurusan', 'tahun_masuk', 'tahun_lulus')
    search_fields = ('sekolah', 'jurusan')
    list_filter = ('user',)

@admin.register(PengalamanKerja)
class PengalamanKerjaAdmin(admin.ModelAdmin):
    list_display = ('user', 'perusahaan', 'jabatan', 'tahun', 'keterangan')
    search_fields = ('perusahaan', 'jabatan')
    list_filter = ('user',)
