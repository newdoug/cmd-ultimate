
# Features to Complete before 1.0

- Basic readline CLI capability
- Basic curses CLI capability
- Seemlessly switch between the readline and curses modes
- Ability to add new CLI modes (apart from readline and curses)
  - Users can create new modes, register them with application
  - Pluggable new modes (automatically registered) capability
- Ability to easily add new commands by library users
  - Each command can be readline-only, curses-only, only enabled by a subset of modes, etc.
  - Default supported by all modes
- Categories for each command
  - Built-in commands are in their own category, overridable by library users
  - Each individual command's category can be overridden, not just all built-ins at once So, basically hinting at some call like `app.update_category("cmd name", "some category")`
- Subcommand ability
  - multiple layers of subcommands
  - seemless integration with argparse library
  - also integrates with click? docopt? I just hate dealing with argparse actions and stuff sometimes... Maybe worth making own parsing library (doubt it)?
- Tab completion capabilities
  - Want built-in support for:
    - Case-sensitive static lists (ordered)
    - Case-insensitive static lists (ordered)
    - Case-sensitive dynamic lists (ordering by default is alphanumeric)
    - Case-insensitive dynamic lists (ordering by default is alphanumeric)
    - Ordering of completion items is configurable via lambda/function, have a few builtin ordering types (enum)
    - Default tab-completions
      - Paths
      - File paths
      - Directory paths
      - These completers should have an option for match a regex OR glob pattern
- Ability to add key bindings to the curses mode of the application to execute certain commands, run shell scripts/commands, etc.
- Support scripting commands
- Support aliases (saveable across reloads)
- Support loading new commands and subcommands at runtime, not just application start time
- Support for submenus and subcommands in submenus, etc.
  - Including nested submenus
  - Conditional submenu entrances
    - Based on cmdline args used for the command used to enter the menu
    - Based on current menu
    - Based on user
  - Changing of current prompt based on submenu
  - Lots of hooks pre/post load, entering, etc.
  - Support for (conditionally) loading commands based on menu, cmdline args, etc.
- Support conditional loading of new commands
  - Based on current menu
  - Based on cmdline arguments entered
  - Based on user
  - For both start time and runtime command loading
- Ability to disable built-in commands
- Built-in history
  - auto-saves to file (path is configurable)
  - has configurable formats (all human readable)
    - E.g. \n \t \c == `<num> <datetime> <command>`
    - Other escape sequences with meanings:
      - \n - command number executed
      - \m - menu/submenu user was in
      - \p - prompt when entered in
      - ?? etc.
    - Have DT format configurable
    - Ability to re-run commands by index
    - Ability to re-run commands by shortcuts
      - !!
- Built-in commands
  - shell - run shell commands (using SHELL environment variable, default to /usr/bin/env bash if not present, etc.)
    - Default shell configurable
  - alias - manage aliases.
  - history - manage history
  - jobs - manage background jobs
  - exitsh - exits submenu
  - quit - quit application
  - help - lists available commands, what menu the user is in, categories, etc. Takes optional positional arguments of commands to display their help text
  - configure - change CLI configuration settings
    - extendable for re-use by applications

- Built-in configuration file format support?
- Built-in logging ability
  - Log to syslog
   - OutputDebugStringA on windows?
   - Windows events?
  - Log to file(s)
  - Log levels setting
  - Enable and disable/configurable at runtime and load time
  - Changing of log format as well
  - Disabled by default, enablable easily though
  - Configurable from CLI config file if that idea is followed through with
- Library comes with test module to help unit test things
- Ability to save all stdout and stderr to a file
  - Default off
  - Configurable stdout and stderr to different or same files
- Ability to pipe command output to shell commands
- Ability to redirect command output to files
- Ability to save all stdin to a file 
  - Includes commented commands, piped commands, etc.
- Ability to background commands with an &
  - jobs command will list background commands still running
  - What to do with output? Should probably provide a shell-y way to suppress output until foregrounding it later. When foregrounding, should optionally display all missed output
- Support command chaining
  - cmd1 && cmd2
  - cmd1 || cmd2
  - cmd1; cmd2
- Built-in colored output capability
  - Should check if output is a tty, supports color, etc. and not use color ever if not supported
- Have concept of exit codes per command and viewing them in shell (something like echo "$?")
  - Should help with command chaining
- Built-in table support
  - Styles
  - Configurable spacing settings globally and per-style
  - Configurable default table style setting at runtime
  - Supported in readline and curses modes
    - In curses modes, users should be able to set actions to perform when selecting and hitting enter on elements in tables
      - Possibly enter into a new view, e.g. with more details on selected item or something
- Care about multi-platform (windows, osx) support?
- multi-line command support
- quoted inputs support
- optional support for environment variable expansion in input strings
  - not fancy expansions like bsah and other shells do (e.g. splicing)
- Multi-CLI support in some way?
- Support piping from command to command
  - e.g. cmd1 | cmd2
  - means probably have to distinguish between shell and cmd2 commands here like
    - cmd1 | cmd2 for our cli commands
    - cmd1 | !cmd for piping to shell commands
    - Meaning the command has to have some sort of argument or flag that says it supports being piped input? If using argparse, how will that look like as a stream of data?
- Have mixed support for curses-like stuff in readline mode
  - e.g. asynchronous notifications on:
    - top of screen
    - bottom of screen
      - below prompt
      - above prompt
    - all non-interrupting of input
    - green (success), red (failure), yellow (warning)
    - configurable colors and ANSI styling

- Easy ability to have base commands in subcommands turn into submenus
- Configurable signal handlers
  - Linux/UNIX signals
  - Windows??
