from openerp.osv import osv, fields



class StockOutPackage(osv.osv):
    _name = 'stock.out.package'
    def _make_name(self, cr, uid, ids, name, unknown, context=None):
        result = {}
        for each in ids:
            record = self.browse(cr, uid, each, context)
            name = (record.tracking_number or '')
            result[each] = "%s.gif" % name
        return result


    _columns = {
	'name': fields.char('Name'),
#	'name': fields.function(_make_name, type="char", method=True, string='Name', select="1", size=150, store=True),
	'picking': fields.many2one('stock.picking', 'Delivery Order'),
        'mailpiece_shape': fields.many2one('usps.mailpiece.shape',
            'MailPiece Shape'),
	'refund_status': fields.text('Refund Status'),
	'refund_approved': fields.boolean('Refund Approved'),
        'label_sub_type': fields.selection([
                ('None', 'None'),
                ('Integrated', 'Integrated')
        ], 'Label Sub Type'),
        'integrated_form_type': fields.selection([
                ('Form2976', 'Form2976(Same as CN22)'),
                ('Form2976A', 'Form2976A(Same as CP72)'),
        ], 'Form Type'),
        'mailpiece_shape': fields.many2one('usps.mailpiece.shape',
            'MailPiece Shape'),
        'mailpiece_dimensions': fields.many2one('usps.mailpiece.dimensions',
            'MailPiece Dimensions'),
	'tracking_number': fields.char('Tracking Number'),
	'declared_value': fields.float('Declared Value'),
	'weight': fields.float('Package Weight'),
	'length': fields.float('Length'),
	'width': fields.float('Width'),
	'height': fields.float('Height'),
	'include_postage': fields.boolean('Include Postage'),
	'cost': fields.float('Package Cost'),
	'digest': fields.binary('Information digest for DIGEST'),
	'file': fields.binary('Label Image'),
    }

