"""Classes for melon orders."""
class AbstractMelonOrder():
    """ An abstract base class that other Melon Orders inherit from. """

    def __init__(self, species, qty, country_code = None):
        """Initialize melon order attributes"""

        self.species = species.lower()
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        if "christmas" in self.species:
            base_price = 15
        else:    
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = 'domestic'
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    flat_fee = 3

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        if "christmas" in self.species:
            base_price = 15
        else:    
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10:
            total = total+ self.flat_fee


        return total

class GovermentMelonOrder(AbstractMelonOrder):
    tax = 0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self,passed):
        self.passed_inspection = passed

