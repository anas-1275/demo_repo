from odoo import fields,models
from odoo.exceptions import ValidationError

class SelectUser(models.TransientModel):
    _name="select.user"


    Assign_to=fields.Many2one('res.partner')
    todo_id=fields.Many2one('todo.management')

   #  def action_confirm(self):
   #      for rec in self:
   #         if rec.todo_id.status == 'new' or rec.todo_id.status == 'in progress':
   #            rec.todo_id.Assign_to = rec.Assign_to

   #         else:
   #            raise ValidationError("This State Not New or In progress")



    def action_confirm(self):
        active_ids = self.env.context.get('active_ids', [])#------> get all selected ids
        todos = self.env['todo.management'].browse(active_ids)#------>get the ids record

        for todo in todos:
            if todo.status in ['new', 'in progress']:
                todo.Assign_to = self.Assign_to
            else:
                raise ValidationError("This State Not New or In Progress")
           

  
