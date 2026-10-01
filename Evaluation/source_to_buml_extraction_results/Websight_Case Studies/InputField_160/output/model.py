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
Header = Class(name="Header")
Main = Class(name="Main")
Aside = Class(name="Aside")
Footer = Class(name="Footer")

# Header class attributes and methods
Header_image: Property = Property(name="image", type=StringType)
Header_title: Property = Property(name="title", type=StringType)
Header_description: Property = Property(name="description", type=StringType)
Header.attributes={Header_title, Header_description, Header_image}

# Main class attributes and methods
Main_categories: Property = Property(name="categories", type=StringType)
Main.attributes={Main_categories}

# Aside class attributes and methods
Aside_filters: Property = Property(name="filters", type=StringType)
Aside_recommendations: Property = Property(name="recommendations", type=StringType)
Aside.attributes={Aside_filters, Aside_recommendations}

# Footer class attributes and methods
Footer_newsletterEmail: Property = Property(name="newsletterEmail", type=StringType)
Footer_contactInfo: Property = Property(name="contactInfo", type=StringType)
Footer_socialMedia: Property = Property(name="socialMedia", type=StringType)
Footer.attributes={Footer_socialMedia, Footer_newsletterEmail, Footer_contactInfo}

# Relationships
header_to_main: BinaryAssociation = BinaryAssociation(
    name="header_to_main",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
main_to_aside: BinaryAssociation = BinaryAssociation(
    name="main_to_aside",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
    }
)
main_to_footer: BinaryAssociation = BinaryAssociation(
    name="main_to_footer",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Header, Main, Aside, Footer},
    associations={header_to_main, main_to_aside, main_to_footer},
    generalizations={}
)
