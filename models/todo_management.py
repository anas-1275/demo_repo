from odoo import fields,models,api
from odoo.exceptions import ValidationError
from datetime import timedelta



class Task(models.Model):
    _name="todo.management"
    _inherit=['mail.thread','mail.activity.mixin']



    
    estmated_time = fields.Integer(string="Estmated Time(H)")
    
    task_name=fields.Char()
    Assign_to=fields.Many2one('res.partner')
    due_date=fields.Date()
    ref=fields.Char(default="New" ,readonly=1)
    description=fields.Char()
    status=fields.Selection([
        ('new','New'),
        ('in progress','In Progress'),
        ('completed','Completed'),
        ('closed','Closed'),
        ])
    active=fields.Boolean(default=True)
    time_sheet_ids=fields.One2many(comodel_name='time.sheet.line',inverse_name='todo_id')
    is_late=fields.Boolean()
        


    @api.constrains('estmated_time','time_sheet_ids')
    def check_estmated_time(self):
        for rec in self:
            total_time = sum(rec.time_sheet_ids.mapped('time'))
            if rec.estmated_time < total_time:
                raise ValidationError('You Can Not Exceed Estimated Time')
            
    def action_total_step(self):
        print(sorted(set(self.time_sheet_ids.mapped('step'))))
        
            

    def action_closed(self):
        for rec in self:
            rec.status="closed"

    def check_due_date(self):
        todo_ids=self.search([])
        for rec in todo_ids:
            if rec.due_date and rec.due_date < fields.date.today():
                rec.is_late=True 

    @api.model
    def create(self,vals):
        res= super(Task, self).create(vals)
        if res.ref == 'New':
            res.ref=self.env['ir.sequence'].next_by_code('todo_seq')
        return res
    

    def action_select_user(self):
        for rec in self:
          action=rec.env['ir.actions.actions']._for_xml_id('todo_management.action_open_wizerd_select_user')
          action['context'] ={'default_todo_id': rec.id}
          return action
        

    def action_new(self):
        for rec in self:
            rec.status='new'
    
    def action_in_progress(self):
        for rec in self:
            rec.status='in progress'
   
    def action_completed(self):
        for rec in self:
            rec.status='completed'
            
    @api.model
    def write(self, vals):
        if not self.env.user.has_group('todo_management.todo_manager_group'):
            allowed_fields = ['status']
            if any(field not in allowed_fields for field in vals.keys()):
                raise ValidationError("You can only update the task status from In Progress to Completed.")
        return super(Task, self).write(vals)
        
    

    # @api.onchange('status')
    # def _onchange_price(self):
    #  if self.status == 'new':
    #     return {
    #         'warning': {
    #             'title': "تحذير",
    #             'message': "السعر لا يمكن أن يكون أقل من صفر!",
    #         }
    #     }

    
    
    
    


class TimeSheetLine(models.Model):

    _name="time.sheet.line"

    todo_id=fields.Many2one('todo.management')

    step=fields.Char()
    time=fields.Integer(string="Time(H)")
   
            
    
    
            
    
    
    
    

    # @api.constrains('time')
    # def total_time(self):
        
    #     total=0
    #     for rec in self:
    #          total =rec.time + total
    #         # print(total)
    #     return total
    


                


