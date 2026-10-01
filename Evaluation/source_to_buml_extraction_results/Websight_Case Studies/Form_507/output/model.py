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
Section = Class(name="Section")
Article = Class(name="Article")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Header class attributes and methods
Header_logo: Property = Property(name="logo", type=StringType)
Header.attributes={Header_logo}

# Main class attributes and methods

# Section class attributes and methods

# Article class attributes and methods
Article_image: Property = Property(name="image", type=StringType)
Article_title: Property = Property(name="title", type=StringType)
Article_description: Property = Property(name="description", type=StringType)
Article.attributes={Article_description, Article_title, Article_image}

# Footer class attributes and methods
Footer_newsletterEmail: Property = Property(name="newsletterEmail", type=StringType)
Footer.attributes={Footer_newsletterEmail}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Article", type=Article, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Section, Article, Footer},
    associations={association1, association2, association3, association4, association5},
    generalizations={}
)
