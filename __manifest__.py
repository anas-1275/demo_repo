{
    'name':"To-Do",
    'author':"Anas Ahmed",
    'catagory':"",
    'version':"17.0.0.1.0",
    'depends':['base','account','sale_management','mail'
    ],
     'data':[
         'security\security.xml',
         'security\ir.model.access.csv',
         'data\sequence.xml',
         'views\\base_view.xml',
         'views\\todo_management_view.xml',
         'views\\res_partner_inherit.xml',
         'Reports\\todo_report.xml',
         'wizerd\select_user_view_wizerd.xml',

         ],
         'assets':{  
         },
    'applications':True,

}