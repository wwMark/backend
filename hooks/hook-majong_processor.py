from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('majong_processor')
print('hiddenimports: %s' % hiddenimports)