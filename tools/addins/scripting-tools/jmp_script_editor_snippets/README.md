# JMP Script Editor Snippets
| [Description](#description) | [Usage](#usage) | [Execution](#execution) | [Possible future features](#possible-future-features) |

# WORK IN PROGRESS
See JMP Community for more up-to-date documentation
[JMP Community - JMP Script Editor Snippets](https://community.jmp.com/t5/JMP-Add-Ins/JMP-Script-Editor-Snippets/ta-p/583420)

## Description 
[JMP Community - JMP Script Editor Snippets](https://community.jmp.com/t5/JMP-Add-Ins/JMP-Script-Editor-Snippets/ta-p/583420)

While waiting for Add Snippets to Script Editor wish to be completed, I quickly wrote an add-in so I can have at least some sort of snippets while scripting in Script Editor. Add-in was put together fairly fast and it does still have bugs and issues (especially with focusing different elements in the UI). There might be changes to this add-in which will break the functionality of current snippets and/or their locations.

## Installation
Add-in has been built with Add-In Manager, requires at minimum JMP16 and does support Windows (might work on OSX, but I cannot test that and supported host has been set as Win in add-in manager).

Download the add-in from this page and install as you would normally install JMP Add-Ins (double click). The add-in will (by default) use shortcut keybind Ctrl+Shift+Space . When the add-in first time run it will create folder to users $DOCUMENTS called jmp_script_editor_snippets which user can use to store custom snippets (full path is something like C:\Users\<USERNAME>\Documents\jmp_script_editor_snippets\). The snippet files are basically just .jsl files which are found from the add-ins' snippet folder or from user's documents snippet folder.

## Usage
Write #snippet <optional search term> into your script editor. #snippet is used as a lookup value and if you include optional search terms, those will be used to pre-fill the search bar. After you have #snippet in your code, press Ctrl+Shift+Space to launch JMP Script Editor Snippet window, search for correct snippet and press OK (you can sometimes also just press Enter / use Tab to get to Enter). #snippet line will be replaced with the snippet you selected. Below is image of the snippet window

### GUI

### Options

## Execution

## Possible future features


