# 📌 Auto Clicker

A lightweight, multi-threaded Python auto-clicker with customizable hotkeys. Optimized for Sky: Children of the Light, but adaptable for other contexts.

## 🚀 Features
* ⌨️ Hotkey support: Start/stop with your own shortcut
* 🖱️ Mouse automation: Simulate fast and responsive clicks
* 🧵 Multi-threaded architecture: Smooth concurrent execution
* 🎮 Game-friendly: Designed with Sky: Children of the Light in mind
* 💻 Cross-platform-ready: Tested on Windows 11, adaptable for others

## 🛠️ Requirements
* Python 3.12 or higher
* `pynput` library

## Installation Guide
Make sure that Python version is **Python 3.12.10 or higher**

### 🪟 Windows
Install Python  
  1. Download Python from the [python official website](https://www.python.org/downloads/)
  2. Run the installer and **check the box "Add Python to PATH"**
  3. Click "Install Now"

Or use Command Prompt (Windows 11):  
```Cmd
winget install Python.Python
```

Install the `pynput` library via Command Prompt (cmd)
```Cmd
pip install pynput
```

### 🐧 Linux (Ubuntu / Debian)
Install Python3 (*Updated your OS first*)
```Sh
sudo apt install python3 python3-pip
```
Install the `pynput` library via Terminal
```Sh
sudo apt pip3 install pynput
```

### 🍎 macOS 
Install Python3
```Sh
brew install python
```
Install the `pynput` library via Terminal
```Sh
pip3 install pynput
```

## 🔧 Customizing
In `auto_clicker_script.py` file
* **TOGGLE_KEY** is the Hotkey to start/stop the auto-clicker *(Default is F6 key)*
* **STOP_KEY** is the Hotkey to exit the program *(Default is F7 key)*
* **CLICK_BUTTON** is the Mouse button to click *(Default is right click)*
* **CLICK_INTERVAL** is the Time in seconds between clicks *(Default is 3 seconds)*

## 🎯 Usage
1. Run the script on:  
   - Windows *(Command Prompt)* 
`python auto_clicker_script.py`  
   - Linux (Ubuntu/Debian) and macOS *(Terminal)*
`python3 auto_clicker_script.py`
2. Use the Hotkey to Start/Stop Clicking
3. Use the Hotkey to Exit the Auto Clicker Program

## 🙌 Credits
Developed by *Haruji23*. Inspired by the joy of playing Sky: Children of the Light and the beauty of streamlined automation.
