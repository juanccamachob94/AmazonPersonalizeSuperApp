class ItemValidator:
    @classmethod
    def is_valid(cls, item):
        return bool(item.get_item_id() and item.get_site())
