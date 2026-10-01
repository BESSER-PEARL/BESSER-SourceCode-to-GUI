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
ContactManager = Class(name="ContactManager")
ContactForm = Class(name="ContactForm")
SearchForm = Class(name="SearchForm")

# ContactManager class attributes and methods

# ContactForm class attributes and methods
ContactForm_inputEmail: Property = Property(name="inputEmail", type=StringType)
ContactForm_inputLocationCity: Property = Property(name="inputLocationCity", type=StringType)
ContactForm_inputLocationCountry: Property = Property(name="inputLocationCountry", type=StringType)
ContactForm_inputYourRelation: Property = Property(name="inputYourRelation", type=StringType)
ContactForm_inputBirthday: Property = Property(name="inputBirthday", type=DateType)
ContactForm_inputGivenName: Property = Property(name="inputGivenName", type=StringType)
ContactForm_inputFamilyName: Property = Property(name="inputFamilyName", type=StringType)
ContactForm_inputPhoneNumber: Property = Property(name="inputPhoneNumber", type=StringType)
ContactForm.attributes={ContactForm_inputFamilyName, ContactForm_inputLocationCountry, ContactForm_inputBirthday, ContactForm_inputPhoneNumber, ContactForm_inputYourRelation, ContactForm_inputGivenName, ContactForm_inputEmail, ContactForm_inputLocationCity}

# SearchForm class attributes and methods
SearchForm_searchString: Property = Property(name="searchString", type=StringType)
SearchForm.attributes={SearchForm_searchString}

# Relationships
containsForm1: BinaryAssociation = BinaryAssociation(
    name="containsForm1",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactForm", type=ContactForm, multiplicity=Multiplicity(1, 1))
    }
)
containsForm2: BinaryAssociation = BinaryAssociation(
    name="containsForm2",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchForm", type=SearchForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactManager, ContactForm, SearchForm},
    associations={containsForm1, containsForm2},
    generalizations={}
)
