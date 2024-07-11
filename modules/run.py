from commands.pull import Pull
from commands.push import Push

STR_TO_COMMAND = {
    'push': Push,
    'pull': Pull
}

def run_command(args):
    command = args.command.lower()

    command_class = STR_TO_COMMAND[command]
    command_class().execute(args)
