from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Grid, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
superheroesListViewComponent = ViewComponent(name="SuperheroesListView", description="Display a list of superheroes with actions")
addSuperheroButton = Button(name="AddSuperheroButton", description="Add a new superhero", label="Add Superhero", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
editHeroButton = Button(name="EditHeroButton", description="Edit a superhero", label="Edit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Edit, styling=buttonStyling)
deleteHeroButton = Button(name="DeleteHeroButton", description="Delete a superhero", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=buttonStyling)
datasource_superhero = DataSourceElement(name="SuperheroDataSource", dataSourceClass=Superhero, fields=[Superhero_name, Superhero_power, Superhero_badass])
superheroList = DataList(name="SuperheroList", description="A list of superheroes", list_sources={datasource_superhero}, styling=Styling(size=Size(width="100%", height="auto", padding="10px", unit_size=UnitSize.PIXELS)))
SuperheroesListScreen = Screen(name="SuperheroesListScreen", description="Screen displaying a list of superheroes", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={addSuperheroButton, editHeroButton, deleteHeroButton, superheroList}, is_main_page=True, layout=ScreenLayout)
SuperheroesModule = Module(name="SuperheroesModule", screens={SuperheroesListScreen})
gui_model = GUIModel(name="SuperheroesApp", package="com.example.superheroes", versionCode="1", versionName="1.0", description="An application to manage superheroes.", screenCompatibility=True, modules={SuperheroesModule})
