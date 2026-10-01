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
Application = Class(name="Application")
Person = Class(name="Person")
Input = Class(name="Input")
EditInput = Class(name="EditInput")

# Application class attributes and methods
Application_bin: Property = Property(name="bin", type=StringType)
Application_input: Property = Property(name="input", type=StringType)
Application_editInput: Property = Property(name="editInput", type=StringType)
Application_columns: Property = Property(name="columns", type=StringType)
Application_persons: Property = Property(name="persons", type=StringType)
Application.attributes={Application_bin, Application_persons, Application_input, Application_editInput, Application_columns}

# Person class attributes and methods
Person_lname: Property = Property(name="lname", type=StringType)
Person_fname: Property = Property(name="fname", type=StringType)
Person_age: Property = Property(name="age", type=IntegerType)
Person_job: Property = Property(name="job", type=StringType)
Person_address: Property = Property(name="address", type=StringType)
Person.attributes={Person_age, Person_lname, Person_job, Person_fname, Person_address}

# Input class attributes and methods
Input_lname: Property = Property(name="lname", type=StringType)
Input_fname: Property = Property(name="fname", type=StringType)
Input_age: Property = Property(name="age", type=IntegerType)
Input_job: Property = Property(name="job", type=StringType)
Input_address: Property = Property(name="address", type=StringType)
Input.attributes={Input_fname, Input_age, Input_job, Input_address, Input_lname}

# EditInput class attributes and methods
EditInput_lname: Property = Property(name="lname", type=StringType)
EditInput_fname: Property = Property(name="fname", type=StringType)
EditInput_age: Property = Property(name="age", type=IntegerType)
EditInput_job: Property = Property(name="job", type=StringType)
EditInput_address: Property = Property(name="address", type=StringType)
EditInput.attributes={EditInput_lname, EditInput_address, EditInput_fname, EditInput_age, EditInput_job}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Application", type=Application, multiplicity=Multiplicity(1, 1)),
        Property(name="Person", type=Person, multiplicity=Multiplicity(0, 9999))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Application", type=Application, multiplicity=Multiplicity(1, 1)),
        Property(name="Input", type=Input, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Application", type=Application, multiplicity=Multiplicity(1, 1)),
        Property(name="EditInput", type=EditInput, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Application, Person, Input, EditInput},
    associations={association1, association2, association3},
    generalizations={}
)
