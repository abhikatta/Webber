# Webber
### a simple voice system tray assistant app that takes voice input and searches on the default browser.
![image](https://github.com/abhikatta/Webber/assets/76813100/25ee8111-154a-4dc0-8ede-c7c862de6cd9)


![image](https://github.com/abhikatta/Webber/assets/76813100/25cc7135-0670-4eab-ae05-474d1c110aea)

## Compilation:
1. Open Terminal.
2. Change to project directory.
3. Run command:
```
pyinstaller Webber.py --noconsole --datas=[('Webber.ico','./')] 

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
