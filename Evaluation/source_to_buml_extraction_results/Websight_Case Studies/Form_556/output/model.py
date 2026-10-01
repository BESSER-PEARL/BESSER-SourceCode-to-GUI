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
LoginForm = Class(name="LoginForm")
FinancialSection = Class(name="FinancialSection")

# WebPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_subtitle, Header_title}

# LoginForm class attributes and methods
LoginForm_username: Property = Property(name="username", type=StringType)
LoginForm_password: Property = Property(name="password", type=StringType)
LoginForm.attributes={LoginForm_username, LoginForm_password}

# FinancialSection class attributes and methods
FinancialSection_title: Property = Property(name="title", type=StringType)
FinancialSection_description: Property = Property(name="description", type=StringType)
FinancialSection.attributes={FinancialSection_title, FinancialSection_description}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
loginForm: BinaryAssociation = BinaryAssociation(
    name="loginForm",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LoginForm", type=LoginForm, multiplicity=Multiplicity(1, 1))
    }
)
financialSection: BinaryAssociation = BinaryAssociation(
    name="financialSection",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FinancialSection", type=FinancialSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, LoginForm, FinancialSection},
    associations={header, loginForm, financialSection},
    generalizations={}
)
