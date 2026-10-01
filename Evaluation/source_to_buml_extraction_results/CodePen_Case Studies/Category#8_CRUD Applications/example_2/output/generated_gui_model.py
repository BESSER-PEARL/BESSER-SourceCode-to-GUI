from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#28a745", text_color="#FFFFFF", border_color="#218838")
DeleteButtonColor = Color(background_color="#dc3545", text_color="#FFFFFF", border_color="#c82333")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
deleteButtonStyling = Styling(size=buttonSize, position=buttonPosition, color=DeleteButtonColor)
TableColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
TablePosition = Position(type=PositionType.Relative, top="200px", left="20px")
tableSize = Size(width="100%", padding="10px")
TableStyling = Styling(size=tableSize, position=TablePosition, color=TableColor)
ModalColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
ModalPosition = Position(type=PositionType.Fixed, top="50%", left="50%", alignment="center", z_index=1000)
modalSize = Size(width="500px", padding="20px", unit_size=UnitSize.PIXELS)
ModalStyling = Styling(size=modalSize, position=ModalPosition, color=ModalColor)
viewComponent = ViewComponent(name="EmployeeListView", description="Display a list of employees with actions")
addEmployeeButton = Button(name="AddEmployeeButton", description="Add a new employee", label="Add New Employee", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
deleteEmployeeButton = Button(name="DeleteEmployeeButton", description="Delete selected employees", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=deleteButtonStyling)
datasource_employee = DataSourceElement(name="EmployeeDataSource", dataSourceClass=Employee, fields=[Employee_name, Employee_email, Employee_address, Employee_phone])
employeeList = DataList(name="EmployeeList", description="A list of employees", list_sources={datasource_employee}, styling=TableStyling)
addEmployeeModal = Form(
    name="AddEmployeeModal",
    description="Form to add a new employee",
    inputFields={
        InputField(name="NameField", description="Employee Name", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
        InputField(name="EmailField", description="Employee Email", type=InputFieldType.Email, validationRules="required", styling=ModalStyling),
        InputField(name="AddressField", description="Employee Address", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
        InputField(name="PhoneField", description="Employee Phone", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
    },
    styling=ModalStyling,
)
editEmployeeModal = Form(
    name="EditEmployeeModal",
    description="Form to edit an employee",
    inputFields={
        InputField(name="NameField", description="Employee Name", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
        InputField(name="EmailField", description="Employee Email", type=InputFieldType.Email, validationRules="required", styling=ModalStyling),
        InputField(name="AddressField", description="Employee Address", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
        InputField(name="PhoneField", description="Employee Phone", type=InputFieldType.Text, validationRules="required", styling=ModalStyling),
    },
    styling=ModalStyling,
)
deleteEmployeeModal = Form(name="DeleteEmployeeModal", description="Confirmation to delete employees", inputFields={}, styling=ModalStyling)
EmployeeManagementScreen = Screen(name="EmployeeManagementScreen", description="Manage employees with add, edit, and delete functionalities", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={addEmployeeButton, deleteEmployeeButton, employeeList, addEmployeeModal, editEmployeeModal, deleteEmployeeModal}, layout=ScreenLayout)
EmployeeModule = Module(name="EmployeeModule", screens={EmployeeManagementScreen})
gui_model = GUIModel(name="EmployeeManagementApp", package="com.example.employeemanagement", versionCode="1", versionName="1.0", description="A web application for managing employees.", screenCompatibility=True, modules={EmployeeModule})
