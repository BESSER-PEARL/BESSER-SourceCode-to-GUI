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
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")
Dish = Class(name="Dish")
SocialMediaLink = Class(name="SocialMediaLink")

# WebPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# Dish class attributes and methods
Dish_name: Property = Property(name="name", type=StringType)
Dish_description: Property = Property(name="description", type=StringType)
Dish.attributes={Dish_name, Dish_description}

# SocialMediaLink class attributes and methods
SocialMediaLink_platform: Property = Property(name="platform", type=StringType)
SocialMediaLink_url: Property = Property(name="url", type=StringType)
SocialMediaLink.attributes={SocialMediaLink_platform, SocialMediaLink_url}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
dishes: BinaryAssociation = BinaryAssociation(
    name="dishes",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Dish", type=Dish, multiplicity=Multiplicity(0, 9999))
    }
)
socialLinks: BinaryAssociation = BinaryAssociation(
    name="socialLinks",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SocialMediaLink", type=SocialMediaLink, multiplicity=Multiplicity(0, 9999))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer, Dish, SocialMediaLink},
    associations={header, dishes, socialLinks, main, footer},
    generalizations={}
)
