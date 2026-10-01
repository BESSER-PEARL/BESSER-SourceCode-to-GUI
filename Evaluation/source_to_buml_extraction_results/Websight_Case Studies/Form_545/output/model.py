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
CharityOrganization = Class(name="CharityOrganization")
Header = Class(name="Header")
Main = Class(name="Main")
ImageSection = Class(name="ImageSection")
ButtonSection = Class(name="ButtonSection")
Footer = Class(name="Footer")
VolunteerForm = Class(name="VolunteerForm")

# CharityOrganization class attributes and methods

# Header class attributes and methods
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_subtitle, Header_title}

# Main class attributes and methods

# ImageSection class attributes and methods
ImageSection_imageUrl: Property = Property(name="imageUrl", type=StringType)
ImageSection.attributes={ImageSection_imageUrl}

# ButtonSection class attributes and methods

# Footer class attributes and methods
Footer_missionTitle: Property = Property(name="missionTitle", type=StringType)
Footer_missionDescription: Property = Property(name="missionDescription", type=StringType)
Footer_testimonialsTitle: Property = Property(name="testimonialsTitle", type=StringType)
Footer_testimonialsDescription: Property = Property(name="testimonialsDescription", type=StringType)
Footer_volunteerFormTitle: Property = Property(name="volunteerFormTitle", type=StringType)
Footer.attributes={Footer_missionTitle, Footer_missionDescription, Footer_testimonialsDescription, Footer_volunteerFormTitle, Footer_testimonialsTitle}

# VolunteerForm class attributes and methods
VolunteerForm_name: Property = Property(name="name", type=StringType)
VolunteerForm_email: Property = Property(name="email", type=StringType)
VolunteerForm.attributes={VolunteerForm_email, VolunteerForm_name}

# Relationships
assoc1: BinaryAssociation = BinaryAssociation(
    name="assoc1",
    ends={
        Property(name="CharityOrganization", type=CharityOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
assoc2: BinaryAssociation = BinaryAssociation(
    name="assoc2",
    ends={
        Property(name="CharityOrganization", type=CharityOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
assoc3: BinaryAssociation = BinaryAssociation(
    name="assoc3",
    ends={
        Property(name="CharityOrganization", type=CharityOrganization, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
assoc4: BinaryAssociation = BinaryAssociation(
    name="assoc4",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="ImageSection", type=ImageSection, multiplicity=Multiplicity(1, 1))
    }
)
assoc5: BinaryAssociation = BinaryAssociation(
    name="assoc5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="ButtonSection", type=ButtonSection, multiplicity=Multiplicity(1, 1))
    }
)
assoc6: BinaryAssociation = BinaryAssociation(
    name="assoc6",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="VolunteerForm", type=VolunteerForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={CharityOrganization, Header, Main, ImageSection, ButtonSection, Footer, VolunteerForm},
    associations={assoc1, assoc2, assoc3, assoc4, assoc5, assoc6},
    generalizations={}
)
