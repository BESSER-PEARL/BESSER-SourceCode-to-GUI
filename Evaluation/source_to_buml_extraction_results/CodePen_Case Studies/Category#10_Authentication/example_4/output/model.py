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
AccountAuthentication = Class(name="AccountAuthentication")
TopNav = Class(name="TopNav")
Dropdown = Class(name="Dropdown")
PageContainer = Class(name="PageContainer")
Section = Class(name="Section")

# AccountAuthentication class attributes and methods
AccountAuthentication_success_url: Property = Property(name="success_url", type=StringType)
AccountAuthentication_error_url: Property = Property(name="error_url", type=StringType)
AccountAuthentication_authenticity_token: Property = Property(name="authenticity_token", type=StringType)
AccountAuthentication_subject: Property = Property(name="subject", type=StringType)
AccountAuthentication_text: Property = Property(name="text", type=StringType)
AccountAuthentication_access_token: Property = Property(name="access_token", type=StringType)
AccountAuthentication.attributes={AccountAuthentication_error_url, AccountAuthentication_text, AccountAuthentication_success_url, AccountAuthentication_access_token, AccountAuthentication_subject, AccountAuthentication_authenticity_token}

# TopNav class attributes and methods
TopNav_title: Property = Property(name="title", type=StringType)
TopNav.attributes={TopNav_title}

# Dropdown class attributes and methods
Dropdown_language: Property = Property(name="language", type=StringType)
Dropdown.attributes={Dropdown_language}

# PageContainer class attributes and methods

# Section class attributes and methods

# Relationships
auth_nav: BinaryAssociation = BinaryAssociation(
    name="auth_nav",
    ends={
        Property(name="AccountAuthentication", type=AccountAuthentication, multiplicity=Multiplicity(1, 1)),
        Property(name="TopNav", type=TopNav, multiplicity=Multiplicity(1, 1))
    }
)
nav_dropdown: BinaryAssociation = BinaryAssociation(
    name="nav_dropdown",
    ends={
        Property(name="TopNav", type=TopNav, multiplicity=Multiplicity(1, 1)),
        Property(name="Dropdown", type=Dropdown, multiplicity=Multiplicity(1, 1))
    }
)
container_section: BinaryAssociation = BinaryAssociation(
    name="container_section",
    ends={
        Property(name="PageContainer", type=PageContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AccountAuthentication, TopNav, Dropdown, PageContainer, Section},
    associations={auth_nav, nav_dropdown, container_section},
    generalizations={}
)
