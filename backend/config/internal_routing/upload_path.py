class UploadToFolder:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def __call__(self, instance, filename):
        folder_name = str(getattr(instance, 'book_id', 'temp'))
        file_name = f"{folder_name}_{filename}"
        return f"{self.base_dir}/{folder_name}/{file_name}"
    def deconstruct(self):
        return (
            f"{self.__module__}.{self.__class__.__name__}",  # import path
            [self.base_dir],  # positional args
            {}  # keyword args
        )