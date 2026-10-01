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
NavBar = Class(name="NavBar")
MenuLink = Class(name="MenuLink")
ReservationForm = Class(name="ReservationForm")
Footer = Class(name="Footer")
HoursOfOperation = Class(name="HoursOfOperation")
ContactInformation = Class(name="ContactInformation")

# WebPage class attributes and methods

# NavBar class attributes and methods

# MenuLink class attributes and methods
MenuLink_href: Property = Property(name="href", type=StringType)
MenuLink.attributes={MenuLink_href}

# ReservationForm class attributes and methods
ReservationForm_name: Property = Property(name="name", type=StringType)
ReservationForm_email: Property = Property(name="email", type=StringType)
ReservationForm.attributes={ReservationForm_name, ReservationForm_email}

# Footer class attributes and methods

# HoursOfOperation class attributes and methods
HoursOfOperation_weekdayHours: Property = Property(name="weekdayHours", type=StringType)
HoursOfOperation_weekendHours: Property = Property(name="weekendHours", type=StringType)
HoursOfOperation.attributes={HoursOfOperation_weekdayHours, HoursOfOperation_weekendHours}

# ContactInformation class attributes and methods
ContactInformation_address: Property = Property(name="address", type=StringType)
ContactInformation_phone: Property = Property(name="phone", type=StringType)
ContactInformation_email: Property = Property(name="email", type=StringType)
ContactInformation.attributes={ContactInformation_address, ContactInformation_email, ContactInformation_phone}

# Relationships
navBar: BinaryAssociation = BinaryAssociation(
    name="navBar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1))
    }
)
menuLinks: BinaryAssociation = BinaryAssociation(
    name="menuLinks",
    ends={
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1)),
        Property(name="MenuLink", type=MenuLink, multiplicity=Multiplicity(2, 2))
    }
)
reservationForm: BinaryAssociation = BinaryAssociation(
    name="reservationForm",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ReservationForm", type=ReservationForm, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
hours: BinaryAssociation = BinaryAssociation(
    name="hours",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="HoursOfOperation", type=HoursOfOperation, multiplicity=Multiplicity(1, 1))
    }
)
contactInfo: BinaryAssociation = BinaryAssociation(
    name="contactInfo",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactInformation", type=ContactInformation, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, NavBar, MenuLink, ReservationForm, Footer, HoursOfOperation, ContactInformation},
    associations={navBar, menuLinks, reservationForm, footer, hours, contactInfo},
    generalizations={}
)
