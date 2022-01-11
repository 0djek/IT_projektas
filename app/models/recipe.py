class RecipeStep():
    def __init__(self, title: str, seo_title: str, desciption: str, order: int) -> None:
        self.title = title
        self.seo_title = seo_title
        self.description = desciption
        self.order = order


class RecipeIngredient():
    def __init__(self, seo_title: str, quantity: int) -> None:
        self.seo_title = seo_title
        self.quantity = quantity
