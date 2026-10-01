####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
Menu = Class(name="Menu")
Categories = Class(name="Categories")
FilterOptions = Class(name="FilterOptions")
PopularDish = Class(name="PopularDish")

# Menu class attributes and methods
Menu_pizza: Property = Property(name="pizza", type=StringType)
Menu_burger: Property = Property(name="burger", type=StringType)
Menu_sushi: Property = Property(name="sushi", type=StringType)
Menu.attributes={Menu_pizza, Menu_burger, Menu_sushi}

# Categories class attributes and methods
Categories_vegetarian: Property = Property(name="vegetarian", type=StringType)
Categories_nonVegetarian: Property = Property(name="nonVegetarian", type=StringType)
Categories.attributes={Categories_vegetarian, Categories_nonVegetarian}

# FilterOptions class attributes and methods
FilterOptions_price: Property = Property(name="price", type=StringType)
FilterOptions_rating: Property = Property(name="rating", type=StringType)
FilterOptions.attributes={FilterOptions_rating, FilterOptions_price}

# PopularDish class attributes and methods
PopularDish_image: Property = Property(name="image", type=StringType)
PopularDish_description: Property = Property(name="description", type=StringType)
PopularDish.attributes={PopularDish_description, PopularDish_image}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="Categories", type=Categories, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="FilterOptions", type=FilterOptions, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="PopularDish", type=PopularDish, multiplicity=Multiplicity(1, 1)),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Menu, Categories, FilterOptions, PopularDish},
    associations={association1, association2, association3},
    generalizations={}
)
