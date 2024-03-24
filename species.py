class Species:
    def __init__(self, species):

        def filter_format(species):
            return species

        self.species = filter_format(species)

    def get_log(self):
        return self.species