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
Section = Class(name="Section")
Row = Class(name="Row")
Column = Class(name="Column")

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage.attributes={WebPage_title}

# Section class attributes and methods
Section_sectionClass: Property = Property(name="sectionClass", type=StringType)
Section.attributes={Section_sectionClass}

# Row class attributes and methods
Row_rowClass: Property = Property(name="rowClass", type=StringType)
Row.attributes={Row_rowClass}

# Column class attributes and methods
Column_columnClass: Property = Property(name="columnClass", type=StringType)
Column_content: Property = Property(name="content", type=StringType)
Column.attributes={Column_content, Column_columnClass}

# Relationships
containsSection: BinaryAssociation = BinaryAssociation(
    name="containsSection",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
containsRow: BinaryAssociation = BinaryAssociation(
    name="containsRow",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Row", type=Row, multiplicity=Multiplicity(1, 1))
    }
)
containsColumn: BinaryAssociation = BinaryAssociation(
    name="containsColumn",
    ends={
        Property(name="Row", type=Row, multiplicity=Multiplicity(1, 1)),
        Property(name="Column", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Section, Row, Column},
    associations={containsSection, containsRow, containsColumn},
    generalizations={}
)
