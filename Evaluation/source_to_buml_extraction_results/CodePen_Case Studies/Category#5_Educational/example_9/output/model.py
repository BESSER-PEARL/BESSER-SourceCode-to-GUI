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
Logo = Class(name="Logo")
Menu = Class(name="Menu")
MainContent = Class(name="MainContent")
FormText = Class(name="FormText")
Form = Class(name="Form")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Header class attributes and methods

# Logo class attributes and methods

# Menu class attributes and methods

# MainContent class attributes and methods

# FormText class attributes and methods

# Form class attributes and methods
Form_examination: Property = Property(name="examination", type=StringType)
Form_year: Property = Property(name="year", type=IntegerType)
Form_board: Property = Property(name="board", type=StringType)
Form_rollNo: Property = Property(name="rollNo", type=IntegerType)
Form_regNo: Property = Property(name="regNo", type=IntegerType)
Form.attributes={Form_examination, Form_year, Form_board, Form_rollNo, Form_regNo}

# Footer class attributes and methods

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
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
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
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Logo", type=Logo, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormText", type=FormText, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Logo, Menu, MainContent, FormText, Form, Footer},
    associations={association1, association2, association3, association4, association5, association6, association7},
    generalizations={}
)
