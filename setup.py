from cx_Freeze import setup, Executable

executables = [Executable('main.py', target_name='construct.exe', base='Win32GUI', icon='construct.ico')]

include_files = ['/UIFiles/Construct.ui', '/UIFiles/supreme_access.ui', '/UIFiles/supreme_window.ui', '/UIFiles/username_change_window.ui',
                 '/UIFiles/update.ui', '/UIFiles/profile_images/', '/UIFiles/TextFiles/']
options = {
    'build_exe': {
        'include_msvcr': True,
        'build_exe': 'build_windows',
        'include_files': include_files,
    }
}

setup(name='hello_world',
      version='0.0.2',
      description='construct.exe',
      executables=executables,
      options=options)
