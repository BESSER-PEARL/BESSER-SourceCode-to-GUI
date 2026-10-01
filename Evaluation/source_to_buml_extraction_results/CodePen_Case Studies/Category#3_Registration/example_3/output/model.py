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
UserRegistration = Class(name="UserRegistration")
Container = Class(name="Container")
RegisterLeft = Class(name="RegisterLeft")
RegisterRight = Class(name="RegisterRight")
TabContent = Class(name="TabContent")
EmployeeForm = Class(name="EmployeeForm")
HirerForm = Class(name="HirerForm")

# UserRegistration class attributes and methods

# Container class attributes and methods

# RegisterLeft class attributes and methods
RegisterLeft_welcomeMessage: Property = Property(name="welcomeMessage", type=StringType)
RegisterLeft_loginButton: Property = Property(name="loginButton", type=BooleanType)
RegisterLeft.attributes={RegisterLeft_welcomeMessage, RegisterLeft_loginButton}

# RegisterRight class attributes and methods

# TabContent class attributes and methods

# EmployeeForm class attributes and methods
EmployeeForm_firstName: Property = Property(name="firstName", type=StringType)
EmployeeForm_lastName: Property = Property(name="lastName", type=StringType)
EmployeeForm_password: Property = Property(name="password", type=StringType)
EmployeeForm_confirmPassword: Property = Property(name="confirmPassword", type=StringType)
EmployeeForm_gender: Property = Property(name="gender", type=StringType)
EmployeeForm_email: Property = Property(name="email", type=StringType)
EmployeeForm_phone: Property = Property(name="phone", type=StringType)
EmployeeForm_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
EmployeeForm_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
EmployeeForm.attributes={EmployeeForm_password, EmployeeForm_phone, EmployeeForm_firstName, EmployeeForm_confirmPassword, EmployeeForm_securityAnswer, EmployeeForm_lastName, EmployeeForm_gender, EmployeeForm_securityQuestion, EmployeeForm_email}

# HirerForm class attributes and methods
HirerForm_firstName: Property = Property(name="firstName", type=StringType)
HirerForm_lastName: Property = Property(name="lastName", type=StringType)
HirerForm_email: Property = Property(name="email", type=StringType)
HirerForm_phone: Property = Property(name="phone", type=StringType)
HirerForm_password: Property = Property(name="password", type=StringType)
HirerForm_confirmPassword: Property = Property(name="confirmPassword", type=StringType)
HirerForm_securityQuestion: Property = Property(name="securityQuestion", type=StringType)
HirerForm_securityAnswer: Property = Property(name="securityAnswer", type=StringType)
HirerForm.attributes={HirerForm_email, HirerForm_securityAnswer, HirerForm_confirmPassword, HirerForm_phone, HirerForm_firstName, HirerForm_password, HirerForm_securityQuestion, HirerForm_lastName}

# Relationships
UR_Container: BinaryAssociation = BinaryAssociation(
    name="UR_Container",
    ends={
        Property(name="UserRegistration", type=UserRegistration, multiplicity=Multiplicity(1, 1)),
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1))
    }
)
C_RegisterLeft: BinaryAssociation = BinaryAssociation(
    name="C_RegisterLeft",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1)),
        Property(name="RegisterLeft", type=RegisterLeft, multiplicity=Multiplicity(1, 1))
    }
)
C_RegisterRight: BinaryAssociation = BinaryAssociation(
    name="C_RegisterRight",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1)),
        Property(name="RegisterRight", type=RegisterRight, multiplicity=Multiplicity(1, 1))
    }
)
RR_TabContent: BinaryAssociation = BinaryAssociation(
    name="RR_TabContent",
    ends={
        Property(name="RegisterRight", type=RegisterRight, multiplicity=Multiplicity(1, 1)),
        Property(name="TabContent", type=TabContent, multiplicity=Multiplicity(1, 1))
    }
)
TC_EmployeeForm: BinaryAssociation = BinaryAssociation(
    name="TC_EmployeeForm",
    ends={
        Property(name="TabContent", type=TabContent, multiplicity=Multiplicity(1, 1)),
        Property(name="EmployeeForm", type=EmployeeForm, multiplicity=Multiplicity(1, 1))
    }
)
TC_HirerForm: BinaryAssociation = BinaryAssociation(
    name="TC_HirerForm",
    ends={
        Property(name="TabContent", type=TabContent, multiplicity=Multiplicity(1, 1)),
        Property(name="HirerForm", type=HirerForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={UserRegistration, Container, RegisterLeft, RegisterRight, TabContent, EmployeeForm, HirerForm},
    associations={UR_Container, C_RegisterLeft, C_RegisterRight, RR_TabContent, TC_EmployeeForm, TC_HirerForm},
    generalizations={}
)
