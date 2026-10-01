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
FitnessCenterPage = Class(name="FitnessCenterPage")
MembershipPricing = Class(name="MembershipPricing")

# FitnessCenterPage class attributes and methods

# MembershipPricing class attributes and methods
MembershipPricing_plan: Property = Property(name="plan", type=StringType)
MembershipPricing_cost: Property = Property(name="cost", type=FloatType)
MembershipPricing.attributes={MembershipPricing_plan, MembershipPricing_cost}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="FitnessCenterPage", type=FitnessCenterPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MembershipPricing", type=MembershipPricing, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FitnessCenterPage, MembershipPricing},
    associations={contains},
    generalizations={}
)
