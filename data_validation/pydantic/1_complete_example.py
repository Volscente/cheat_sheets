from typing import Optional, Union, Dict, List, TypedDict, Any
import json

from pydantic import BaseModel, Field, field_validator
import pandas as pd

class MenuItemOptionSelection(BaseModel):
    """
    Define a so-called Option Group Selection that is added to a Product.
    A product can have a list of Option Groups (``MenuItemOption``),
    each constituted by a list of Option Group Selection.

    Example:
        - Product: Pizza Margherita 9€
        - Option Group: Crust
        - Option Group Selections: Salami Crust + 3€, Cheese Crust +4€

    Attributes:
        selection_name (str): Name of the selection (e.g., "Salami Crust")
        selection_price (Union[float, str, None]): Price of the selection
        selection_description (Optional[str]): Description of the selection
    """

    selection_name: str = Field(
        ..., description="The name of the selection.", alias="selection_name"
    )
    selection_price: Union[float, str, None] = Field(
        ...,
        description="Price of the selection",
        alias="selection_price",
        union_mode="left_to_right",
    )
    selection_description: Optional[str] = Field(
        None,
        description="Description of the selection.",
        alias="selection_description",
    )

    @classmethod
    def get_schema(cls) -> Dict[str, Any]:
        """
        Return the JSON schema for MenuItemOptionSelection.
        """
        return {
            "type": "object",
            "description": "A single selection available within an option group.",
            "properties": {
                "selection_name": {
                    "type": "string",
                    "description": "The name of the selection (e.g., 'Salami Crust').",
                },
                "selection_price": {
                    "anyOf": [
                        {"type": "number", "format": "float"},
                        {"type": "string"},
                        {"type": "null"},
                    ],
                    "description": "Price of the selection, which may be numeric, a formatted string, or null.",
                },
                "selection_description": {
                    "type": ["string", "null"],
                    "description": "Optional description of the selection.",
                },
            },
            "required": ["selection_name", "selection_price"],
        }

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the model as a Python dictionary (using field aliases).
        """
        return self.model_dump(by_alias=True)

    def as_json(self) -> str:
        """
        Return the model as a JSON string (with indentation for readability).
        """
        return self.model_dump_json(by_alias=True, indent=2)

    def as_df(self) -> pd.DataFrame:
        """
        Return the model as a single-row pandas DataFrame.
        """
        return pd.DataFrame([self.as_dict()])


class MenuItemOption(BaseModel):
    """
    Define a so-called Option Group, composed of a list of Option Group Selections (``MenuItemOptionSelection``).

    Example:
        - Product: Pizza Margherita 9€
        - Option Group: Crust
        - Option Group Selections: Salami Crust +3€, Cheese Crust +4€

    Attributes:
        option_name (str): Name of the option.
        option_is_mandatory (bool): Flag indicating whether the Option Group is mandatory.
        option_selections (List[MenuItemOptionSelection]): List of possible Option Group Selections.
    """

    option_name: str = Field(
        ..., description="The name of the option.", alias="option_name"
    )
    option_is_mandatory: Optional[bool] = Field(
        ...,
        description="Flag indicating whether the Option Group is mandatory.",
        alias="option_is_mandatory",
    )
    option_selections: List[MenuItemOptionSelection] = Field(
        ...,
        description="List of possible Option Group Selections.",
        alias="option_selections",
    )

    @classmethod
    def get_schema(cls) -> Dict[str, Any]:
        """
        Return the JSON schema for MenuItemOption.
        """
        return {
            "type": "object",
            "description": "An option group available for a menu item.",
            "properties": {
                "option_name": {
                    "type": "string",
                    "description": "The name of the option group.",
                },
                "option_is_mandatory": {
                    "type": ["boolean", "null"],
                    "description": "Whether this option group is mandatory.",
                },
                "option_selections": {
                    "type": "array",
                    "description": "List of selections available within this option group.",
                    "items": MenuItemOptionSelection.get_schema(),
                },
            },
            "required": [
                "option_name",
                "option_is_mandatory",
                "option_selections",
            ],
        }

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the model as a Python dictionary (using field aliases).
        """
        return self.model_dump(by_alias=True)

    def as_json(self) -> str:
        """
        Return the model as a JSON string (with indentation for readability).
        """
        return self.model_dump_json(by_alias=True, indent=2)

    def as_df(self) -> pd.DataFrame:
        """
        Return the model as a pandas DataFrame, expanding nested selections if needed.
        """
        data = self.as_dict()

        # Flatten nested selections (each selection becomes a row)
        if data.get("option_selections"):
            df_selections = pd.DataFrame(data["option_selections"])
            df_selections.insert(0, "option_name", data["option_name"])
            df_selections.insert(
                1, "option_is_mandatory", data["option_is_mandatory"]
            )
            return df_selections

        # Fallback to single-row DataFrame if no selections
        return pd.DataFrame([data])


