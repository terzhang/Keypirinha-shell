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

## Build

Here's how to build the plugin yourself:
1. Make you have the [Keypirinha SDK](https://github.com/Keypirinha/SDK) cloned to local
2. Go into the SDK directory, setup your environment running `cmd/kpenv.cmd` in Command Prompt or Powershell
    Now your local PATH is modified with path to Keypirinha's SDK
3. Change back to your package directory, and run `make.cmd`
4. A new build will be generated in the [build](./build) directory

## License

MIT

## Credits
This is a fork of [bantya](https://github.com/bantya)'s Keypirinha-Command
