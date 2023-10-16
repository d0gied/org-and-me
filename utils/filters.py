from aiogram.types import Message, CallbackQuery


class CallbackData:
    def __init__(self, *commands) -> None:
        self.commands = []
        for command in commands:
            if isinstance(command, str):
                self.commands.append(command)
            elif isinstance(command, list):
                self.commands.extend(command)
            else:  # pragma: no cover
                raise TypeError(
                    "CallbackData() argument must be a string or a list of strings."
                )

    def __call__(self, query: CallbackQuery):
        return query.data in self.commands
