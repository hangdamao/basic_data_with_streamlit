# # @Project ：basic_data_gui
# # @File    ：1111.py
# # @Author  ：aircraft carrier
# # @Date    ：2023/9/11 19:49
#
# streamlit-option-menu is a simple Streamlit component that allows users to select a single item from a list of options in a menu.
# It is similar in function to st.selectbox(), except that:
# - It uses a simple static list to display the options instead of a dropdown
# - It has configurable icons for each option item and the menu title
#
# It is built on [streamlit-component-template-vue](https://github.com/andfanilo/streamlit-component-template-vue), styled with [Bootstrap](https://getbootstrap.com/) and with icons from [bootstrap-icons](https://icons.getbootstrap.com/)
#
# ## Installation
# ```
# pip install streamlit-option-menu
# ```
#
# ## Parameters
# The `option_menu` function accepts the following parameters:
# - menu_title (required): the title of the menu; pass None to hide the title
# - options (required): list of (string) options to display in the menu; set an option to "---" if you want to insert a section separator
# - default_index (optional, default=0): the index of the selected option by default
# - menu_icon (optional, default="menu-up"): name of the [bootstrap-icon](https://icons.getbootstrap.com/) to be used for the menu title
# - icons (optional, default=["caret-right"]): list of [bootstrap-icon](https://icons.getbootstrap.com/) names to be used for each option; its length should be equal to the length of options
# - orientation (optional, default="vertical"): "vertical" or "horizontal"; whether to display the menu vertically or horizontally
#
# The function returns the (string) option currently selected

## Example
# ```
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("目录", ["Home", 'Settings'],
                           icons=['house', 'gear'], menu_icon="slack", default_index=1)
print(selected)

# horizontal Menu
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
                        icons=['house', 'cloud-upload', "list-task", 'gear'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
print(selected2)
