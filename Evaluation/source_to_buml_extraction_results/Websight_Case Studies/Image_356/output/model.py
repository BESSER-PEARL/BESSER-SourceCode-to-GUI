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
Navigation = Class(name="Navigation")

# WebPage class attributes and methods
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_footer: Property = Property(name="footer", type=StringType)
WebPage.attributes={WebPage_description, WebPage_logo, WebPage_footer, WebPage_title}

# Navigation class attributes and methods
Navigation_home: Property = Property(name="home", type=StringType)
Navigation_about: Property = Property(name="about", type=StringType)
Navigation_products: Property = Property(name="products", type=StringType)
Navigation_contact: Property = Property(name="contact", type=StringType)
Navigation.attributes={Navigation_home, Navigation_products, Navigation_contact, Navigation_about}

# Relationships
navLink: BinaryAssociation = BinaryAssociation(
    name="navLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Navigation},
    associations={navLink},
    generalizations={}
)
