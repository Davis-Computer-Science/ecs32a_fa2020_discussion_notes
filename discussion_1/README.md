# Terms

- [`terminal`](https://en.wikipedia.org/wiki/Data_terminal_equipment): Refers to interfaces to interact with your system. Almost the same as `shell` now.
- `shell`: Command-line user interface(CLI) and graphical user interface(GUI).
  - `sh`
  - [`bash`](https://en.wikipedia.org/wiki/Bash_(Unix_shell)): Command language that almost everyone(Most Linux distribution, Mac OS before Catalina, Windows Subsystem for Linux) uses.
  - `zsh`: Default on Mac OS X Catalina([How to change default to bash](https://www.howtogeek.com/444596/how-to-change-the-default-shell-to-bash-in-macos-catalina/))
  - ......
- `IDE`: Puts everything(Coding, text editing, documentation, version control, terminal, extensions, etc.) together
  - VS Code
  - PyCharm
  - ......
- `Markdown`: A lightweight texting format that renders nice looking html pages :)

# VC Code usage

- **Left panel**: Navigate through files, versions, debugging, extensions.
- **Main screen**: Text editing, previewing
- **Terminal**

# Commands

`<command> [args*]`

## Directories
- `pwd`: Print the name of the current working directory.
- `ls`: List information about the FILEs (the current directory by default).
  - Relative path: relative to current directory.
    - `.` is the current directory, `..` is the parent directory.
  - Absolute path: starts with `/`
- `cd`: Change directory.
- `mkdir`: Make directory.

## Files
- `cp`: Copy
- `mv`: Move
- `cat`: Concatenate FILE(s) to standard output.
- `touch`
- `diff`

## Others
- `echo`: Print something.
- `git`: Version control.
- `python3` / `python`

# HW Submission

# Quick tips

- `.` is the current directory, `..` is the parent directory.
- Use `Tab` to auto-fill your command.
- `Ctrl + C` terminates current command, `Ctrl + Shift + C/V` is copy/paste.
- `Ctrl + R` to search past commands.
- Set up vars: `<VAR>=SOMETHING`, use vars: `$<VAR>`

# Conclusion

- Terminal(shell) is a command-line interface with your system, most of you use `bash`.
- VS Code is an IDE, not terminal. We demostrated certain usage of VS Code
- Serval commands: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, etc...