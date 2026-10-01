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
EducationInstitution = Class(name="EducationInstitution")
Academics = Class(name="Academics")
Admissions = Class(name="Admissions")
StudentLife = Class(name="StudentLife")
Testimonials = Class(name="Testimonials")

# EducationInstitution class attributes and methods
EducationInstitution_image: Property = Property(name="image", type=StringType)
EducationInstitution_title: Property = Property(name="title", type=StringType)
EducationInstitution_description: Property = Property(name="description", type=StringType)
EducationInstitution.attributes={EducationInstitution_image, EducationInstitution_title, EducationInstitution_description}

# Academics class attributes and methods
Academics_description: Property = Property(name="description", type=StringType)
Academics.attributes={Academics_description}

# Admissions class attributes and methods
Admissions_description: Property = Property(name="description", type=StringType)
Admissions.attributes={Admissions_description}

# StudentLife class attributes and methods
StudentLife_description: Property = Property(name="description", type=StringType)
StudentLife.attributes={StudentLife_description}

# Testimonials class attributes and methods
Testimonials_description: Property = Property(name="description", type=StringType)
Testimonials.attributes={Testimonials_description}

# Relationships
section1: BinaryAssociation = BinaryAssociation(
    name="section1",
    ends={
        Property(name="EducationInstitution", type=EducationInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Academics", type=Academics, multiplicity=Multiplicity(1, 1))
    }
)
section2: BinaryAssociation = BinaryAssociation(
    name="section2",
    ends={
        Property(name="EducationInstitution", type=EducationInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Admissions", type=Admissions, multiplicity=Multiplicity(1, 1))
    }
)
section3: BinaryAssociation = BinaryAssociation(
    name="section3",
    ends={
        Property(name="EducationInstitution", type=EducationInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="StudentLife", type=StudentLife, multiplicity=Multiplicity(1, 1))
    }
)
section4: BinaryAssociation = BinaryAssociation(
    name="section4",
    ends={
        Property(name="EducationInstitution", type=EducationInstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Testimonials", type=Testimonials, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={EducationInstitution, Academics, Admissions, StudentLife, Testimonials},
    associations={section1, section2, section3, section4},
    generalizations={}
)
