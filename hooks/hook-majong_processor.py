from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('majong_processor')
# hiddenimports = collect_submodules('qrcode_generator')
print('hiddenimports: %s' % hiddenimports)
