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
Employee = Class(name="Employee")
EmployeeTable = Class(name="EmployeeTable")
Modal = Class(name="Modal")
AddEmployeeModal = Class(name="AddEmployeeModal")
EditEmployeeModal = Class(name="EditEmployeeModal")
DeleteEmployeeModal = Class(name="DeleteEmployeeModal")

# Employee class attributes and methods
Employee_name: Property = Property(name="name", type=StringType)
Employee_email: Property = Property(name="email", type=StringType)
Employee_address: Property = Property(name="address", type=StringType)
Employee_phone: Property = Property(name="phone", type=StringType)
Employee.attributes={Employee_email, Employee_address, Employee_name, Employee_phone}

# EmployeeTable class attributes and methods
EmployeeTable_employees: Property = Property(name="employees", type=StringType)
EmployeeTable.attributes={EmployeeTable_employees}

# Modal class attributes and methods
Modal_title: Property = Property(name="title", type=StringType)
Modal.attributes={Modal_title}

# AddEmployeeModal class attributes and methods

# EditEmployeeModal class attributes and methods

# DeleteEmployeeModal class attributes and methods

# Relationships
containsEmployees: BinaryAssociation = BinaryAssociation(
    name="containsEmployees",
    ends={
        Property(name="EmployeeTable", type=EmployeeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="Employee", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
hasAddModal: BinaryAssociation = BinaryAssociation(
    name="hasAddModal",
    ends={
        Property(name="EmployeeTable", type=EmployeeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="AddEmployeeModal", type=AddEmployeeModal, multiplicity=Multiplicity(1, 1))
    }
)
hasEditModal: BinaryAssociation = BinaryAssociation(
    name="hasEditModal",
    ends={
        Property(name="EmployeeTable", type=EmployeeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="EditEmployeeModal", type=EditEmployeeModal, multiplicity=Multiplicity(1, 1))
    }
)
hasDeleteModal: BinaryAssociation = BinaryAssociation(
    name="hasDeleteModal",
    ends={
        Property(name="EmployeeTable", type=EmployeeTable, multiplicity=Multiplicity(1, 1)),
        Property(name="DeleteEmployeeModal", type=DeleteEmployeeModal, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_AddEmployeeModal_Modal = Generalization(general=Modal, specific=AddEmployeeModal)
gen_EditEmployeeModal_Modal = Generalization(general=Modal, specific=EditEmployeeModal)
gen_DeleteEmployeeModal_Modal = Generalization(general=Modal, specific=DeleteEmployeeModal)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Employee, EmployeeTable, Modal, AddEmployeeModal, EditEmployeeModal, DeleteEmployeeModal},
    associations={containsEmployees, hasAddModal, hasEditModal, hasDeleteModal},
    generalizations={gen_AddEmployeeModal_Modal, gen_EditEmployeeModal_Modal, gen_DeleteEmployeeModal_Modal}
)
