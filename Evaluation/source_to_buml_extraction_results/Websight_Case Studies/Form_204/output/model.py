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
ServiceAppointmentForm = Class(name="ServiceAppointmentForm")

# WebPage class attributes and methods
WebPage_headerImage: Property = Property(name="headerImage", type=StringType)
WebPage_navLinks: Property = Property(name="navLinks", type=StringType)
WebPage_featuredVehiclesTitle: Property = Property(name="featuredVehiclesTitle", type=StringType)
WebPage_featuredVehiclesDescription: Property = Property(name="featuredVehiclesDescription", type=StringType)
WebPage_vehicleSpecificationsTitle: Property = Property(name="vehicleSpecificationsTitle", type=StringType)
WebPage_vehicleSpecificationsDescription: Property = Property(name="vehicleSpecificationsDescription", type=StringType)
WebPage_financingInformationTitle: Property = Property(name="financingInformationTitle", type=StringType)
WebPage_financingInformationDescription: Property = Property(name="financingInformationDescription", type=StringType)
WebPage_contactInformationTitle: Property = Property(name="contactInformationTitle", type=StringType)
WebPage_contactInformation: Property = Property(name="contactInformation", type=StringType)
WebPage_serviceAppointmentTitle: Property = Property(name="serviceAppointmentTitle", type=StringType)
WebPage.attributes={WebPage_headerImage, WebPage_vehicleSpecificationsTitle, WebPage_navLinks, WebPage_featuredVehiclesDescription, WebPage_financingInformationDescription, WebPage_contactInformationTitle, WebPage_featuredVehiclesTitle, WebPage_vehicleSpecificationsDescription, WebPage_serviceAppointmentTitle, WebPage_financingInformationTitle, WebPage_contactInformation}

# ServiceAppointmentForm class attributes and methods
ServiceAppointmentForm_name: Property = Property(name="name", type=StringType)
ServiceAppointmentForm_email: Property = Property(name="email", type=StringType)
ServiceAppointmentForm_phone: Property = Property(name="phone", type=StringType)
ServiceAppointmentForm_message: Property = Property(name="message", type=StringType)
ServiceAppointmentForm.attributes={ServiceAppointmentForm_message, ServiceAppointmentForm_name, ServiceAppointmentForm_email, ServiceAppointmentForm_phone}

# Relationships
form: BinaryAssociation = BinaryAssociation(
    name="form",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ServiceAppointmentForm", type=ServiceAppointmentForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, ServiceAppointmentForm},
    associations={form},
    generalizations={}
)
