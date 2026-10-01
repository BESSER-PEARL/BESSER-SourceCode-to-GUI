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
App = Class(name="App")
UIHelpers = Class(name="UIHelpers")
Filtered = Class(name="Filtered")
Results = Class(name="Results")
Document = Class(name="Document")

# App class attributes and methods
App_queryinput: Property = Property(name="queryinput", type=StringType)
App_config: Property = Property(name="config", type=StringType)
App_q: Property = Property(name="q", type=StringType)
App.attributes={App_config, App_queryinput, App_q}

# UIHelpers class attributes and methods
UIHelpers_waitingForResults: Property = Property(name="waitingForResults", type=BooleanType)
UIHelpers_totalHits: Property = Property(name="totalHits", type=IntegerType)
UIHelpers_docCount: Property = Property(name="docCount", type=IntegerType)
UIHelpers_allHitsDisplayed: Property = Property(name="allHitsDisplayed", type=BooleanType)
UIHelpers_json: Property = Property(name="json", type=BooleanType)
UIHelpers.attributes={UIHelpers_totalHits, UIHelpers_json, UIHelpers_waitingForResults, UIHelpers_docCount, UIHelpers_allHitsDisplayed}

# Filtered class attributes and methods
Filtered_categories: Property = Property(name="categories", type=StringType)
Filtered.attributes={Filtered_categories}

# Results class attributes and methods
Results_categories: Property = Property(name="categories", type=StringType)
Results_searchresults: Property = Property(name="searchresults", type=StringType)
Results.attributes={Results_categories, Results_searchresults}

# Document class attributes and methods
Document_name: Property = Property(name="name", type=StringType)
Document_image: Property = Property(name="image", type=StringType)
Document.attributes={Document_name, Document_image}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="App", type=App, multiplicity=Multiplicity(1, 1)),
        Property(name="UIHelpers", type=UIHelpers, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="App", type=App, multiplicity=Multiplicity(1, 1)),
        Property(name="Results", type=Results, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Results", type=Results, multiplicity=Multiplicity(1, 1)),
        Property(name="Document", type=Document, multiplicity=Multiplicity(0, 9999))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="UIHelpers", type=UIHelpers, multiplicity=Multiplicity(1, 1)),
        Property(name="Filtered", type=Filtered, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={App, UIHelpers, Filtered, Results, Document},
    associations={association1, association2, association3, association4},
    generalizations={}
)
