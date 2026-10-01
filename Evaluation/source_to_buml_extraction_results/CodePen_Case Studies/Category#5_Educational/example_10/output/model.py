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
StudentComplaintForm = Class(name="StudentComplaintForm")

# StudentComplaintForm class attributes and methods
StudentComplaintForm_fullName: Property = Property(name="fullName", type=StringType)
StudentComplaintForm_major: Property = Property(name="major", type=StringType)
StudentComplaintForm_graduationYear: Property = Property(name="graduationYear", type=StringType)
StudentComplaintForm_streetAddress: Property = Property(name="streetAddress", type=StringType)
StudentComplaintForm_streetAddressLine2: Property = Property(name="streetAddressLine2", type=StringType)
StudentComplaintForm_city: Property = Property(name="city", type=StringType)
StudentComplaintForm_region: Property = Property(name="region", type=StringType)
StudentComplaintForm_postalCode: Property = Property(name="postalCode", type=StringType)
StudentComplaintForm_country: Property = Property(name="country", type=StringType)
StudentComplaintForm_email: Property = Property(name="email", type=StringType)
StudentComplaintForm_phone: Property = Property(name="phone", type=StringType)
StudentComplaintForm_preferredContactMethod: Property = Property(name="preferredContactMethod", type=StringType)
StudentComplaintForm_eventDate: Property = Property(name="eventDate", type=DateType)
StudentComplaintForm_involvedPersons: Property = Property(name="involvedPersons", type=StringType)
StudentComplaintForm_complaintDetails: Property = Property(name="complaintDetails", type=StringType)
StudentComplaintForm_resolutionAttempts: Property = Property(name="resolutionAttempts", type=StringType)
StudentComplaintForm_unresolvedReason: Property = Property(name="unresolvedReason", type=StringType)
StudentComplaintForm_desiredResolution: Property = Property(name="desiredResolution", type=StringType)
StudentComplaintForm_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
StudentComplaintForm.attributes={StudentComplaintForm_major, StudentComplaintForm_country, StudentComplaintForm_email, StudentComplaintForm_phone, StudentComplaintForm_preferredContactMethod, StudentComplaintForm_eventDate, StudentComplaintForm_involvedPersons, StudentComplaintForm_complaintDetails, StudentComplaintForm_resolutionAttempts, StudentComplaintForm_unresolvedReason, StudentComplaintForm_desiredResolution, StudentComplaintForm_additionalInfo, StudentComplaintForm_streetAddressLine2, StudentComplaintForm_graduationYear, StudentComplaintForm_city, StudentComplaintForm_streetAddress, StudentComplaintForm_region, StudentComplaintForm_fullName, StudentComplaintForm_postalCode}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={StudentComplaintForm},
    associations={},
    generalizations={}
)
