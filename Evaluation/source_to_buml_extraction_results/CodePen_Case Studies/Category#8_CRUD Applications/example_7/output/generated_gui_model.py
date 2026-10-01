from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="150px", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
TableColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
TablePosition = Position(type=PositionType.Relative, top="200px", left="20px")
tableSize = Size(width="100%", height="auto", padding="10px")
TableStyling = Styling(size=tableSize, position=TablePosition, color=TableColor)
viewComponent = ViewComponent(name="VehicleListView", description="Display a list of vehicles with actions")
addVehicleButton = Button(name="AddVehicleButton", description="Add a vehicle", label="Add Vehicle", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
datasource_vehicle = DataSourceElement(name="VehicleDataSource", dataSourceClass=Vehicle, fields=[Vehicle_make, Vehicle_model, Vehicle_mileage, Vehicle_status])
vehicleList = DataList(name="VehicleList", description="A list of vehicles", list_sources={datasource_vehicle}, styling=TableStyling)
VehicleListScreen = Screen(name="VehicleListScreen", description="Explore a collection of vehicles", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={addVehicleButton, vehicleList}, layout=ScreenLayout)
MyModule = Module(name="VehicleManagementModule", screens={VehicleListScreen})
gui_model = GUIModel(name="VehicleManagementApp", package="com.example.vehiclemanagement", versionCode="1", versionName="1.0", description="A comprehensive web application for managing vehicles.", screenCompatibility=True, modules={MyModule})
