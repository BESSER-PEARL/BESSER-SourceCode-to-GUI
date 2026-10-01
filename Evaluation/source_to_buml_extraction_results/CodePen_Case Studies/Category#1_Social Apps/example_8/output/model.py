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
RadioSection = Class(name="RadioSection")
RadioList = Class(name="RadioList")
RadioItem = Class(name="RadioItem")

# RadioSection class attributes and methods

# RadioList class attributes and methods

# RadioItem class attributes and methods

# Relationships
containsList: BinaryAssociation = BinaryAssociation(
    name="containsList",
    ends={
        Property(name="RadioSection", type=RadioSection, multiplicity=Multiplicity(1, 1)),
        Property(name="RadioList", type=RadioList, multiplicity=Multiplicity(1, 1))
    }
)
containsItems: BinaryAssociation = BinaryAssociation(
    name="containsItems",
    ends={
        Property(name="RadioList", type=RadioList, multiplicity=Multiplicity(1, 1)),
        Property(name="RadioItem", type=RadioItem, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RadioSection, RadioList, RadioItem},
    associations={containsList, containsItems},
    generalizations={}
)
