# Webber
### a simple system tray voice assistant app that takes voice input and searches on the default browser.
### Click [here](https://github.com/abhikatta/Webber/releases/download/proto1/Webber.zip) to download app.
![image](https://github.com/abhikatta/Webber/assets/76813100/25ee8111-154a-4dc0-8ede-c7c862de6cd9)


![image](https://github.com/abhikatta/Webber/assets/76813100/25cc7135-0670-4eab-ae05-474d1c110aea)

## Compilation:
1. Open Terminal.
2. Change current directory to project directory.
3. Run command:
```
pyinstaller Webber.py --noconsole --add-data './Webber.ico;.' 

```
4. [Optional] Make any changes if you want to the `Webber.spec` file and run
   ```
   pyinstaller Webber.spec
   ```
That's it!

### Bonus: If you want to open webber on system sign-in, you can add it to start-up apps by following below steps:

1. Press `Win+r` on your windows machine.
2. Type in: 
   ```
   shell:startup
   ```
3. Add `Webber.exe` to `path/to/startup/folder`.
   And you're done!

## Check out [infi.systray](https://pypi.org/project/infi.systray/) for more info/customization.
