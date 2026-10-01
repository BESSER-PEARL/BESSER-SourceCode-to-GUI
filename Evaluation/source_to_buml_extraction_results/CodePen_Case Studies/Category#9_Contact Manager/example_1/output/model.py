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
ContactPage = Class(name="ContactPage")
SuccessMessage = Class(name="SuccessMessage")

# ContactPage class attributes and methods
ContactPage_email: Property = Property(name="email", type=StringType)
ContactPage_subject: Property = Property(name="subject", type=StringType)
ContactPage_message: Property = Property(name="message", type=StringType)
ContactPage_submission_time: Property = Property(name="submission_time", type=DateTimeType)
ContactPage_name: Property = Property(name="name", type=StringType)
ContactPage.attributes={ContactPage_email, ContactPage_subject, ContactPage_name, ContactPage_message, ContactPage_submission_time}

# SuccessMessage class attributes and methods
SuccessMessage_message_text: Property = Property(name="message_text", type=StringType)
SuccessMessage_display_time: Property = Property(name="display_time", type=DateTimeType)
SuccessMessage.attributes={SuccessMessage_display_time, SuccessMessage_message_text}

# Relationships
form_submission: BinaryAssociation = BinaryAssociation(
    name="form_submission",
    ends={
        Property(name="ContactPage", type=ContactPage, multiplicity=Multiplicity(1, 1)),
        Property(name="SuccessMessage", type=SuccessMessage, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactPage, SuccessMessage},
    associations={form_submission},
    generalizations={}
)
