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
Volunteer = Class(name="Volunteer")
Search = Class(name="Search")
Pagination = Class(name="Pagination")

# Volunteer class attributes and methods
Volunteer_id: Property = Property(name="id", type=IntegerType)
Volunteer_name: Property = Property(name="name", type=StringType)
Volunteer_phone: Property = Property(name="phone", type=StringType)
Volunteer_email: Property = Property(name="email", type=StringType)
Volunteer_status: Property = Property(name="status", type=StringType)
Volunteer_unix: Property = Property(name="unix", type=DateTimeType)
Volunteer.attributes={Volunteer_id, Volunteer_phone, Volunteer_name, Volunteer_email, Volunteer_unix, Volunteer_status}

# Search class attributes and methods
Search_selected: Property = Property(name="selected", type=StringType)
Search_search: Property = Property(name="search", type=StringType)
Search.attributes={Search_selected, Search_search}

# Pagination class attributes and methods
Pagination_resultlimit: Property = Property(name="resultlimit", type=IntegerType)
Pagination.attributes={Pagination_resultlimit}

# Relationships
searchFunctionality: BinaryAssociation = BinaryAssociation(
    name="searchFunctionality",
    ends={
        Property(name="Volunteer", type=Volunteer, multiplicity=Multiplicity(1, 1)),
        Property(name="Search", type=Search, multiplicity=Multiplicity(0, 9999))
    }
)
paginationControl: BinaryAssociation = BinaryAssociation(
    name="paginationControl",
    ends={
        Property(name="Volunteer", type=Volunteer, multiplicity=Multiplicity(1, 1)),
        Property(name="Pagination", type=Pagination, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Volunteer, Search, Pagination},
    associations={searchFunctionality, paginationControl},
    generalizations={}
)
