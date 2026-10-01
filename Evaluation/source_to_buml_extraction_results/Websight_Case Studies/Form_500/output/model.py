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
Video = Class(name="Video")
Form = Class(name="Form")
CourseDetails = Class(name="CourseDetails")
WebPage = Class(name="WebPage")

# Video class attributes and methods

# Form class attributes and methods
Form_username: Property = Property(name="username", type=StringType)
Form_password: Property = Property(name="password", type=StringType)
Form.attributes={Form_username, Form_password}

# CourseDetails class attributes and methods

# WebPage class attributes and methods

# Relationships
containsVideo: BinaryAssociation = BinaryAssociation(
    name="containsVideo",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Video", type=Video, multiplicity=Multiplicity(1, 1))
    }
)
containsForm: BinaryAssociation = BinaryAssociation(
    name="containsForm",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
containsCourseDetails: BinaryAssociation = BinaryAssociation(
    name="containsCourseDetails",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="CourseDetails", type=CourseDetails, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Video, Form, CourseDetails, WebPage},
    associations={containsVideo, containsForm, containsCourseDetails},
    generalizations={}
)
