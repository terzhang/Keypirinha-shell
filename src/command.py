
import re
import subprocess
import keypirinha as kp

class Command(kp.Plugin):

    SECTION_MAIN = 'main'

    REGEX_INPUT = r'^(>{1,2})\s(.+)'

    ITEM_COMMAND = kp.ItemCategory.USER_BASE + 1

    def __init__(self):
        super().__init__()

    def on_start(self):
        self._load_settings()

        actions = []

        actions.append(self._set_action('keep_open', 'Keep Open', 'Run the command and keep shell open.'))
        actions.append(self._set_action('close_shell', 'Close shell', 'Close shell after running the command.'))

        self.set_actions(self.ITEM_COMMAND, actions)

    def on_catalog(self):
        self.on_start()

    def on_suggest(self, user_input, items_chain):
        input = re.search(self.REGEX_INPUT, user_input)

        if input is None:
            return None

        if len(input.groups()) != 2:
            pass
        else:
            operator = input.group(1)
            command = input.group(2)

        suggestion = [self._set_suggestion(operator + '@' + command)]

        self.set_suggestions(suggestion)

    def on_execute(self, item, action):
        if item.category() != self.ITEM_COMMAND:
            return
        
        prompt = 'wt'

        [operator, command] = self._split_target(item.target())


        if operator == '>>' or (action and action.name() == "close_shell"):
            # Runs a shell command and prompt for enter before exiting
            msg="read -p 'Press enter to exit...' x"
            shell = ['sh', '-c', command + ' && ' + msg]
            print(f'running one time command: {command}')
        elif operator == '>' or (action and action.name() == "keep_open"):
            # Runs a shell command in an existing windows terminal window (if possible)
            # then run a shell console after
            shell_list = [*command.split(' '), '&&', 'bash']
            shell = [prompt, '-w', '1', 'nt', '-p', 'Bash', 'sh', '-c', ' '.join(shell_list)]
            print(f'running command: {command}')

        try:
            subprocess.Popen(shell)
        except Exception as e:
            print('Exception: shell - (%s)' % (e))

    def on_activated(self):
        pass

    def on_deactivated(self):
        pass

    def on_events(self, flags):
        pass

    def _set_action(self, name, label, desc):
        return self.create_action(
            name = name,
            label = label,
            short_desc = desc
        )

    def _set_suggestion(self, target):
        [operator, command] = self._split_target(target)

        if operator == '>':
            close_msg = ''
        elif operator == '>>':
            close_msg = ' and close shell.'

        return self.create_item(
            category = self.ITEM_COMMAND,
            label = operator + ' ' + command,
            short_desc = 'Run \'' + command + '\' command' + close_msg,
            target = target,
            args_hint = kp.ItemArgsHint.FORBIDDEN,
            hit_hint = kp.ItemHitHint.IGNORE
        )

    def _load_settings(self):
        self.settings = self.load_settings()

    def _split_target(self, target):
        return target.split('@')
