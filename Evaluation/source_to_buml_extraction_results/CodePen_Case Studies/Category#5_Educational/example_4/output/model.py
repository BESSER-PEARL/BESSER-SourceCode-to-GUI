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
FAQPage = Class(name="FAQPage")
AccordionContainer = Class(name="AccordionContainer")
AccordionItem = Class(name="AccordionItem")
AccordionHeader = Class(name="AccordionHeader")
AccordionContent = Class(name="AccordionContent")
AccordionBody = Class(name="AccordionBody")
BadgeSticky = Class(name="BadgeSticky")

# FAQPage class attributes and methods
FAQPage_description: Property = Property(name="description", type=StringType)
FAQPage.attributes={FAQPage_description}

# AccordionContainer class attributes and methods

# AccordionItem class attributes and methods

# AccordionHeader class attributes and methods

# AccordionContent class attributes and methods

# AccordionBody class attributes and methods
AccordionBody_content: Property = Property(name="content", type=StringType)
AccordionBody.attributes={AccordionBody_content}

# BadgeSticky class attributes and methods
BadgeSticky_href: Property = Property(name="href", type=StringType)
BadgeSticky_target: Property = Property(name="target", type=StringType)
BadgeSticky.attributes={BadgeSticky_href, BadgeSticky_target}

# Relationships
includesBody: BinaryAssociation = BinaryAssociation(
    name="includesBody",
    ends={
        Property(name="AccordionContent", type=AccordionContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AccordionBody", type=AccordionBody, multiplicity=Multiplicity(1, 1))
    }
)
containsContainer: BinaryAssociation = BinaryAssociation(
    name="containsContainer",
    ends={
        Property(name="FAQPage", type=FAQPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AccordionContainer", type=AccordionContainer, multiplicity=Multiplicity(1, 1))
    }
)
containsItems: BinaryAssociation = BinaryAssociation(
    name="containsItems",
    ends={
        Property(name="AccordionContainer", type=AccordionContainer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AccordionItem", type=AccordionItem, multiplicity=Multiplicity(2, 2))
    }
)
hasHeader: BinaryAssociation = BinaryAssociation(
    name="hasHeader",
    ends={
        Property(name="AccordionItem", type=AccordionItem, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AccordionHeader", type=AccordionHeader, multiplicity=Multiplicity(1, 1))
    }
)
hasContent: BinaryAssociation = BinaryAssociation(
    name="hasContent",
    ends={
        Property(name="AccordionItem", type=AccordionItem, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AccordionContent", type=AccordionContent, multiplicity=Multiplicity(1, 1))
    }
)
hasBadge: BinaryAssociation = BinaryAssociation(
    name="hasBadge",
    ends={
        Property(name="FAQPage", type=FAQPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="BadgeSticky", type=BadgeSticky, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FAQPage, AccordionContainer, AccordionItem, AccordionHeader, AccordionContent, AccordionBody, BadgeSticky},
    associations={includesBody, containsContainer, containsItems, hasHeader, hasContent, hasBadge},
    generalizations={}
)
