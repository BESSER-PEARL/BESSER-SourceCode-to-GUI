from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
##############################
#      GUI model definition  #
##############################

####### Styling definitions ################

# Screen layout
ScreenLayout = Layout(
    type=LayoutType.Flex,
    orientation="vertical",
    gap="15px",
    alignment=JustificationType.Center
)

# Button styling
ButtonColor = Color(
    background_color="#007BFF",
    text_color="#FFFFFF",
    border_color="#0056b3"
)
buttonPosition = Position(
    type=PositionType.Relative,
    z_index=10
)
buttonSize = Size(
    width="auto",
    height="40px",
    padding="8px",
    margin="24px",
    font_size="14px",
    unit_size=UnitSize.PIXELS
)
buttonStyling = Styling(
    size=buttonSize,
    position=buttonPosition,
    color=ButtonColor
)

# Table styling
TableColor = Color(
    background_color="#FFFFFF",
    text_color="#343A40",
    border_color="#CED4DA"
)
TablePosition = Position(
    type=PositionType.Relative,
    top="200px",
    left="20px",
    z_index=0
)
tableSize = Size(
    width="100%",
    height="auto",
    padding="10px",
    unit_size=UnitSize.PIXELS
)
TableStyling = Styling(
    size=tableSize,
    position=TablePosition,
    color=TableColor
)

# Action button styling
actionButtonPosition = Position(
    type=PositionType.Inline,
    alignment="right",
    z_index=0
)
actionButtonSize = Size(
    width="60px",
    height="30px",
    padding="10px",
    font_size="14px",
    unit_size=UnitSize.PIXELS
)

# Edit button styling
editButtonColor = Color(
    background_color="#3B82F6",
    text_color="#FFFFFF",
    border_color="#2563EB"
)
EditButtonStyling = Styling(
    size=actionButtonSize,
    position=actionButtonPosition,
    color=editButtonColor
)

# Delete button styling
deleteButtonColor = Color(
    background_color="#EF4444",
    text_color="#FFFFFF",
    border_color="#DC2626"
)
DeleteButtonStyling = Styling(
    size=actionButtonSize,
    position=actionButtonPosition,
    color=deleteButtonColor
)

##### Elements for Bodega Management Screen #####

# ViewComponent definition
viewComponent = ViewComponent(
    name="BodegaListView",
    description="Display a list of bodegas with actions"
)

# Add Bodega Button
addBodegaButton = Button(
    name="AddBodegaButton",
    description="Add a new bodega",
    label="A�adir Bodega",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add,
    styling=buttonStyling
)

# Edit Bodega Button
editBodegaButton = Button(
    name="EditBodegaButton",
    description="Edit a bodega",
    label="Entrar",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Edit,
    styling=EditButtonStyling
)

# Delete Bodega Button
deleteBodegaButton = Button(
    name="DeleteBodegaButton",
    description="Delete a bodega",
    label="Borrar",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Delete,
    styling=DeleteButtonStyling
)

# Bodega DataSource definition
datasource_bodega = DataSourceElement(
    name="BodegaDataSource",
    dataSourceClass=Bodega,
    fields=[Bodega_nombre, Bodega_localizacion, Bodega_telefono, Bodega_email]
)

# Bodega List definition
bodegaList = DataList(
    name="BodegaList",
    description="A list of bodegas",
    list_sources={datasource_bodega},
    styling=TableStyling
)

# Bodega Management Screen definition
BodegaManagementScreen = Screen(
    name="BodegaManagementScreen",
    description="Manage bodegas",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    is_main_page=True,
    view_elements={addBodegaButton, bodegaList, editBodegaButton, deleteBodegaButton},
    layout=ScreenLayout
)

# Module definition
BodegaModule = Module(
    name="BodegaModule",
    screens={BodegaManagementScreen}
)

# Application definition
gui_model = GUIModel(
    name="BodegaManagementApp",
    package="com.example.bodegamanagement",
    versionCode="1",
    versionName="1.0",
    description="A web application for managing bodegas.",
    screenCompatibility=True,
    modules={BodegaModule}
)

# Class and attributes
# Class: Bodega
# Attributes: nombre, localizacion, telefono, email
