import os
import sys
import webview

def get_entry_point():
    # المسار داخل ملف EXE بعد التحزيم
    if hasattr(sys, '_MEIPASS'):
        path_in_exe = os.path.join(sys._MEIPASS, 'dist', 'index.html')
        if os.path.exists(path_in_exe):
            return path_in_exe
        return os.path.join(sys._MEIPASS, 'index.html')
    
    # المسار أثناء التشغيل العادي من المجلد
    return os.path.abspath(os.path.join('dist', 'index.html'))

entry = get_entry_point()

window = webview.create_window('Belgian Salary Tracker', entry, width=1280, height=800, resizable=True)
webview.start(http_server=True)