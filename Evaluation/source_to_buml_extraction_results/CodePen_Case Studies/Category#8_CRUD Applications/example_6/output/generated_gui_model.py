from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from some_gui_library import Layout, LayoutType, JustificationType, Color, Position, PositionType, Size, UnitSize, Styling, Form, InputField, InputFieldType, Button, ButtonType, ButtonActionType, DataList, DataSourceElement, ViewComponent, Screen, Module, GUIModel

screen_layout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="20px", alignment=JustificationType.Center)
form_styling = Styling(size=Size(width="100%", padding="10px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC"))
button_styling = Styling(size=Size(width="100%", height="40px", padding="10px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3"))
table_styling = Styling(size=Size(width="100%", padding="10px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC"))
modal_styling = Styling(size=Size(width="400px", padding="20px", font_size="16px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Fixed, top="50%", left="50%", alignment="center", z_index=1000), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC"))
add_user_form = Form(
    name="AddUserForm",
    description="Form to add a new user",
    inputFields={InputField(name="NameInput", description="Input for user's name", type=InputFieldType.Text, validationRules="required", styling=form_styling), InputField(name="AddressInput", description="Input for user's address", type=InputFieldType.Text, validationRules="required", styling=form_styling), InputField(name="AgeInput", description="Input for user's age", type=InputFieldType.Number, validationRules="required|min:10|max:100", styling=form_styling)},
    styling=form_styling,
)
submit_button = Button(name="SubmitButton", description="Button to submit the form", label="SUBMIT", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=button_styling)
user_table = DataList(name="UserTable", description="Table displaying users", list_sources={DataSourceElement(name="UserDataSource", dataSourceClass="UserPage", fields={"UserPage_name", "UserPage_address", "UserPage_age"})}, styling=table_styling)
update_user_modal = ViewComponent(name="UpdateUserModal", description="Modal for updating user information", styling=modal_styling)
user_page_screen = Screen(name="UserPageScreen", description="Screen for managing users", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={add_user_form, submit_button, user_table, update_user_modal}, is_main_page=True, layout=screen_layout)
user_module = Module(name="UserModule", screens={user_page_screen})
gui_model = GUIModel(name="UserManagementApp", package="com.example.usermanagement", versionCode="1", versionName="1.0", description="An application for managing users.", screenCompatibility=True, modules={user_module})
