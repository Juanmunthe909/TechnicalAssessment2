from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    nama_ruangan = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('meeting_kecil', 'Meeting Room Kecil'),
        ('meeting_besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1A', '1A'),
        ('1B', '1B'),
        ('1C', '1C'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary(string='Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')

    _sql_constraints = [
        ('unique_nama_ruangan', 'UNIQUE(nama_ruangan)', 'Nama ruangan harus unik!'),
    ]
