# -*- mode: python -*-

block_cipher = None


a = Analysis(['0_tetris-game.py'],
             pathex=['C:\\Windows\\System32', 'C:\\Users\\Mashanz\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\Mashanz\\Google Drive\\Python-GUI-using-PyQt5'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='0_tetris-game',
          debug=False,
          strip=False,
          upx=True,
          console=True )
