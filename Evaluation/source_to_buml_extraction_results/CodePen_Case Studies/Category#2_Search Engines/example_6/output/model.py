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
SearchedResultsDisplay = Class(name="SearchedResultsDisplay")
AfterSearchContainer = Class(name="AfterSearchContainer")
WikiResults = Class(name="WikiResults")
Wrapper = Class(name="Wrapper")
SearchBody = Class(name="SearchBody")
Footer = Class(name="Footer")
FooterLogos = Class(name="FooterLogos")

# SearchedResultsDisplay class attributes and methods

# AfterSearchContainer class attributes and methods
AfterSearchContainer_after_search: Property = Property(name="after_search", type=StringType)
AfterSearchContainer.attributes={AfterSearchContainer_after_search}

# WikiResults class attributes and methods

# Wrapper class attributes and methods

# SearchBody class attributes and methods
SearchBody_before_search: Property = Property(name="before_search", type=StringType)
SearchBody.attributes={SearchBody_before_search}

# Footer class attributes and methods

# FooterLogos class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="SearchedResultsDisplay", type=SearchedResultsDisplay, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="AfterSearchContainer", type=AfterSearchContainer, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="SearchedResultsDisplay", type=SearchedResultsDisplay, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="WikiResults", type=WikiResults, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="SearchBody", type=SearchBody, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="FooterLogos", type=FooterLogos, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SearchedResultsDisplay, AfterSearchContainer, WikiResults, Wrapper, SearchBody, Footer, FooterLogos},
    associations={association1, association2, association3, association4},
    generalizations={}
)
