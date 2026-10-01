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
HeroImage = Class(name="HeroImage")
Section = Class(name="Section")
NavigationLink = Class(name="NavigationLink")

# WebPage class attributes and methods

# HeroImage class attributes and methods

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_content: Property = Property(name="content", type=StringType)
Section.attributes={Section_content, Section_title}

# NavigationLink class attributes and methods
NavigationLink_href: Property = Property(name="href", type=StringType)
NavigationLink_text: Property = Property(name="text", type=StringType)
NavigationLink.attributes={NavigationLink_href, NavigationLink_text}

# Relationships
heroImage: BinaryAssociation = BinaryAssociation(
    name="heroImage",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="HeroImage", type=HeroImage, multiplicity=Multiplicity(1, 1))
    }
)
navigationLinks: BinaryAssociation = BinaryAssociation(
    name="navigationLinks",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="NavigationLink", type=NavigationLink, multiplicity=Multiplicity(3, 3))
    }
)
sections: BinaryAssociation = BinaryAssociation(
    name="sections",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, HeroImage, Section, NavigationLink},
    associations={heroImage, navigationLinks, sections},
    generalizations={}
)
