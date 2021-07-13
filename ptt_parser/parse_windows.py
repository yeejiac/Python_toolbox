from win32gui import *
titles = set()
def foo(hwnd,mouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        titles.add(GetWindowText(hwnd))

EnumWindows(foo, 0)
lt = [t for t in titles if t]
lt.sort()
for t in lt:
 print(t)