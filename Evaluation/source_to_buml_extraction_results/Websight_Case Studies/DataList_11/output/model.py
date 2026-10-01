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
HeroSection = Class(name="HeroSection")
FinancialTable = Class(name="FinancialTable")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Navigation class attributes and methods

# HeroSection class attributes and methods

# FinancialTable class attributes and methods
FinancialTable_income: Property = Property(name="income", type=StringType)
FinancialTable_expenses: Property = Property(name="expenses", type=StringType)
FinancialTable.attributes={FinancialTable_expenses, FinancialTable_income}

# Footer class attributes and methods

# Relationships
navLink: BinaryAssociation = BinaryAssociation(
    name="navLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
heroContent: BinaryAssociation = BinaryAssociation(
    name="heroContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="HeroSection", type=HeroSection, multiplicity=Multiplicity(1, 1))
    }
)
financialData: BinaryAssociation = BinaryAssociation(
    name="financialData",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FinancialTable", type=FinancialTable, multiplicity=Multiplicity(1, 1))
    }
)
footerContent: BinaryAssociation = BinaryAssociation(
    name="footerContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Navigation, HeroSection, FinancialTable, Footer},
    associations={navLink, heroContent, financialData, footerContent},
    generalizations={}
)
