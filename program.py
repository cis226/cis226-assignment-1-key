"""Program code"""

# David Barnes
# CIS 226
# 05-28-23

# Internal imports.
from beverage import BeverageCollection
from errors import AlreadyImportedError
from user_interface import UserInterface
from utils import CSVProcessor

# Set a constant for the path to the CSV file
PATH_TO_CSV = "./datafiles/beverage_list.csv"


def main(*args):
    """Method to run program"""

    # Create an instance of User Interface class
    ui = UserInterface()

    # Create an instance of the BeverageCollection class.
    beverage_collection = BeverageCollection()

    # Create an instance of the CSVProcessor class.
    csv_processor = CSVProcessor()

    # Display the Welcome Message to the user.
    ui.display_welcome_greeting()

    # Display the Menu and get the response. Store the response in the choice
    # integer. This is the 'primer' run of displaying and getting.
    choice = ui.display_menu_and_get_response()

    # While the choice is not exit program
    while choice != 5:
        if choice == 1:
            # Load the CSV File
            try:
                csv_processor.import_csv(beverage_collection, PATH_TO_CSV)
                ui.display_import_success()

            except AlreadyImportedError:
                ui.display_already_imported_error()
            except FileNotFoundError:
                ui.display_file_not_found_error()
            except EOFError:
                ui.display_empty_file_error()

        elif choice == 2:
            # Print Entire List Of Items
            all_item_string = str(beverage_collection)
            if all_item_string:
                ui.display_all_items(all_item_string)
            else:
                ui.display_all_items_error()

        elif choice == 3:
            # Search for an Item
            search_query = ui.get_search_query()
            item_info = beverage_collection.find_by_id(search_query)
            if item_info:
                ui.display_item_found(item_info)
            else:
                ui.display_item_found_error()

        elif choice == 4:
            # Collect information for a new item and add it to the collection
            new_item_info = ui.get_new_item_information()
            if beverage_collection.find_by_id(new_item_info[0]) is None:
                beverage_collection.add(
                    new_item_info[0],
                    new_item_info[1],
                    new_item_info[2],
                    float(new_item_info[3]),
                    new_item_info[4] == "True",
                )
                ui.display_add_beverage_success()
            else:
                ui.display_beverage_already_exists_error()

        # Get the new choice of what to do from the user.
        choice = ui.display_menu_and_get_response()
