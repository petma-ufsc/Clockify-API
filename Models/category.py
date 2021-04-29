from models import *
import requests


class Category(Model):

    __table__ = "category"
    __fillable__ = ["clockify_id", "name"]
    __primary_key__ = "id"
    __incrementing__ = True

    @classmethod
    def save_from_clockify(cls):
        """Check if all categories in clockify are register as categories in the database.
        Create a new categories if necessary."""
        categories = cls.fetch_all_categories()
        for category in categories:
            Category.update_or_create(
                {"clockify_id": category["clockify_id"]}, {"name": category["name"]}
            )
        return categories

    @staticmethod
    def fetch_all_categories(archived=None):
        """Find all categories from Clockify on NEO's workspace.
        Returns list of dictionaries containing "clockify_id" and "name"
        of every category."""

        url = "{}/workspaces/{}/clients".format(V1_API_URL, WORKSPACE_ID)
        responses = requests.get(url, headers=HEADERS)
        return [
            {"clockify_id": category["id"], "name": category["name"].lower()}
            for category in responses.json()
        ]

    @staticmethod
    def map_all_categories():
        """Returns a dictionary of all categories in database. Dictionary key is category
           clockify id. This should be used to reduce Queries to our DB in other functions."""

        categories_map = {}
        for category in Category.all():
            categories_map[category.clockify_id] = {"id": category.id, "name": category.name}
        return categories_map