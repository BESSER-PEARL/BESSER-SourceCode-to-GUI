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
PatientForm = Class(name="PatientForm")

# PatientForm class attributes and methods
PatientForm_age: Property = Property(name="age", type=IntegerType)
PatientForm_diabetesType: Property = Property(name="diabetesType", type=StringType)
PatientForm_treatmentType: Property = Property(name="treatmentType", type=StringType)
PatientForm_averageFastGlucose: Property = Property(name="averageFastGlucose", type=IntegerType)
PatientForm_hba1c: Property = Property(name="hba1c", type=StringType)
PatientForm.attributes={PatientForm_age, PatientForm_hba1c, PatientForm_averageFastGlucose, PatientForm_diabetesType, PatientForm_treatmentType}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={PatientForm},
    associations={},
    generalizations={}
)
