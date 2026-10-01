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
ContactInformation = Class(name="ContactInformation")
PatientResources = Class(name="PatientResources")
Newsletter = Class(name="Newsletter")
HealthcareOrganizationPage = Class(name="HealthcareOrganizationPage")
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")
Navigation = Class(name="Navigation")
Section = Class(name="Section")
Video = Class(name="Video")

# ContactInformation class attributes and methods
ContactInformation_address: Property = Property(name="address", type=StringType)
ContactInformation_phone: Property = Property(name="phone", type=StringType)
ContactInformation_email: Property = Property(name="email", type=StringType)
ContactInformation.attributes={ContactInformation_phone, ContactInformation_address, ContactInformation_email}

# PatientResources class attributes and methods

# Newsletter class attributes and methods
Newsletter_email: Property = Property(name="email", type=StringType)
Newsletter.attributes={Newsletter_email}

# HealthcareOrganizationPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# Navigation class attributes and methods

# Section class attributes and methods

# Video class attributes and methods

# Relationships
assoc9: BinaryAssociation = BinaryAssociation(
    name="assoc9",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="Newsletter", type=Newsletter, multiplicity=Multiplicity(1, 1))
    }
)
assoc1: BinaryAssociation = BinaryAssociation(
    name="assoc1",
    ends={
        Property(name="HealthcareOrganizationPage", type=HealthcareOrganizationPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
assoc2: BinaryAssociation = BinaryAssociation(
    name="assoc2",
    ends={
        Property(name="HealthcareOrganizationPage", type=HealthcareOrganizationPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
assoc3: BinaryAssociation = BinaryAssociation(
    name="assoc3",
    ends={
        Property(name="HealthcareOrganizationPage", type=HealthcareOrganizationPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
assoc4: BinaryAssociation = BinaryAssociation(
    name="assoc4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
assoc5: BinaryAssociation = BinaryAssociation(
    name="assoc5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
assoc6: BinaryAssociation = BinaryAssociation(
    name="assoc6",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Video", type=Video, multiplicity=Multiplicity(1, 1))
    }
)
assoc7: BinaryAssociation = BinaryAssociation(
    name="assoc7",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactInformation", type=ContactInformation, multiplicity=Multiplicity(1, 1))
    }
)
assoc8: BinaryAssociation = BinaryAssociation(
    name="assoc8",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="PatientResources", type=PatientResources, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactInformation, PatientResources, Newsletter, HealthcareOrganizationPage, Header, Main, Footer, Navigation, Section, Video},
    associations={assoc9, assoc1, assoc2, assoc3, assoc4, assoc5, assoc6, assoc7, assoc8},
    generalizations={}
)
