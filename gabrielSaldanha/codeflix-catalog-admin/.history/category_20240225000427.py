class Category:
    def __init__(
        self,
        id = "",
        name = "",
        description = "",
        is_active = True,
    ):
        self.id = id or uuid = uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active
