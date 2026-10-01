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
EducationCompany = Class(name="EducationCompany")
Footer = Class(name="Footer")
AboutUs = Class(name="AboutUs")

# EducationCompany class attributes and methods
EducationCompany_logo: Property = Property(name="logo", type=StringType)
EducationCompany_title: Property = Property(name="title", type=StringType)
EducationCompany_description: Property = Property(name="description", type=StringType)
EducationCompany.attributes={EducationCompany_logo, EducationCompany_description, EducationCompany_title}

# Footer class attributes and methods
Footer_copyright: Property = Property(name="copyright", type=StringType)
Footer.attributes={Footer_copyright}

# AboutUs class attributes and methods
AboutUs_title: Property = Property(name="title", type=StringType)
AboutUs_description: Property = Property(name="description", type=StringType)
AboutUs.attributes={AboutUs_title, AboutUs_description}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="EducationCompany", type=EducationCompany, multiplicity=Multiplicity(1, 1)),
        Property(name="AboutUs", type=AboutUs, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="EducationCompany", type=EducationCompany, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={EducationCompany, Footer, AboutUs},
    associations={association1, association2},
    generalizations={}
)
