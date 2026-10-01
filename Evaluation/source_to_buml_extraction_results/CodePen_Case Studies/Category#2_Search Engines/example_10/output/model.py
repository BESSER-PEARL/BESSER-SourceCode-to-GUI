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
YouTubeVideoSearch = Class(name="YouTubeVideoSearch")
SearchForm = Class(name="SearchForm")
Results = Class(name="Results")
Buttons = Class(name="Buttons")

# YouTubeVideoSearch class attributes and methods
YouTubeVideoSearch_query: Property = Property(name="query", type=StringType)
YouTubeVideoSearch.attributes={YouTubeVideoSearch_query}

# SearchForm class attributes and methods
SearchForm_searchTerm: Property = Property(name="searchTerm", type=StringType)
SearchForm.attributes={SearchForm_searchTerm}

# Results class attributes and methods
Results_videoTitle: Property = Property(name="videoTitle", type=StringType)
Results_videoDuration: Property = Property(name="videoDuration", type=TimeType)
Results_uploadDate: Property = Property(name="uploadDate", type=DateType)
Results.attributes={Results_videoDuration, Results_uploadDate, Results_videoTitle}

# Buttons class attributes and methods
Buttons_nextPage: Property = Property(name="nextPage", type=BooleanType)
Buttons_previousPage: Property = Property(name="previousPage", type=BooleanType)
Buttons.attributes={Buttons_nextPage, Buttons_previousPage}

# Relationships
searchForm: BinaryAssociation = BinaryAssociation(
    name="searchForm",
    ends={
        Property(name="YouTubeVideoSearch", type=YouTubeVideoSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchForm", type=SearchForm, multiplicity=Multiplicity(1, 1))
    }
)
results: BinaryAssociation = BinaryAssociation(
    name="results",
    ends={
        Property(name="YouTubeVideoSearch", type=YouTubeVideoSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="Results", type=Results, multiplicity=Multiplicity(1, 1))
    }
)
navigationButtons: BinaryAssociation = BinaryAssociation(
    name="navigationButtons",
    ends={
        Property(name="YouTubeVideoSearch", type=YouTubeVideoSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="Buttons", type=Buttons, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={YouTubeVideoSearch, SearchForm, Results, Buttons},
    associations={searchForm, results, navigationButtons},
    generalizations={}
)
