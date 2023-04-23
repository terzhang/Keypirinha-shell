# Keypirinha Plugin: Shell

This is Shell, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

This plugin provides an easy way to execute simple commands from Keypirinha.

## Install:

Download the `Shell.keypirinha-package` file is downloaded,
move it to the `InstalledPackage` folder located at:

- `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
- **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
final path would look like
`C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)

**NOTE:** You may have to manually restart Keypirinha to see the package activated.


## Configuration:

0. NO configuration is required.


## Usage:

Invoke Keypirinha and put the command to be executed in following format:
```sh
> command
-OR-
>> command

e.g.

> echo 'Hello World'
>> ping 'google.com'
```

| ![Command usage](./images/usage.png "Command usage") |
| :-: |
| *Command usage* |


### Difference between > and >>:

Running with `>>` will close the shell window after completion.

Running with `>`, will keep the shell window open after completion


### Actions

There are two actions available irrespective of the configuration.

| ![Command actions](./images/actions.png "Command actions") |
| :-: |
| *Command actions* |

- **Keep Open**: Do not close the prompt after running the command.
- **Close CMD**: Close the prompt after running the command.

## License

MIT

## Credits
This is a fork of [bantya](https://github.com/bantya)'s Keypirinha-Command
