# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['color_detection_exe.py'],
    pathex=[],
    binaries=[],
    datas=[('colors.csv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['IPython', 'jedi', 'jupyter', 'jupyter_client', 'jupyter_core', 'ipykernel', 'debugpy', 'pygments', 'parso', 'wcwidth', 'psutil', 'zmq', 'tornado', 'matplotlib_inline', 'executing', 'asttokens', 'comm', 'nest_asyncio2'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Color Detection',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
