def format_error_message(error: Exception) -> str:
    tb = error.__traceback__
    while tb and tb.tb_next:
        tb = tb.tb_next

    file_name = tb.tb_frame.f_code.co_filename if tb else "Unknown File"
    line_number = tb.tb_lineno if tb else "Unknown Line"
    error_type = type(error).__name__

    return (
        f"Error occurred in python script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"| Type: [{error_type}] "
        f"| Message: [{str(error)}]"
    )


class CustomException(Exception):
    def __init__(self, error: Exception):
        super().__init__(str(error))
        self.error_message = format_error_message(error)

    def __str__(self) -> str:
        return self.error_message
