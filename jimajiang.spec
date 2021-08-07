# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['manage.py'],
             pathex=['C:\\Users\\Mark\\iCloudDrive\\zaizai\\majong'],
             binaries=[],
             datas=[('qrcode_generator/img', './qrcode_generator/img'), ('qrcode_generator/menmiao.ttf', './qrcode_generator'), ('majong_processor/templates', './majong_processor/templates')],
             hiddenimports=['majong_processor'],
             hookspath=['hooks/'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='jimajiang',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               # Tree('..\\qrcode_generator\\img', prefix='img\\'),
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='jimajiang')
