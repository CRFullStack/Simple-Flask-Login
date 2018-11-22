from cx_Freeze import setup, Executable

#includefiles = [
#    'Flask_Login\static\content\bootstrap.css',
#    'Flask_Login\static\content\bootstrap.min.css',
#    'Flask_Login\static\content\site.css',
#    'Flask_Login\static\fonts\glyphicons-halflings-regular.eot',
#    'Flask_Login\static\fonts\glyphicons-halflings-regular.svg',
#    'Flask_Login\static\fonts\glyphicons-halflings-regular.ttf',
#    'Flask_Login\static\fonts\glyphicons-halflings-regular.woff',
#    ]

setup(name = "Flask-login" ,
      version = "0.1" ,
      description = "Web site" ,
      executables = [Executable("runserver.py")]
      )
