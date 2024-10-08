from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True, readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('pemesanan.ruangan'))
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesanan = fields.Char(string='Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Datetime(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft')
    catatan = fields.Text(string='Catatan Pemesanan')

    _sql_constraints = [
        ('unique_nama_pemesanan', 'UNIQUE(nama_pemesanan)', 'Nama pemesanan harus unik!'),
    ]

    @api.constrains('tanggal_pemesanan', 'ruangan_id')
    def _check_ruangan_date(self):
        for record in self:
            overlapping_reservations = self.search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)  # Ignore the current record
            ])
            if overlapping_reservations:
                raise ValidationError('Ruangan sudah dipesan pada tanggal ini.')

    def set_on_going(self):
        for record in self:
            record.status_pemesanan = 'on_going'

    def set_done(self):
        for record in self:
            record.status_pemesanan = 'done'
