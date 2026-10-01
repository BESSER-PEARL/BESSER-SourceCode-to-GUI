from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import Property
from structural_model import FoodSite, SearchBar, Table, Category, Recipe, NutritionInfo, hasCategory, containsSearchBar, hasRecipe, hasNutritionInfo, containsTable

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
searchInputColor = Color(background_color="#E5E7EB", text_color="#4B5563", border_color="#9CA3AF")
searchInputPosition = Position(type=PositionType.Relative)
searchInputSize = Size(width="100%", padding="8px", margin="8px", font_size="16", unit_size=UnitSize.PIXELS)
searchInputStyling = Styling(size=searchInputSize, position=searchInputPosition, color=searchInputColor)
tableColor = Color(background_color="#FFFFFF", text_color="#1F2937", border_color="#E5E7EB")
tablePosition = Position(type=PositionType.Relative)
tableSize = Size(width="100%", padding="10px", margin="16px", font_size="14", unit_size=UnitSize.PIXELS)
tableStyling = Styling(size=tableSize, position=tablePosition, color=tableColor)
searchBarComponent = InputField(name="SearchBar", description="Search input field", type="Text", validationRules="", styling=searchInputStyling)
categoryColumn = DataSourceElement(name="CategoryColumn", dataSourceClass=Category, fields=[Property(name="Category", type=Category)])
recipeColumn = DataSourceElement(name="RecipeColumn", dataSourceClass=Recipe, fields=[Property(name="Recipe", type=Recipe)])
nutritionInfoColumn = DataSourceElement(name="NutritionInfoColumn", dataSourceClass=NutritionInfo, fields=[Property(name="NutritionInfo", type=NutritionInfo)])
tableDataList = DataList(name="FoodTable", description="Table displaying food categories, recipes, and nutrition info", list_sources={categoryColumn, recipeColumn, nutritionInfoColumn}, styling=tableStyling)
FoodSiteScreen = Screen(name="FoodSiteScreen", description="Screen for displaying food site with search and table", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={searchBarComponent, tableDataList}, is_main_page=True, layout=ScreenLayout)
FoodSiteModule = Module(name="FoodSiteModule", screens={FoodSiteScreen})
gui_model = GUIModel(name="FoodSiteApp", package="com.example.foodsite", versionCode="1", versionName="1.0", description="A web application for managing food categories, recipes, and nutrition information.", screenCompatibility=True, modules={FoodSiteModule})