class MenuItemExtractionOptions(BaseModel):
    """
    Define a Product inside a menu that is able to support Option Groups (``MenuItemOption``).

    Example:
        - Product: Pizza Margherita 9€
        - Option Group: Crust
        - Option Group Selections: Salami Crust +3€, Cheese Crust +4€

    Attributes:
        item_name (str): Name of the item
        item_price (Union[float, str, None]): Price of the item
        item_size (Optional[str]): Size of the item
        item_description (Optional[str]): Description of the item
        item_category (Optional[str]): Category of the item
        item_language (Optional[str]): Language of the item
        item_options (List[MenuItemOption]): List of possible Option Groups
    """

    item_name: str = Field(
        ..., description="Name of the item", alias="item_name"
    )
    item_price: Union[float, str, None] = Field(
        ...,
        description="Price of the item",
        alias="item_price",
        union_mode="left_to_right",
    )
    item_size: Optional[str] = Field(
        None, description="Size of the item", alias="item_size"
    )
    item_description: Optional[str] = Field(
        None, description="Description of the item", alias="item_description"
    )
    item_category: Optional[str] = Field(
        None, description="Category of the item", alias="item_category"
    )
    item_language: Optional[str] = Field(
        None, description="Language of the item", alias="item_language"
    )
    item_options: List[MenuItemOption] = Field(
        default_factory=list,
        description="List of possible Option Groups",
        alias="item_options",
    )

    class Config:
        populate_by_name = True

    @classmethod
    def get_schema(cls) -> Dict[str, Any]:
        """
        Return the JSON schema for MenuItemExtractionOptions.
        """
        return {
            "type": "object",
            "description": "A single item on a menu with possible option groups and selections.",
            "properties": {
                "item_name": {
                    "type": "string",
                    "description": "Name of the item.",
                },
                "item_price": {
                    "anyOf": [
                        {"type": "number", "format": "float"},
                        {"type": "string"},
                        {"type": "null"},
                    ],
                    "description": "Price of the item, which may be numeric, a formatted string, or null.",
                },
                "item_size": {
                    "type": ["string", "null"],
                    "description": "Size of the item, if applicable.",
                },
                "item_description": {
                    "type": ["string", "null"],
                    "description": "Description of the item, if provided.",
                },
                "item_category": {
                    "type": ["string", "null"],
                    "description": "Category of the item, if available.",
                },
                "item_language": {
                    "type": ["string", "null"],
                    "description": "Language code (ISO 639-1) of the item, if specified.",
                },
                "item_options": {
                    "type": "array",
                    "description": "List of possible Option Groups for the item.",
                    "items": MenuItemOption.get_schema(),
                },
            },
            "required": ["item_name", "item_price"],
        }

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the model as a Python dictionary (using field aliases).
        Nested models (MenuItemOption) are converted via their own as_dict().
        """
        data = self.model_dump(by_alias=True)
        data["item_options"] = [opt.as_dict() for opt in self.item_options]
        return data

    def as_json(self) -> str:
        """
        Return the model as a JSON string (with indentation for readability).
        """
        return json.dumps(self.as_dict(), indent=2, ensure_ascii=False)

    def as_df(self) -> pd.DataFrame:
        """
        Return the model as a pandas DataFrame.
        Each MenuItemOptionSelection under item_options becomes its own row,
        flattened with the parent item’s information.
        """
        base_data = {
            "item_name": self.item_name,
            "item_price": self.item_price,
            "item_size": self.item_size,
            "item_description": self.item_description,
            "item_category": self.item_category,
            "item_language": self.item_language,
        }

        if not self.item_options:
            # no options — single-row DataFrame
            return pd.DataFrame([base_data])

        # Flatten nested options → selections
        rows = []
        for option in self.item_options:
            option_df = option.as_df()
            for _, opt_row in option_df.iterrows():
                row = {**base_data, **opt_row.to_dict()}
                rows.append(row)

        return pd.DataFrame(rows)


class MenuExtractionOptions(BaseModel):
    """
    Define a Menu that includes Products (``MenuItemExtractionOptions``) able to support Option Groups.

    Attributes:
        items (List[MenuItemExtractionOptions]): List of possible Products
    """

    items: List[MenuItemExtractionOptions] = Field(default_factory=list)

    @classmethod
    def get_schema(cls) -> Dict:
        return {
            "type": "array",
            "description": "A list of menu items with option groups.",
            "items": MenuItemExtractionOptions.get_schema(),
        }

    def as_dict(self) -> Dict:
        return self.model_dump(by_alias=True)

    def as_json(self) -> str:
        return self.model_dump_json(by_alias=True)

    def as_df(self) -> pd.DataFrame:
        data_list = [item.as_dict() for item in self.items]
        return pd.DataFrame(data_list)
