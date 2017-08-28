# Wox-UUID

This plugin generates UUIDs that you can easily copy and paste.

Screenshots soon.

## Tips for Wox plugin development

### Use `print`

It will generate a Windows message box.

### Check the `python.exe` in use

On my system I have both `C:\Program Files\Python36` and `C:\Program Files\Anaconda3`.
I just opened a prompt and run `pip install pyperclip`, but the plugin wasn't loading.
I checked `C:\Users\<me>\AppData\Roaming\Wox\Logs\1.3.183\<today>.log` and found the module was not loading.
I realized that I installed the plugin with Anaconda3 but was using Python36 in Wox settings.

### Permission error on `pip install`.

Just run inside an Administrator PowerShell. Again, be careful which `pip` you are using.
Remember you can also invoke it with `python -m pip install`.

