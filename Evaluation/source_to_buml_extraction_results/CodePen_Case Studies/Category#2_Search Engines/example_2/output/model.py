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
Main = Class(name="Main")
HomePage = Class(name="HomePage")
ResultPage = Class(name="ResultPage")
Container = Class(name="Container")
Row = Class(name="Row")
Column = Class(name="Column")
Form = Class(name="Form")
Input = Class(name="Input")
Footer = Class(name="Footer")
Section = Class(name="Section")
DisplayResults = Class(name="DisplayResults")

# Main class attributes and methods

# HomePage class attributes and methods

# ResultPage class attributes and methods

# Container class attributes and methods

# Row class attributes and methods

# Column class attributes and methods

# Form class attributes and methods

# Input class attributes and methods
Input_placeholder: Property = Property(name="placeholder", type=StringType)
Input_id: Property = Property(name="id", type=StringType)
Input_type: Property = Property(name="type", type=StringType)
Input.attributes={Input_placeholder, Input_id, Input_type}

# Footer class attributes and methods

# Section class attributes and methods

# DisplayResults class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="HomePage", type=HomePage, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ResultPage", type=ResultPage, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="HomePage", type=HomePage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="ResultPage", type=ResultPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Row", type=Row, multiplicity=Multiplicity(3, 3))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Row", type=Row, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Column", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="Column", type=Column, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="Column", type=Column, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="Column", type=Column, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Input", type=Input, multiplicity=Multiplicity(1, 1))
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="DisplayResults", type=DisplayResults, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Main, HomePage, ResultPage, Container, Row, Column, Form, Input, Footer, Section, DisplayResults},
    associations={association1, association2, association3, association4, association5, association6, association7, association8, association9, association10, association11},
    generalizations={}
)
