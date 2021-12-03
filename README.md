# README
Exports Discord chat logs to a csv-file, then using that csv file for making name replacements.

This project is based on [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter).

Therefore it also requires a **.NET Runtime** which has to be installed manually. 
- [.NET Core v3.1 Runtime for **Windows x64**](https://dotnet.microsoft.com/download/dotnet-core/thank-you/runtime-desktop-3.1.0-windows-x64-installer)
- [.NET Core v3.1 Runtime for **Windows x86**](https://dotnet.microsoft.com/download/dotnet-core/thank-you/runtime-desktop-3.1.0-windows-x86-installer)
- [.NET Core v3.1 Runtime for **macOS x64**](https://dotnet.microsoft.com/download/dotnet-core/thank-you/runtime-3.1.0-macos-x64-installer)
- [.NET Core v3.1 Runtime for **Linux**](https://docs.microsoft.com/en-us/dotnet/core/install/linux) (find your distro)

## Installing the python requirements
`pip install -r requirements.txt`

## Getting required information
You need to get your `Discord Token` and a `Channel ID` to use this tool.
Rename `config.template.yaml` to `config.yaml` and insert the Discord Token and Channel ID.
This file is also responsible for the replacements pairs. 

### How to get the Discord Token
1. Open Discord
2. Press Ctrl+Shift+I (⌥⌘I on macOS) to open developer tools
3. Press Ctrl+Shift+M (⇧⌘M) to toggle device toolbar
4. Navigate to the Application tab
5. On the left, expand Local Storage and select https꞉//discord.com
6. Type token into the Filter box
7. If the token key does not appear, press Ctrl+R (⌘R) to reload
8. Copy the value of the token key
[Source](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token)

or this video
- https://www.youtube.com/watch?v=YEgFvgg7ZPI


### How to get the channel id
Receive the channel token in the browser version of discord.

![Channel ID](./img/channel_id.png)

## Run the App
`python3 app.py`