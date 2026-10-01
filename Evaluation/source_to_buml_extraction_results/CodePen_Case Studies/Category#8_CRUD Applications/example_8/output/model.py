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
EmployeeManagementPage = Class(name="EmployeeManagementPage")
Employee = Class(name="Employee")
Modal = Class(name="Modal")
AddEmployeeModal = Class(name="AddEmployeeModal")
EditEmployeeModal = Class(name="EditEmployeeModal")
DeleteEmployeeModal = Class(name="DeleteEmployeeModal")

# EmployeeManagementPage class attributes and methods

# Employee class attributes and methods
Employee_name: Property = Property(name="name", type=StringType)
Employee_email: Property = Property(name="email", type=StringType)
Employee_address: Property = Property(name="address", type=StringType)
Employee_phone: Property = Property(name="phone", type=StringType)
Employee.attributes={Employee_name, Employee_email, Employee_address, Employee_phone}

# Modal class attributes and methods
Modal_title: Property = Property(name="title", type=StringType)
Modal.attributes={Modal_title}

# AddEmployeeModal class attributes and methods

# EditEmployeeModal class attributes and methods

# DeleteEmployeeModal class attributes and methods
DeleteEmployeeModal_confirmationMessage: Property = Property(name="confirmationMessage", type=StringType)
DeleteEmployeeModal.attributes={DeleteEmployeeModal_confirmationMessage}

# Relationships
modal_association1: BinaryAssociation = BinaryAssociation(
    name="modal_association1",
    ends={
        Property(name="EmployeeManagementPage", type=EmployeeManagementPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Modal", type=Modal, multiplicity=Multiplicity(1, 1))
    }
)
emp_association1: BinaryAssociation = BinaryAssociation(
    name="emp_association1",
    ends={
        Property(name="EmployeeManagementPage", type=EmployeeManagementPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_AddEmployeeModal_Modal = Generalization(general=Modal, specific=AddEmployeeModal)
gen_EditEmployeeModal_Modal = Generalization(general=Modal, specific=EditEmployeeModal)
gen_DeleteEmployeeModal_Modal = Generalization(general=Modal, specific=DeleteEmployeeModal)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={EmployeeManagementPage, Employee, Modal, AddEmployeeModal, EditEmployeeModal, DeleteEmployeeModal},
    associations={modal_association1, emp_association1},
    generalizations={gen_AddEmployeeModal_Modal, gen_EditEmployeeModal_Modal, gen_DeleteEmployeeModal_Modal}
)
