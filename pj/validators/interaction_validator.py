class InteractionValidator:

    @classmethod
    def is_valid(cls, interaction):
        return interaction.get_user_id() and interaction.get_item_id() and \
            interaction.get_event_type()
