try:
    from tkinter import *
    import time
    import os
    import sys
    import pwd
    import subprocess
    from sys import exit
except (ImportError, OSError, PermissionError) as error:
    import subprocess
    import sys
    print (error)
    msg = """display dialog "Spotium could not load dependencies. Please join the discord for assistance." with title "Spotium" with icon stop buttons {"EXIT"}"""
    subprocess.call("osascript -e '{}'".format(msg), shell=True)
    exit()
try:
    USER_NAME = pwd.getpwuid(os.getuid()).pw_name
    logpath = "/Users/" + USER_NAME + "/Spotium/spotiumlog.txt"
    localpath = "/Users/" + USER_NAME + "/Spotium"
    VERSION = '6.0'
    global loading
    loading = True
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    if os.path.exists(localpath):
        pass
    else:
        os.mkdir(localpath)
    def on_drag(event):
        if not window.winfo_containing(event.x_root, event.y_root).winfo_class() == "Button":
            x = window.winfo_pointerx() - window._offsetx
            y = window.winfo_pointery() - window._offsety
            window.geometry(f"+{x}+{y}")
    def on_click(event):
        window._offsetx = event.x
        window._offsety = event.y
    def btn_exit():
        global loading
        if not loading: 
            with open (logpath, "a") as f:
                logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                f.write("\n" + logprefix + 'Goodbye!')
            def fade_out():
                opacity = window.attributes("-alpha")
                if opacity > 0.0:
                    opacity -= 0.2
                    window.attributes("-alpha", opacity)
                    window.after(50, fade_out)
                else:
                    exit()
            fade_out()
        else:
            pass
    def btn_blckads():
        global loading
        if loading == False:
            loading = True
            mainbutton.config(file = resource_path("loading.png"))
            window.update()
            if os.path.exists(localpath + "/.patch"):
                os.unlink(localpath + "/.patch")
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killing Spotify')
                subprocess.call(['pkill', 'Spotify'])
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killed Spotify')
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Unpatching Spotify')
                subprocess.call(['sh', '-c', 'curl -k -sS -f https://app.spotium.dev/mac/unpatch.sh | sh'])
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Unpatched Spotify')
                mainbutton.config(file = resource_path("btn-block.png"))
                window.update()
                loading = False
            else:
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killing Spotify')
                subprocess.call(['pkill', 'Spotify'])
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killed Spotify')
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Patching Spotify')
                subprocess.call(['sh', '-c', 'curl -k -sS -f https://app.spotium.dev/mac/patch.sh | sh'])
                if os.path.exists(localpath + "/failedversion.txt"):
                    if not os.path.exists(localpath + "/bypass.spotium"):
                        with open (localpath + "/failedversion.txt", "r") as f:
                            r1 = f.readline().strip()
                            r2 = f.readline().strip()
                        ins = f'{r1} < {r2}'
                        os.unlink(localpath + "/failedversion.txt")
                        msg = """display dialog "Spotify version mismatch!\n"""  + ins + """\nThe patch will still most likely work but please be aware that some features may not work." with title "Spotium" with icon caution buttons {"Run patch anyway", "Okay"}"""
                        result = subprocess.check_output("osascript -e '{}'".format(msg), shell=True, universal_newlines=True)
                        if "button returned:Run patch anyway" in result:
                                with open(localpath + "/bypass.spotium", "w") as f:
                                    f.write("@greioghj408ghioreno")
                                    f.close()
                                loading = False
                                btn_blckads()
                        else:
                                with open (logpath, "a") as f:
                                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                                    f.write("\n" + logprefix + 'Patching Spotify failed! Version mismatch')
                                mainbutton.config(file = resource_path("btn-block.png"))
                                window.update()
                                loading = False
                    else:
                        os.unlink(localpath + "/bypass.spotium")
                        with open (logpath, "a") as f:
                            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                            f.write("\n" + logprefix + 'Patched Spotify')
                        mainbutton.config(file = resource_path("btn-unblock.png"))
                        window.update()
                        loading = False
                        with open (localpath + "/.patch", "w") as f:
                            f.write("@oifhi3hjf90g24u0f9ju2")
                            f.close()
                else:
                    with open (logpath, "a") as f:
                        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                        f.write("\n" + logprefix + 'Patched Spotify')
                    mainbutton.config(file = resource_path("btn-unblock.png"))
                    window.update()
                    loading = False
                    with open (localpath + "/.patch", "w") as f:
                        f.write("@oifhi3hjf90g24u0f9ju2")
                        f.close()
        else:
            pass
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Spotium ' + VERSION )
    def fade_in():
        opacity = window.attributes("-alpha")
        if opacity < 1.0:
            opacity += 0.2
            window.attributes("-alpha", opacity)
            window.after(50, fade_in)
        if opacity >= 1:
            with open(localpath + '/.data', 'r') as f:
                data = f.read()
                f.close()
            if '@nxkclvd89rt4uy38r952789rj23' in data:
                data = data.replace('@nxkclvd89rt4uy38r952789rj23', '@fngeoiru3og398rh98rwji')
                with open(localpath + '/.data', 'w') as f:
                    f.write(data)
                    f.close()
                btn_blckads()
    window = Tk()
    window.geometry("824x443")
    window.configure(bg = "#212121")
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Building menu')
    canvas = Canvas(window,bg = "#212121",height = 443,width = 824,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    window.attributes("-alpha", 0.0)
    background_img = PhotoImage(file = resource_path("background.png"))
    background = canvas.create_image(
        412.0, 223.5,
        image=background_img)
    def center_window(width=824, height=443):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    center_window()
    exitcircle = PhotoImage(file = resource_path("exit.png"))
    exitbutton = Button(image = exitcircle,borderwidth = 0,highlightthickness = 0,command = btn_exit,relief = "flat")
    exitbutton.place(x = 5, y = 6,width = 20,height = 20)  
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Menu built')
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Checking if Spotify is installed')
    if os.path.exists("/Applications/Spotify.app"):
        with open (logpath, "a") as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + 'Spotify OK')
        if not os.path.exists(localpath + "/.data"):
            with open(localpath + '/.data', "w") as f:
                f.write("@nxkclvd89rt4uy38r952789rj23")
                f.close()
        if os.path.exists(localpath + "/.patch"):
            mainbutton = PhotoImage(file = resource_path("btn-unblock.png"))
        else:
            mainbutton = PhotoImage(file = resource_path("btn-block.png"))
        blockadsbutton = Button(image = mainbutton,borderwidth = 0,highlightthickness = 0,command = btn_blckads,relief = "flat")
        blockadsbutton.place(x = 200, y = 205,width = 422,height = 105)
    else:
        with open (logpath, "a") as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + 'Spotify is not installed')
            msg = """display dialog "Spotium could not find any installation of Spotify in your applications folder. Please make sure Spotify is installed." with title "Spotium" with icon caution buttons {"EXIT"}"""
            subprocess.call("osascript -e '{}'".format(msg), shell=True)
            exit()
    window.bind("<B1-Motion>", on_drag)
    window.bind("<Button-1>", on_click)
    window.resizable(False, False)
    window.overrideredirect(True)
    window.update()
    window.after(500, fade_in)
    window.mainloop()
except (Exception, OSError, PermissionError) as error:
    msg = """display dialog "Something went wrong while Spotium was running and it now has to close. Please join the discord for assistance.\n\nHere is your error: """ + format(error) + """" with title "Spotium" with icon stop buttons {"EXIT"}"""
    subprocess.call("osascript -e '{}'".format(msg), shell=True)
    if os.path.exists(logpath):
        with open (logpath, 'a') as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + "Something went wrong while Spotium was running ->" + format(error))
    else:
        with open (logpath, 'w') as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + "Something went wrong while Spotium was running ->" + format(error))