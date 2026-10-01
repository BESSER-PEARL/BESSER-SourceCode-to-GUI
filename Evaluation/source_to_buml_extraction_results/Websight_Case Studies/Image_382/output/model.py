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

# WebPage class attributes and methods
WebPage_courses: Property = Property(name="courses", type=StringType)
WebPage_faculty: Property = Property(name="faculty", type=StringType)
WebPage_achievements: Property = Property(name="achievements", type=StringType)
WebPage_lastUpdated: Property = Property(name="lastUpdated", type=DateTimeType)
WebPage_isActive: Property = Property(name="isActive", type=BooleanType)
WebPage_programs: Property = Property(name="programs", type=StringType)
WebPage.attributes={WebPage_programs, WebPage_lastUpdated, WebPage_isActive, WebPage_courses, WebPage_faculty, WebPage_achievements}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
