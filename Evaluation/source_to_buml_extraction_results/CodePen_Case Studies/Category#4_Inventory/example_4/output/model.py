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
Contents = Class(name="Contents")
Pagination = Class(name="Pagination")
ContentsTable = Class(name="ContentsTable")
ContentsPin = Class(name="ContentsPin")
WebPage = Class(name="WebPage")

# Contents class attributes and methods
Contents_contentName: Property = Property(name="contentName", type=StringType)
Contents_category: Property = Property(name="category", type=StringType)
Contents_registered: Property = Property(name="registered", type=DateType)
Contents_user: Property = Property(name="user", type=StringType)
Contents.attributes={Contents_contentName, Contents_registered, Contents_user, Contents_category}

# Pagination class attributes and methods
Pagination_previousPage: Property = Property(name="previousPage", type=StringType)
Pagination_currentPage: Property = Property(name="currentPage", type=StringType)
Pagination_nextPage: Property = Property(name="nextPage", type=StringType)
Pagination.attributes={Pagination_currentPage, Pagination_previousPage, Pagination_nextPage}

# ContentsTable class attributes and methods
ContentsTable_contents: Property = Property(name="contents", type=Contents)
ContentsTable_pagination: Property = Property(name="pagination", type=Pagination)
ContentsTable.attributes={ContentsTable_pagination, ContentsTable_contents}

# ContentsPin class attributes and methods

# WebPage class attributes and methods
WebPage_contentsPin: Property = Property(name="contentsPin", type=ContentsPin)
WebPage_contentsTable: Property = Property(name="contentsTable", type=ContentsTable)
WebPage.attributes={WebPage_contentsTable, WebPage_contentsPin}

# Relationships
pinAssociation: BinaryAssociation = BinaryAssociation(
    name="pinAssociation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentsPin", type=ContentsPin, multiplicity=Multiplicity(1, 1))
    }
)
tableAssociation: BinaryAssociation = BinaryAssociation(
    name="tableAssociation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentsTable", type=ContentsTable, multiplicity=Multiplicity(1, 1))
    }
)
contentsAssociation: BinaryAssociation = BinaryAssociation(
    name="contentsAssociation",
    ends={
        Property(name="ContentsTable", type=ContentsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="Contents", type=Contents, multiplicity=Multiplicity(1, 9999))
    }
)
paginationAssociation: BinaryAssociation = BinaryAssociation(
    name="paginationAssociation",
    ends={
        Property(name="ContentsTable", type=ContentsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="Pagination", type=Pagination, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Contents, Pagination, ContentsTable, ContentsPin, WebPage},
    associations={pinAssociation, tableAssociation, contentsAssociation, paginationAssociation},
    generalizations={}
)
