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
MusicWebsite = Class(name="MusicWebsite")
NavBar = Class(name="NavBar")
Section = Class(name="Section")
Footer = Class(name="Footer")

# MusicWebsite class attributes and methods

# NavBar class attributes and methods
NavBar_title: Property = Property(name="title", type=StringType)
NavBar_linksCount: Property = Property(name="linksCount", type=IntegerType)
NavBar.attributes={NavBar_linksCount, NavBar_title}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_title, Section_description}

# Footer class attributes and methods
Footer_socialMediaLinksCount: Property = Property(name="socialMediaLinksCount", type=IntegerType)
Footer_newsletterEmail: Property = Property(name="newsletterEmail", type=StringType)
Footer.attributes={Footer_newsletterEmail, Footer_socialMediaLinksCount}

# Relationships
navBar: BinaryAssociation = BinaryAssociation(
    name="navBar",
    ends={
        Property(name="MusicWebsite", type=MusicWebsite, multiplicity=Multiplicity(1, 1)),
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1))
    }
)
mainSection: BinaryAssociation = BinaryAssociation(
    name="mainSection",
    ends={
        Property(name="MusicWebsite", type=MusicWebsite, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
pageFooter: BinaryAssociation = BinaryAssociation(
    name="pageFooter",
    ends={
        Property(name="MusicWebsite", type=MusicWebsite, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={MusicWebsite, NavBar, Section, Footer},
    associations={navBar, mainSection, pageFooter},
    generalizations={}
)
