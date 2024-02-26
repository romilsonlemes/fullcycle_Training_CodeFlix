import uuid

class Category:
    def __init__(
        self,
        name,
        id = "",
        description = "",
        is_active = True,
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active
        
        self.validate()
        
    # Validações dos campos
    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer than 255 characters")
        
        if not self.name:   # len(self.name) == 0
            raise ValueError("name cannot be empty")
        
    def __str__(self) -> str:
        return f"{self.name}    - {self.description}    ({self.is_active})"
    
    def __repr__(self) -> str:
        return f"<Category {self.name} ({self.id})>"
    
    def update_category(self, name, description):
        self.name = name
        self.description = description
        
        self.validate()
      
    