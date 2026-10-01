# generated_gui_model_v2.py
# Extends generated_gui_model.py with two fixes:
#   Fix 1 — resolve targetScreen bindings on all Navigate buttons
#   Fix 2 — add sidebar Navigate buttons on every secondary screen so that
#            every GT inter-page link is captured

import os, sys
_base = r"D:\VSCodeBESSER\HTML-to-BUML-Convertor"
_here = os.path.join(_base, "evaluation_shards", "buml_output", "gui_model")
sys.path.insert(0, _base)
exec(open(os.path.join(_here, "generated_gui_model.py")).read())

# ── Fix 1: resolve targetScreen on all existing Navigate buttons ─────────────
dashboardNavLink1.targetScreen = HomePage           # NavDashboard    → HomePage
dashboardNavLink2.targetScreen = UserProfileScreen  # NavUserProfile  → UserProfileScreen
dashboardNavLink3.targetScreen = AddNewPostScreen   # NavAddNewPost   → AddNewPostScreen
dashboardNavLink4.targetScreen = TablesScreen       # NavTables       → TablesScreen
dashboardNavLink5.targetScreen = ErrorsScreen       # NavErrors       → ErrorsScreen
backToDashboardButton.targetScreen = HomePage       # Errors → HomePage

# ── Fix 2: add sidebar nav buttons to each secondary screen ──────────────────
# Each page in the Shards Dashboard has the same 5-item sidebar, so every
# screen must link to the other 4 screens.  We create fresh Button objects
# per screen to avoid shared object mutations.

def _make_sidebar_buttons(screen_name, screens_map):
    """Return Navigate buttons for every screen except the caller's own."""
    buttons = []
    for label, target in screens_map.items():
        if target is not None:
            btn = Button(
                name=f"SidebarNav_{screen_name}_to_{label}",
                description=f"Sidebar link from {screen_name} to {label}",
                label=label,
                buttonType=ButtonType.TextButton,
                actionType=ButtonActionType.Navigate,
                targetScreen=target,
                styling=SecondaryButtonStyling,
            )
            buttons.append(btn)
    return buttons

_all_screens = {
    "HomePage":           HomePage,
    "UserProfileScreen":  UserProfileScreen,
    "AddNewPostScreen":   AddNewPostScreen,
    "TablesScreen":       TablesScreen,
    "ErrorsScreen":       ErrorsScreen,
}

# UserProfileScreen — add links to the 4 other pages
for btn in _make_sidebar_buttons("UserProfile",
        {k: v for k, v in _all_screens.items() if k != "UserProfileScreen"}):
    UserProfileScreen.view_elements.add(btn)

# AddNewPostScreen — add links to the 4 other pages
for btn in _make_sidebar_buttons("AddNewPost",
        {k: v for k, v in _all_screens.items() if k != "AddNewPostScreen"}):
    AddNewPostScreen.view_elements.add(btn)

# TablesScreen — add links to the 4 other pages
for btn in _make_sidebar_buttons("Tables",
        {k: v for k, v in _all_screens.items() if k != "TablesScreen"}):
    TablesScreen.view_elements.add(btn)

# ErrorsScreen — already has backToDashboardButton (now resolved to HomePage).
# Add links to the remaining 3 pages.
for btn in _make_sidebar_buttons("Errors",
        {k: v for k, v in _all_screens.items() if k not in ("ErrorsScreen", "HomePage")}):
    ErrorsScreen.view_elements.add(btn)
