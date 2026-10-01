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
PhoneInput = Class(name="PhoneInput")
TwoFactorInput = Class(name="TwoFactorInput")
NotificationBox = Class(name="NotificationBox")

# WebPage class attributes and methods

# PhoneInput class attributes and methods
PhoneInput_telephone: Property = Property(name="telephone", type=StringType)
PhoneInput.attributes={PhoneInput_telephone}

# TwoFactorInput class attributes and methods
TwoFactorInput_twoFactorAuth: Property = Property(name="twoFactorAuth", type=StringType)
TwoFactorInput.attributes={TwoFactorInput_twoFactorAuth}

# NotificationBox class attributes and methods
NotificationBox_successMessage: Property = Property(name="successMessage", type=StringType)
NotificationBox_errorMessage: Property = Property(name="errorMessage", type=StringType)
NotificationBox.attributes={NotificationBox_errorMessage, NotificationBox_successMessage}

# Relationships
containsPhoneInput: BinaryAssociation = BinaryAssociation(
    name="containsPhoneInput",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="PhoneInput", type=PhoneInput, multiplicity=Multiplicity(1, 1))
    }
)
containsTwoFactorInput: BinaryAssociation = BinaryAssociation(
    name="containsTwoFactorInput",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="TwoFactorInput", type=TwoFactorInput, multiplicity=Multiplicity(1, 1))
    }
)
containsNotificationBox: BinaryAssociation = BinaryAssociation(
    name="containsNotificationBox",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="NotificationBox", type=NotificationBox, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, PhoneInput, TwoFactorInput, NotificationBox},
    associations={containsPhoneInput, containsTwoFactorInput, containsNotificationBox},
    generalizations={}
)
