class ExitSettings:
    EXIT_CODE_SUCCESS = 0

    def __init__(self, exit_code: int = EXIT_CODE_SUCCESS):
        self.exit_code = exit_code
