from odoo import models, fields, api


class ScadaLiveData(models.Model):
    _name = 'scada.livedata'

    shift = fields.Char(string='Production Shift', help='Production Shift', size=50)
    operator_Id = fields.Char(string='Machine Operator Id', help='Machine Operator Id', size=50)
    machine_code = fields.Char(string='Machine Code', help='Machine Code', size=100)
    status = fields.Char(string='Machine Status', help='Machine Status', size=50)
    nail_dia = fields.Float(string='Product Daimeter', help='Product Daimeter', digits=(18,2))
    nail_length = fields.Float(string='Product length', help='Product length', digits=(18,2))
    nail_speed = fields.Float(string='Machine Running Speed', help='Machine Running Speed',  digits=(18,2))
    nail_produced = fields.Float(string='Produceded Qty', help='Produceded Qty',digits=(18,2))
    t_date = fields.Datetime(string='Transaction Date', help='Transaction Date')
    hours = fields.Integer(string='Total Production Hours', help='Total Production Hours')
    minute = fields.Integer(string='Total Production Minutes',help='Total Production Minutes')
    input_code = fields.Char(string='Rawmaterial/WIP Product Code',help='Rawmaterial/WIP Product Code', size=100)
    input_coiltag= fields.Char(string='Tag No/ Cast No. Appears on Tag', help='Tag No/ Cast No. Appears on Tag', size=300)
    output_code = fields.Char(string='WIP/Finished Product Code (WIP- Work in processes)', help='WIP/Finished Product Code (WIP- Work in processes)', size=100)
    inupt_coil_weight = fields.Float(string='Production Shift', help='Rawmaterial/WIP Product Weight', digits=(18,2))
    machine_code = fields.Char(string='Machine Code',help='Machine Code',size=100)
    shift_ope_code = fields.Char(string='Shift Supervisor Code',help='Shift Supervisor Code', size=100)
    crane_ope_code = fields.Char(string='Crane Operator Code',help='Crane Operator Code', size=100)
    forklift_ope_code = fields.Char(string='Forklift Operator Code', help='Forklift Operator Code', size=100)
    mach_ope_code = fields.Char(string='Machine Operator Code', help='Machine Operator Code', size=100)
    ope_code1 = fields.Char(string='Machine Operator Code1', help='Machine Operator Code1', size=100)
    ope_code2 = fields.Char(string='Machine Operator Code2', help='Machine Operator Code2', size=100)
    starttime = fields.Datetime(string='Production Start Time', help='Production Start Time')
    endtime = fields.Datetime(string='Production end Time', help='Production end Time')
    input_dia = fields.Float(string='Product Diameter', help='Product Diameter',digits=(18,2))
    input_length = fields.Float(string='Product Size', help='Product Size',digits=(18,2))
    output_dia = fields.Float(string='Output Product Diameter',help='Output Product Diameter',digits=(18,2))
    output_length = fields.Float(string='Length of Output Product',help='Length of Output Product',digits=(18,2))
    scrap = fields.Float(string='Powder Scrap weight (Manual entry in SCADA)', help='Powder Scrap weight (Manual entry in SCADA)',digits=(18,2))
    t_time = fields.Datetime(string='Tranction Time', help='Tranction Time')
    coil_status = fields.Char(string='Coil Status (Active or Stop)', help='Coil Status (Active or Stop)', size=50)
    tab_date = fields.Datetime(string='Transaction Date (From Android Application)', help='Transaction Date (From Android Application)')
    tab_actual_weight = fields.Float(string='Actual Weight record from Android application', help='Actual Weight record from Android application',digits=(18,3))
    tab_scrap_weight = fields.Float(string='Actual Scrap Weight record from Android Application',help='Actual Scrap Weight record from Android Application',digits=(18,3))
    tab_mac_id = fields.Char(string='Android Machine Mac Id (TAB/Mobile)', help='Android Machine Mac Id (TAB/Mobile)',size=50)
    tab_mcn_code = fields.Char(string='Machine Code', help='Machine Code',size=50)
    tab_user_id = fields.Char(string='User Id (Loged in Android devise)',help='User Id (Loged in Android devise)',size=50)
    tab_scrap_type = fields.Char(string='Rawmaterial Product In barcode scan from Android Application', help='Rawmaterial Product In barcode scan from Android Application', size=50)
    tab_in_barcode = fields.Char(string='WIP/Finished Product barcode scan from android application', help='WIP/Finished Product barcode scan from android application', size=50)
    tab_out_barcode = fields.Char(string='Scrap Type', help='Scrap Type', size=50)
    tab_scrap_powder_kg = fields.Float(string='Scrap weight(Powder) record from Android App.', help='Scrap weight(Powder) record from Android App.',digits=(18,3))
    tab_scrap_coil_kg = fields.Float(string='Scrap weight (of coil) record from Android App.', help='Scrap weight (of coil) record from Android App.',digits=(18,3))
