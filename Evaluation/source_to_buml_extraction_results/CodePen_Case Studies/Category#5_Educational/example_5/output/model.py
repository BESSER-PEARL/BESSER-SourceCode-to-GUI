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
SurveyForm = Class(name="SurveyForm")

# SurveyForm class attributes and methods
SurveyForm_role: Property = Property(name="role", type=StringType)
SurveyForm_recommend: Property = Property(name="recommend", type=StringType)
SurveyForm_service: Property = Property(name="service", type=StringType)
SurveyForm_improvements: Property = Property(name="improvements", type=StringType)
SurveyForm_comments: Property = Property(name="comments", type=StringType)
SurveyForm_name: Property = Property(name="name", type=StringType)
SurveyForm_email: Property = Property(name="email", type=StringType)
SurveyForm_age: Property = Property(name="age", type=IntegerType)
SurveyForm.attributes={SurveyForm_role, SurveyForm_email, SurveyForm_recommend, SurveyForm_service, SurveyForm_age, SurveyForm_improvements, SurveyForm_name, SurveyForm_comments}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SurveyForm},
    associations={},
    generalizations={}
)
