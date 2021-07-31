from cx_Freeze import setup, Executable

executables = [Executable('main.py', target_name='construct.exe', base='Win32GUI', icon='construct.ico')]
include_files = ['LimboQT.ui', 'supreme_access.ui', 'supreme_window.ui', 'username_change_window.ui', 'update.ui']
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
