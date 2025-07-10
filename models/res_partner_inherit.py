from odoo import fields,models


class ResPartner(models.Model):
    _inherit="res.partner"



    todo_id=fields.Many2one('todo.management')
    number_of_tasks=fields.Integer(compute="_compute_number_of_tasks")

    def _compute_number_of_tasks(self):
        for rec in self:
            rec.number_of_tasks=self.env['todo.management'].search_count([('Assign_to', '=', rec.name)])


    def action_of_tasks(self):
        for rec in self:
            action=rec.env['ir.actions.actions']._for_xml_id('todo_management.todo_action')
            action['context'] ={'default_todo_id': rec.id}
            action['domain'] = [('Assign_to', '=', rec.name)]
            return action