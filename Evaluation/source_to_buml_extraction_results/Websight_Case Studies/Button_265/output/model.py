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
BankPage = Class(name="BankPage")
Navigation = Class(name="Navigation")
MainContent = Class(name="MainContent")
Footer = Class(name="Footer")

# BankPage class attributes and methods
BankPage_title: Property = Property(name="title", type=StringType)
BankPage_description: Property = Property(name="description", type=StringType)
BankPage.attributes={BankPage_title, BankPage_description}

# Navigation class attributes and methods
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation_aboutLink: Property = Property(name="aboutLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation.attributes={Navigation_aboutLink, Navigation_homeLink, Navigation_contactLink}

# MainContent class attributes and methods
MainContent_welcomeMessage: Property = Property(name="welcomeMessage", type=StringType)
MainContent_accountInfo: Property = Property(name="accountInfo", type=StringType)
MainContent.attributes={MainContent_accountInfo, MainContent_welcomeMessage}

# Footer class attributes and methods
Footer_copyrightNotice: Property = Property(name="copyrightNotice", type=StringType)
Footer.attributes={Footer_copyrightNotice}

# Relationships
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="BankPage", type=BankPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="BankPage", type=BankPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
content: BinaryAssociation = BinaryAssociation(
    name="content",
    ends={
        Property(name="BankPage", type=BankPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={BankPage, Navigation, MainContent, Footer},
    associations={footer, nav, content},
    generalizations={}
)
