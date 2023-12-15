# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['utm-sensor.py'],
             pathex=['/home/yet/Work/utm-sensor'],
             binaries=[],
             datas=[('assets/sslCheckUrls.txt', 'assets/'), ('assets/urls.txt', 'assets/'), ('assets/malware.txt', 'assets/'), ('assets/cert.pem', 'assets/'), ('assets/domains.txt', 'assets/'), ('assets/testdata.json', 'assets/'), ('assets/cert.der', 'assets/'), ('assets/maildomain.txt', 'assets/'), ('assets/ips.txt', 'assets/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_bootlocale'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='utm-sensor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
