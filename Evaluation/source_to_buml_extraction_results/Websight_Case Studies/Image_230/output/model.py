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
Section = Class(name="Section")
Footer = Class(name="Footer")
TeamSection = Class(name="TeamSection")
ServicesSection = Class(name="ServicesSection")
ReviewsSection = Class(name="ReviewsSection")
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Navigation = Class(name="Navigation")

# Section class attributes and methods

# Footer class attributes and methods

# TeamSection class attributes and methods

# ServicesSection class attributes and methods

# ReviewsSection class attributes and methods

# WebPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TeamSection", type=TeamSection, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ServicesSection", type=ServicesSection, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ReviewsSection", type=ReviewsSection, multiplicity=Multiplicity(1, 1))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Section, Footer, TeamSection, ServicesSection, ReviewsSection, WebPage, Header, Navigation},
    associations={association2, association3, association4, association5, association6, association7, association1},
    generalizations={}
)
