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
AccountSetup = Class(name="AccountSetup")
SocialProfiles = Class(name="SocialProfiles")
PersonalDetails = Class(name="PersonalDetails")

# AccountSetup class attributes and methods
AccountSetup_email: Property = Property(name="email", type=StringType)
AccountSetup_pass: Property = Property(name="pass", type=StringType)
AccountSetup_cpass: Property = Property(name="cpass", type=StringType)
AccountSetup.attributes={AccountSetup_cpass, AccountSetup_email, AccountSetup_pass}

# SocialProfiles class attributes and methods
SocialProfiles_twitter: Property = Property(name="twitter", type=StringType)
SocialProfiles_facebook: Property = Property(name="facebook", type=StringType)
SocialProfiles_gplus: Property = Property(name="gplus", type=StringType)
SocialProfiles.attributes={SocialProfiles_facebook, SocialProfiles_gplus, SocialProfiles_twitter}

# PersonalDetails class attributes and methods
PersonalDetails_fname: Property = Property(name="fname", type=StringType)
PersonalDetails_lname: Property = Property(name="lname", type=StringType)
PersonalDetails_phone: Property = Property(name="phone", type=StringType)
PersonalDetails_address: Property = Property(name="address", type=StringType)
PersonalDetails.attributes={PersonalDetails_fname, PersonalDetails_lname, PersonalDetails_phone, PersonalDetails_address}

# Relationships
step2_to_step3: BinaryAssociation = BinaryAssociation(
    name="step2_to_step3",
    ends={
        Property(name="SocialProfiles", type=SocialProfiles, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="PersonalDetails", type=PersonalDetails, multiplicity=Multiplicity(1, 1))
    }
)
step1_to_step2: BinaryAssociation = BinaryAssociation(
    name="step1_to_step2",
    ends={
        Property(name="AccountSetup", type=AccountSetup, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="SocialProfiles", type=SocialProfiles, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AccountSetup, SocialProfiles, PersonalDetails},
    associations={step2_to_step3, step1_to_step2},
    generalizations={}
)
