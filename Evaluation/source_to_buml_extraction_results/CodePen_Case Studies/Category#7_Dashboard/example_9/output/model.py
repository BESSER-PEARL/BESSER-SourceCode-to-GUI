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
Container = Class(name="Container")
Menu = Class(name="Menu")
MenuItem = Class(name="MenuItem")
SearchInput = Class(name="SearchInput")
Grid = Class(name="Grid")
Column = Class(name="Column")
Form = Class(name="Form")
TextField = Class(name="TextField")
TextArea = Class(name="TextArea")

# WebPage class attributes and methods

# Container class attributes and methods

# Menu class attributes and methods

# MenuItem class attributes and methods

# SearchInput class attributes and methods
SearchInput_placeholder: Property = Property(name="placeholder", type=StringType)
SearchInput.attributes={SearchInput_placeholder}

# Grid class attributes and methods

# Column class attributes and methods

# Form class attributes and methods

# TextField class attributes and methods
TextField_name: Property = Property(name="name", type=StringType)
TextField_placeholder: Property = Property(name="placeholder", type=StringType)
TextField.attributes={TextField_name, TextField_placeholder}

# TextArea class attributes and methods
TextArea_placeholder: Property = Property(name="placeholder", type=StringType)
TextArea.attributes={TextArea_placeholder}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TextArea", type=TextArea, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MenuItem", type=MenuItem, multiplicity=Multiplicity(0, 9999))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SearchInput", type=SearchInput, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Grid", type=Grid, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Grid", type=Grid, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Column", type=Column, multiplicity=Multiplicity(0, 9999))
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
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TextField", type=TextField, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Container, Menu, MenuItem, SearchInput, Grid, Column, Form, TextField, TextArea},
    associations={association1, association9, association2, association3, association4, association5, association6, association7, association8},
    generalizations={}
)
