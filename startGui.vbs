set ws=WScript.CreateObject("WScript.Shell")
currentpath = createobject("Scripting.FileSystemObject").GetFolder(".").Path
GUI_Tools = currentpath & "\startGui.bat"
ws.Run GUI_Tools,0