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
Destination = Class(name="Destination")
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Section = Class(name="Section")

# Destination class attributes and methods
Destination_name: Property = Property(name="name", type=StringType)
Destination_image: Property = Property(name="image", type=StringType)
Destination.attributes={Destination_name, Destination_image}

# WebPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_subtitle, Header_title}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section.attributes={Section_title}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Destination", type=Destination, multiplicity=Multiplicity(3, 3))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Destination, WebPage, Header, Section},
    associations={association1, association2, association3},
    generalizations={}
)
