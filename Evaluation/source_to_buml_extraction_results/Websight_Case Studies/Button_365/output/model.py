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
Section = Class(name="Section")

# WebPage class attributes and methods

# Navigation class attributes and methods
Navigation_home: Property = Property(name="home", type=StringType)
Navigation_services: Property = Property(name="services", type=StringType)
Navigation_testimonials: Property = Property(name="testimonials", type=StringType)
Navigation_contact: Property = Property(name="contact", type=StringType)
Navigation.attributes={Navigation_testimonials, Navigation_contact, Navigation_services, Navigation_home}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_description, Section_title}

# Relationships
nav1: BinaryAssociation = BinaryAssociation(
    name="nav1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
sec1: BinaryAssociation = BinaryAssociation(
    name="sec1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Navigation, Section},
    associations={nav1, sec1},
    generalizations={}
)
