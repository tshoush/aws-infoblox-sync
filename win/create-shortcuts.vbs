' VBScript to create desktop shortcuts for AWS to InfoBlox Tag Mapper
' This script creates shortcuts with custom icons and descriptions

Option Explicit

Dim objShell, objFSO, strDesktop, strAppPath
Dim objShortcut, strIconPath

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get paths
strDesktop = objShell.SpecialFolders("Desktop")
strAppPath = "C:\infoblox-tag-mapper"

' Check if application directory exists
If Not objFSO.FolderExists(strAppPath) Then
    MsgBox "Application directory not found: " & strAppPath & vbCrLf & _
           "Please ensure the application is installed in C:\infoblox-tag-mapper\", _
           vbError, "Directory Not Found"
    WScript.Quit
End If

' Create Start shortcut
Set objShortcut = objShell.CreateShortcut(strDesktop & "\Start Tag Mapper.lnk")
objShortcut.TargetPath = strAppPath & "\start-tag-mapper.bat"
objShortcut.WorkingDirectory = strAppPath
objShortcut.WindowStyle = 1
objShortcut.IconLocation = "shell32.dll, 137"
objShortcut.Description = "Start AWS to InfoBlox Tag Mapper Web Interface"
objShortcut.Save

' Create Stop shortcut
Set objShortcut = objShell.CreateShortcut(strDesktop & "\Stop Tag Mapper.lnk")
objShortcut.TargetPath = strAppPath & "\stop-tag-mapper.bat"
objShortcut.WorkingDirectory = strAppPath
objShortcut.WindowStyle = 1
objShortcut.IconLocation = "shell32.dll, 131"
objShortcut.Description = "Stop AWS to InfoBlox Tag Mapper"
objShortcut.Save

' Create Status shortcut
Set objShortcut = objShell.CreateShortcut(strDesktop & "\Tag Mapper Status.lnk")
objShortcut.TargetPath = strAppPath & "\status-tag-mapper.bat"
objShortcut.WorkingDirectory = strAppPath
objShortcut.WindowStyle = 1
objShortcut.IconLocation = "shell32.dll, 23"
objShortcut.Description = "Check AWS to InfoBlox Tag Mapper Status"
objShortcut.Save

' Create Logs shortcut
Set objShortcut = objShell.CreateShortcut(strDesktop & "\Tag Mapper Logs.lnk")
objShortcut.TargetPath = strAppPath & "\logs-tag-mapper.bat"
objShortcut.WorkingDirectory = strAppPath
objShortcut.WindowStyle = 1
objShortcut.IconLocation = "shell32.dll, 56"
objShortcut.Description = "View AWS to InfoBlox Tag Mapper Logs"
objShortcut.Save

' Create folder shortcut
Set objShortcut = objShell.CreateShortcut(strDesktop & "\Tag Mapper Files.lnk")
objShortcut.TargetPath = strAppPath
objShortcut.WindowStyle = 1
objShortcut.IconLocation = "shell32.dll, 4"
objShortcut.Description = "Open AWS to InfoBlox Tag Mapper Files"
objShortcut.Save

MsgBox "Desktop shortcuts created successfully!" & vbCrLf & vbCrLf & _
       "Created shortcuts:" & vbCrLf & _
       "• Start Tag Mapper" & vbCrLf & _
       "• Stop Tag Mapper" & vbCrLf & _
       "• Tag Mapper Status" & vbCrLf & _
       "• Tag Mapper Logs" & vbCrLf & _
       "• Tag Mapper Files", _
       vbInformation, "Shortcuts Created"