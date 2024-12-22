class DataTable:
    def __init__(self, start: int = 0, length: int = 10, **kwargs):
        self.start = start
        self.length = length
        self.MAX_LENGTH = 100
        self.kwargs = kwargs
    

    def validate_params(self) -> list[str]:
        errors = []

        if not self.validate_limit():
            errors.append("Limit is invalid")

        return errors


    def validate_limit(self) -> bool:
        return (
            isinstance(self.start, int) and isinstance(self.length, int)
            and self.length < self.MAX_LENGTH
            and self.start >= 0
        )
    

    def validate_order_by_col(self, valid_order_by_cols: list[str]) -> bool:
        pass


    def validate_order_direction(self) -> bool:
        pass
