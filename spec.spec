# -*- mode: python -*-
programName = "textWid" # название программы
folder_to_add = 'resources'
file_to_compile = 'gaTectum_app.pyw'
main_icon = 'resources\\icon_main.ico'

block_cipher = None

a = Analysis([file_to_compile],
             # pathex=['C:\\Users\\Андрей\\OneDrive\\Documents\\Программирование\\Python\\- hotEges2\\- Builds\\2.2.1\\2.2.1'],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

def extra_datas(mydir):
    "Добавляет все файлы из папки в а - для компиляции"
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################

# append the 'data' dir
a.datas += extra_datas(folder_to_add)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=programName,
          debug=False,
          icon=main_icon,
          strip=None,
          upx=True,
          console=False)
