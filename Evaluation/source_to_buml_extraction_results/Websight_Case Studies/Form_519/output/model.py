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
TravelAgencyPage = Class(name="TravelAgencyPage")
Parallax = Class(name="Parallax")
Section = Class(name="Section")
Form = Class(name="Form")
InputField = Class(name="InputField")

# TravelAgencyPage class attributes and methods

# Parallax class attributes and methods
Parallax_backgroundImage: Property = Property(name="backgroundImage", type=StringType)
Parallax.attributes={Parallax_backgroundImage}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_content: Property = Property(name="content", type=StringType)
Section.attributes={Section_content, Section_title}

# Form class attributes and methods

# InputField class attributes and methods
InputField_label: Property = Property(name="label", type=StringType)
InputField_inputType: Property = Property(name="inputType", type=StringType)
InputField_placeholder: Property = Property(name="placeholder", type=StringType)
InputField.attributes={InputField_label, InputField_placeholder, InputField_inputType}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Parallax", type=Parallax, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(0, 9999))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1)),
        Property(name="InputField", type=InputField, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgencyPage, Parallax, Section, Form, InputField},
    associations={association1, association2, association3, association4},
    generalizations={}
)
